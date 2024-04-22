document.addEventListener('DOMContentLoaded', function() {
  const slides = document.querySelectorAll('.slide');
  let currentSlide = 0;

  function showSlide(index) {
    slides[currentSlide].classList.remove('active');
    currentSlide = (index + slides.length) % slides.length;
    slides[currentSlide].classList.add('active');
  }

  document.querySelector('.next').addEventListener('click', function() {
    showSlide(currentSlide + 1);
  });

  document.querySelector('.prev').addEventListener('click', function() {
    showSlide(currentSlide - 1);
  });
});
