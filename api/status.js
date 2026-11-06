const { config, send } = require('./_ai');

module.exports = (req, res) => {
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    res.setHeader('Allow', 'GET, HEAD');
    return send(res, 405, { error: 'Method not allowed.' });
  }
  const { key, model } = config();
  return send(res, 200, { configured: Boolean(key && model), model });
};
