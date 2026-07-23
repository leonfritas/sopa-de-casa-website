// nav background on scroll
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 40);
});

// reveal on scroll
const revealEls = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.15 });
revealEls.forEach(el => io.observe(el));

// carrossel de temperos
const track = document.getElementById('spice-track');
const btnPrev = document.getElementById('btn-prev');
const btnNext = document.getElementById('btn-next');

if(track && btnPrev && btnNext) {
  btnNext.addEventListener('click', () => {
    // largura de um card + gap
    const itemWidth = track.querySelector('.spice-card').offsetWidth + 22;
    track.scrollBy({ left: itemWidth, behavior: 'smooth' });
  });
  btnPrev.addEventListener('click', () => {
    const itemWidth = track.querySelector('.spice-card').offsetWidth + 22;
    track.scrollBy({ left: -itemWidth, behavior: 'smooth' });
  });
}
