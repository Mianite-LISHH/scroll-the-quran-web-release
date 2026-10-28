const p=location.pathname.replace(/\/+$/, '')||'/';if(p!==location.pathname)history.replaceState(null,'',p+location.search+location.hash);
