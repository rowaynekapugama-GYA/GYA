(function(){
  // Header shadow on scroll
  const header=document.querySelector('.header');
  const onScroll=()=>header&&header.classList.toggle('scrolled',window.scrollY>8);
  onScroll();addEventListener('scroll',onScroll,{passive:true});

  // Mobile menu
  const burger=document.querySelector('.burger');
  const mm=document.querySelector('.mobile-menu');
  if(burger&&mm){
    burger.addEventListener('click',()=>{
      const open=mm.classList.toggle('open');
      burger.setAttribute('aria-expanded',open);
      document.body.style.overflow=open?'hidden':'';
    });
    mm.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
      mm.classList.remove('open');burger.setAttribute('aria-expanded','false');document.body.style.overflow='';
    }));
  }

  // Mark current nav item
  const path=location.pathname.split('/').pop()||'index.html';
  document.querySelectorAll('.menu a, .mobile-menu a.item').forEach(a=>{
    if((a.getAttribute('href')||'').split('/').pop()===path)a.setAttribute('aria-current','page');
  });

  // Reveal on scroll
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}}),{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

  // Site screenshots: the screenshot service returns a small placeholder while it
  // renders a fresh capture. Retry a few times, then fall back to the styled card.
  document.querySelectorAll('img[data-mshot]').forEach(img=>{
    let tries=0;
    const check=()=>{
      if(img.naturalWidth && img.naturalWidth<500){
        if(tries++<4){const u=img.src.split('&_r=')[0];setTimeout(()=>{img.src=u+'&_r='+Date.now()},3000);}
        else img.parentNode.classList.add('noimg');
      }
    };
    img.addEventListener('load',check);
    if(img.complete)check();
  });

  // Contact modal
  const modal=document.getElementById('contact-modal');
  if(modal){
    const open=()=>{modal.classList.add('open');document.body.style.overflow='hidden';modal.querySelector('input')?.focus();};
    const close=()=>{modal.classList.remove('open');document.body.style.overflow='';};
    document.querySelectorAll('[data-open-contact]').forEach(b=>b.addEventListener('click',e=>{e.preventDefault();open();}));
    modal.querySelectorAll('[data-close]').forEach(b=>b.addEventListener('click',close));
    addEventListener('keydown',e=>{if(e.key==='Escape')close();});
    if(location.hash==='#talk')open();
  }

  // Contact forms (front-end only; wire to your endpoint)
  document.querySelectorAll('form[data-contact]').forEach(form=>{
    form.addEventListener('submit',e=>{
      e.preventDefault();
      const btn=form.querySelector('button[type=submit]');
      btn.textContent='Sent. We will call you.';btn.disabled=true;
    });
  });
})();
