const { MAX_BODY_CHARS, config, send, sameOrigin, limited } = require('./_ai');

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return send(res, 405, { error: 'Method not allowed.' });
  }

  const { key, model, base } = config();
  if (!key || !model) {
    return send(res, 503, { error: 'AI is not connected yet. Set AI_API_KEY, AI_MODEL and AI_BASE_URL in the Vercel project settings, then redeploy.' });
  }
  if (!base.startsWith('https://')) return send(res, 400, { error: 'AI_BASE_URL must use HTTPS.' });
  if (!sameOrigin(req)) return send(res, 403, { error: 'Requests are only accepted from this website.' });
  if (limited(req)) return send(res, 429, { error: 'Too many AI requests. Please wait a few minutes and try again.' });

  let data = req.body;
  try {
    if (typeof data === 'string') data = JSON.parse(data);
    if (JSON.stringify(data || {}).length > MAX_BODY_CHARS) return send(res, 413, { error: 'Request too large.' });
    const messages = data && data.messages;
    if (!Array.isArray(messages) || messages.length === 0 || messages.length > 30) throw new Error('Invalid messages');
    const clean = messages
      .filter(m => m && typeof m === 'object' && ['system', 'user', 'assistant'].includes(m.role) && 'content' in m)
      .map(m => ({ role: m.role, content: String(m.content).slice(0, 12000) }));
    if (clean.length === 0) throw new Error('Invalid messages');

    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 55000);
    let upstream;
    try {
      upstream = await fetch(base + '/chat/completions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + key },
        body: JSON.stringify({ model, messages: clean, temperature: 0.5 }),
        signal: controller.signal,
      });
    } finally {
      clearTimeout(timer);
    }

    if (!upstream.ok) {
      return send(res, 502, { error: `AI provider returned HTTP ${upstream.status}. Check the model, API key, quota and base URL.` });
    }
    const result = await upstream.json();
    const text = result && result.choices && result.choices[0] && result.choices[0].message && result.choices[0].message.content;
    if (typeof text !== 'string') return send(res, 502, { error: 'The AI service returned an unexpected reply.' });
    return send(res, 200, { text });
  } catch (err) {
    if (err instanceof SyntaxError || (err && err.message === 'Invalid messages')) {
      return send(res, 400, { error: 'Invalid request.' });
    }
    return send(res, 502, { error: 'Could not reach the AI provider. Check your configuration and connection.' });
  }
};
