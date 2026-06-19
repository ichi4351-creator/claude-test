/* =============================================
   Email obfuscation (S-C1)
   ============================================= */
const u = 'ichi.4351';
const d = 'gmail.com';
const emailEl   = document.getElementById('contact-email');
const emailText = document.getElementById('contact-email-text');
if (emailEl && emailText) {
  const addr = `${u}@${d}`;
  emailEl.href = `mailto:${addr}`;
  emailText.textContent = addr;
}

/* =============================================
   Loader
   ============================================= */
window.addEventListener('load', () => {
  const loader = document.getElementById('loader');
  if (loader) {
    setTimeout(() => {
      loader.classList.add('done');
      setTimeout(() => loader.remove(), 600);
    }, 1300);
  }
});

/* =============================================
   Nav — scroll shadow + hamburger
   ============================================= */
const nav       = document.getElementById('nav');
const hamburger = document.getElementById('hamburger');
const navLinks  = document.getElementById('nav-links');

if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 30);
  }, { passive: true });
}

if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    const open = hamburger.classList.toggle('open');
    hamburger.setAttribute('aria-expanded', open);
    navLinks.classList.toggle('open', open);
  });

  navLinks.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      hamburger.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
      navLinks.classList.remove('open');
    });
  });
}

/* =============================================
   Smooth scroll with nav offset (R-S1: null guard)
   ============================================= */
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', e => {
    const target = document.querySelector(link.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const offset = nav ? nav.getBoundingClientRect().height : 0;
    const top = target.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top, behavior: 'smooth' });
  });
});

/* =============================================
   Reveal on scroll — R-S2: siblings ループに統一して重複除去
   ============================================= */
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const siblings = entry.target.parentElement.querySelectorAll('.reveal:not(.visible)');
    siblings.forEach((el, idx) => {
      setTimeout(() => el.classList.add('visible'), idx * 90);
    });
    revealObserver.unobserve(entry.target);
  });
}, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

/* =============================================
   Parallax — P-W2: rAF スロットリング
   ============================================= */
const parallaxEls = document.querySelectorAll('.parallax-bg');
function updateParallax() {
  parallaxEls.forEach(el => {
    const section = el.parentElement;
    const rect = section.getBoundingClientRect();
    el.style.transform = `translateY(${rect.top * 0.35}px)`;
  });
}
let rafId = null;
window.addEventListener('scroll', () => {
  if (rafId) return;
  rafId = requestAnimationFrame(() => {
    updateParallax();
    rafId = null;
  });
}, { passive: true });
updateParallax();

/* =============================================
   Lightbox — A-C1: フォーカストラップ / A-W1: hidden属性 / E-W1: onerror
   ============================================= */
const lightbox = document.getElementById('lightbox');
const lbImg    = document.getElementById('lightbox-img');
const lbClose  = document.getElementById('lightbox-close');

let lastFocused = null;

function openLightbox(img) {
  lastFocused = img;
  lbImg.src   = img.src;
  lbImg.alt   = img.alt;
  lbImg.onerror = () => closeLightbox();
  lightbox.removeAttribute('hidden');
  document.body.style.overflow = 'hidden';
  lbClose.focus();
}

function closeLightbox() {
  lightbox.setAttribute('hidden', '');
  document.body.style.overflow = '';
  lbImg.src = '';
  if (lastFocused) lastFocused.focus();
}

/* カード画像クリック + A-W2: キーボード（Enter/Space）対応 */
document.querySelectorAll('.card-img-wrap').forEach(wrap => {
  const img = wrap.querySelector('img');
  if (!img) return;

  wrap.style.cursor = 'zoom-in';

  const trigger = () => openLightbox(img);
  wrap.addEventListener('click', trigger);
  wrap.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      trigger();
    }
  });
});

lbClose.addEventListener('click', closeLightbox);
lightbox.addEventListener('click', e => { if (e.target === lightbox) closeLightbox(); });

/* A-C1: フォーカストラップ + Escape */
document.addEventListener('keydown', e => {
  if (lightbox.hasAttribute('hidden')) return;
  if (e.key === 'Escape') { closeLightbox(); return; }
  if (e.key === 'Tab') {
    e.preventDefault(); // 単一フォーカス要素（lbClose）でループ
    lbClose.focus();
  }
});

/* =============================================
   Active nav highlight on scroll
   ============================================= */
const sections   = document.querySelectorAll('section[id]');
const navAnchors = document.querySelectorAll('.nav-link');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navAnchors.forEach(a => {
        a.classList.toggle('active', a.getAttribute('href') === `#${entry.target.id}`);
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => sectionObserver.observe(s));
