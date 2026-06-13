/**
 * Portfolio – main.js
 * Features:
 *   1. Nav scroll tracking (adds .scrolled class)
 *   2. Smooth scroll for nav links (CSS handles it via scroll-behavior, but
 *      this handles offset for the fixed nav)
 *   3. IntersectionObserver fade-in animation
 */

(function () {
  'use strict';

  /* -------------------------------------------------------
   * 1. Nav: add .scrolled when page is scrolled down
   * ------------------------------------------------------- */
  const nav = document.getElementById('nav');

  function onScroll() {
    if (window.scrollY > 60) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  // Run once on load in case page is already scrolled
  onScroll();

  /* -------------------------------------------------------
   * 2. Smooth scroll with fixed-nav offset
   * ------------------------------------------------------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      const href = link.getAttribute('href');
      if (href === '#') return;

      const target = document.querySelector(href);
      if (!target) return;

      e.preventDefault();

      const navHeight = nav ? nav.offsetHeight : 0;
      const targetTop = target.getBoundingClientRect().top + window.scrollY - navHeight;

      window.scrollTo({ top: targetTop, behavior: 'smooth' });
    });
  });

  /* -------------------------------------------------------
   * 3. Fade-in via IntersectionObserver
   * ------------------------------------------------------- */
  const fadeEls = document.querySelectorAll('.fade-in');

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            // Stop observing once visible
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );

    fadeEls.forEach(function (el) {
      observer.observe(el);
    });
  } else {
    // Fallback: show all immediately for older browsers
    fadeEls.forEach(function (el) {
      el.classList.add('visible');
    });
  }
})();
