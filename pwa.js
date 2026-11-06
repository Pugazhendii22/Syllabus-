(() => {
  const installButton = document.querySelector('#installApp');
  const installDialog = document.querySelector('#installDialog');
  const helpText = document.querySelector('#installHelp');
  let installPrompt;
  const standalone = () => window.matchMedia('(display-mode: standalone)').matches || navigator.standalone === true;
  const hideIfInstalled = () => { installButton.hidden = standalone(); };
  hideIfInstalled();
  window.addEventListener('beforeinstallprompt', event => {
    event.preventDefault();
    installPrompt = event;
    hideIfInstalled();
  });
  window.addEventListener('appinstalled', () => { installPrompt = null; installButton.hidden = true; });
  installButton.addEventListener('click', async () => {
    if (installPrompt) {
      const prompt = installPrompt;
      installPrompt = null;
      await prompt.prompt();
      return;
    }
    const isApple = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    helpText.textContent = isApple
      ? 'On your iPhone or iPad, tap Share (the square with an arrow), scroll down, choose Add to Home Screen, then tap Add. If you see “Open as Web App”, leave it on.'
      : 'Open your browser menu and choose Install app or Add to Home Screen. The wording may vary by browser.';
    installDialog.showModal();
  });
  document.querySelector('#closeInstall').addEventListener('click', () => installDialog.close());
  document.querySelector('#doneInstall').addEventListener('click', () => installDialog.close());
  if ('serviceWorker' in navigator && window.isSecureContext) {
    window.addEventListener('load', () => navigator.serviceWorker.register('/sw.js').catch(() => {
      // The app remains usable online if offline support cannot be registered.
    }));
  }
})();
