(() => {
  const $ = selector => document.querySelector(selector);
  const installButton = $('#installApp');
  const installDialog = $('#installDialog');
  const helpText = $('#installHelp');
  const notice = $('#updateNotice');
  const pullStatus = $('#pullStatus');
  const pullLabel = $('#pullLabel');
  const refreshButton = $('#refreshApp');
  const page = $('.page');
  const header = $('.main > header');
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
    return ['#topicInput','#chatInput'].some(id => { const input=$(id); return input && input.value && input.value.trim(); }) || !!window.ammuHasChatDrafts?.();
  }
  let start = null, armed = false, refreshing = false, hideTimer = null;
  function setPullDistance(distance) {
    const value = Math.round(Math.max(0, Math.min(64, distance)) * 100) / 100;
    page.style.setProperty('--pull-distance', value + 'px');
    pullStatus.style.setProperty('--pull-distance', value + 'px');
    pullStatus.style.setProperty('--pull-opacity', String(Math.min(1, value / 32)));
  }
  function positionIndicator() {
    // Put the reveal immediately below the header, not over its buttons or the iOS status bar.
    const bottom = header.getBoundingClientRect().bottom;
    pullStatus.style.setProperty('--pull-top', Math.max(0, bottom) + 'px');
  }
  function resetPull(animate = true) {
    start = null; armed = false;
    pullStatus.classList.remove('is-armed');
    pullStatus.classList.toggle('is-settling', animate);
    page.classList.toggle('pull-settling', animate);
    setPullDistance(0);
    if (hideTimer !== null) window.clearTimeout(hideTimer);
    if (animate) {
      hideTimer = window.setTimeout(() => {
        pullStatus.hidden = true;
        pullStatus.classList.remove('is-settling');
        page.classList.remove('pull-settling');
        hideTimer = null;
      }, 200);
    } else {
      pullStatus.hidden = true;
      pullStatus.classList.remove('is-settling');
      page.classList.remove('pull-settling');
      hideTimer = null;
    }
  }
  function refresh(fromPull = false) {
    if (refreshing) return;
    if (hasUnsentText() && !window.confirm('Refreshing clears text you have not sent. Refresh anyway?')) {
      if (fromPull) resetPull();
      return;
    }
    refreshing = true;
    refreshButton.classList.add('is-refreshing');
    refreshButton.setAttribute('aria-label', 'Refreshing app');
    if (fromPull) {
      positionIndicator();
      pullStatus.hidden = false;
      pullStatus.classList.remove('is-armed', 'is-settling');
      page.classList.remove('pull-settling');
      pullStatus.classList.add('is-refreshing');
      pullLabel.textContent = 'Refreshing';
      setPullDistance(64);
    }
    if (registration && registration.waiting) {
      applyingUpdate = true;
      $('#reloadUpdate').disabled = true;
      registration.waiting.postMessage({type:'SKIP_WAITING'});
      // Fallback for a browser that does not deliver controllerchange.
      window.setTimeout(reloadOnce, 5000);
    } else reloadOnce();
  }
  refreshButton.addEventListener('click', () => refresh());
  $('#reloadUpdate').addEventListener('click', () => refresh());
  $('#laterUpdate').addEventListener('click', () => { notice.hidden = true; });

  // Pull from the top only. Never intercept a picker, text field or nested scroller.
  function nestedScroller(target) {
    for (let node = target; node && node !== document.body && node !== document.documentElement; node = node.parentElement) {
      if (node.scrollHeight > node.clientHeight + 1 && /(auto|scroll)/.test(window.getComputedStyle(node).overflowY)) return true;
    }
    return false;
  }
  document.addEventListener('touchstart', event => {
    if (refreshing) return;
    resetPull(false);
    if (event.touches.length !== 1 || window.scrollY > 0 || document.querySelector('dialog[open]')) return;
    const target = event.target;
    if (target.closest && target.closest('button,input,textarea,select,[contenteditable="true"]')) return;
    if (nestedScroller(target)) return;
    start = {x:event.touches[0].clientX, y:event.touches[0].clientY};
    positionIndicator();
  }, {passive:true});
  document.addEventListener('touchmove', event => {
    if (!start) return;
    if (event.touches.length !== 1 || window.scrollY > 0) { resetPull(); return; }
    const dx = event.touches[0].clientX - start.x, dy = event.touches[0].clientY - start.y;
    if (dy <= 8 || Math.abs(dx) > dy * 0.7) {
      armed = false;
      pullStatus.classList.remove('is-armed');
      pullStatus.hidden = true;
      setPullDistance(0);
      return;
    }
    if (event.cancelable) event.preventDefault();
    const nextArmed = dy >= 95;
    if (armed !== nextArmed || pullStatus.hidden) {
      pullLabel.textContent = nextArmed ? 'Release to refresh' : 'Pull down to refresh';
    }
    armed = nextArmed;
    pullStatus.hidden = false;
    pullStatus.classList.toggle('is-armed', armed);
    // Resistance makes the page travel less than the finger, like a native pull.
    setPullDistance(Math.min(64, (dy - 8) * 0.68));
  }, {passive:false});
  document.addEventListener('touchend', () => {
    if (refreshing || !start) return;
    const shouldRefresh = !!start && armed;
    start = null;
    if (shouldRefresh) refresh(true); else resetPull();
  }, {passive:true});
  document.addEventListener('touchcancel', () => { if (!refreshing) resetPull(); }, {passive:true});

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
