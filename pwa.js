(() => {
  const $ = selector => document.querySelector(selector);
  const installButton = $('#installApp');
  const installDialog = $('#installDialog');
  const helpText = $('#installHelp');
  const notice = $('#updateNotice');
  const pullStatus = $('#pullStatus');
  let installPrompt, registration, applyingUpdate = false, didReload = false;
  const standalone = () => window.matchMedia('(display-mode: standalone)').matches || navigator.standalone === true;
  const hideIfInstalled = () => { installButton.hidden = standalone(); };
  hideIfInstalled();
  window.addEventListener('beforeinstallprompt', event => {
    event.preventDefault(); installPrompt = event; hideIfInstalled();
  });
  window.addEventListener('appinstalled', () => { installPrompt = null; installButton.hidden = true; });
  installButton.addEventListener('click', async () => {
    if (installPrompt) { const prompt = installPrompt; installPrompt = null; await prompt.prompt(); return; }
    const isApple = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    helpText.textContent = isApple
      ? 'On your iPhone or iPad, tap Share (the square with an arrow), scroll down, choose Add to Home Screen, then tap Add. If you see “Open as Web App”, leave it on.'
      : 'Open your browser menu and choose Install app or Add to Home Screen. The wording may vary by browser.';
    installDialog.showModal();
  });
  $('#closeInstall').addEventListener('click', () => installDialog.close());
  $('#doneInstall').addEventListener('click', () => installDialog.close());

  const reloadOnce = () => { if (!didReload) { didReload = true; window.location.reload(); } };
  function hasUnsentText() {
    return ['#topicInput','#chatInput'].some(id => { const input=$(id); return input && input.value && input.value.trim(); });
  }
  function refresh() {
    if (hasUnsentText() && !window.confirm('Refreshing clears text you have not sent. Refresh anyway?')) return;
    if (registration && registration.waiting) {
      applyingUpdate = true;
      $('#reloadUpdate').disabled = true;
      registration.waiting.postMessage({type:'SKIP_WAITING'});
      // Fallback for a browser that does not deliver controllerchange.
      window.setTimeout(reloadOnce, 5000);
    } else reloadOnce();
  }
  $('#refreshApp').addEventListener('click', refresh);
  $('#reloadUpdate').addEventListener('click', refresh);
  $('#laterUpdate').addEventListener('click', () => { notice.hidden = true; });

  // Pull from the top only. Never intercept a picker, text field or nested scroller.
  let start = null, armed = false;
  function nestedScroller(target) {
    for (let node = target; node && node !== document.body && node !== document.documentElement; node = node.parentElement) {
      if (node.scrollHeight > node.clientHeight + 1 && /(auto|scroll)/.test(window.getComputedStyle(node).overflowY)) return true;
    }
    return false;
  }
  document.addEventListener('touchstart', event => {
    start = null; armed = false; pullStatus.hidden = true;
    if (event.touches.length !== 1 || window.scrollY > 0 || document.querySelector('dialog[open]')) return;
    const target = event.target;
    if (target.closest && target.closest('button,input,textarea,select,[contenteditable="true"]')) return;
    if (nestedScroller(target)) return;
    start = {x:event.touches[0].clientX, y:event.touches[0].clientY};
  }, {passive:true});
  document.addEventListener('touchmove', event => {
    if (!start || event.touches.length !== 1 || window.scrollY > 0) return;
    const dx = event.touches[0].clientX - start.x, dy = event.touches[0].clientY - start.y;
    if (dy <= 8 || Math.abs(dx) > dy * 0.7) { armed = false; pullStatus.hidden = true; return; }
    if (event.cancelable) event.preventDefault();
    armed = dy >= 95;
    pullStatus.hidden = false;
    pullStatus.textContent = armed ? 'Release to refresh ↻' : 'Pull down to refresh ↻';
  }, {passive:false});
  document.addEventListener('touchend', () => {
    const shouldRefresh = !!start && armed; start = null; armed = false; pullStatus.hidden = true;
    if (shouldRefresh) refresh();
  }, {passive:true});
  document.addEventListener('touchcancel', () => { start = null; armed = false; pullStatus.hidden = true; }, {passive:true});

  if ('serviceWorker' in navigator && window.isSecureContext) {
    const sw = navigator.serviceWorker;
    sw.addEventListener('controllerchange', () => { if (applyingUpdate) reloadOnce(); });
    const showUpdate = () => { if (registration && registration.waiting && sw.controller) notice.hidden = false; };
    window.addEventListener('load', () => {
      sw.register('/sw.js', {updateViaCache:'none'}).then(reg => {
        registration = reg;
        showUpdate();
        reg.addEventListener('updatefound', () => {
          const worker = reg.installing;
          if (worker) worker.addEventListener('statechange', () => { if (worker.state === 'installed') showUpdate(); });
        });
        reg.update().catch(() => {});
      }).catch(() => { /* Online use still works without offline support. */ });
    });
    document.addEventListener('visibilitychange', () => {
      if (!document.hidden && registration) { showUpdate(); registration.update().catch(() => {}); }
    });
    window.setInterval(() => { if (registration) registration.update().catch(() => {}); }, 60 * 60 * 1000);
  }
})();
