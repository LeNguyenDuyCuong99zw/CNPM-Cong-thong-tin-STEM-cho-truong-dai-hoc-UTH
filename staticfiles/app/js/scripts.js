document.addEventListener('DOMContentLoaded', function() {
  const carouselInner = document.querySelector('.carousel-inner');
  const carouselItems = document.querySelectorAll('.carousel-item');
  const prevButton = document.querySelector('.carousel-control-prev');
  const nextButton = document.querySelector('.carousel-control-next');
  const indicators = document.querySelectorAll('.carousel-indicators button');
  let currentIndex = 0;
  const totalItems = carouselItems.length;
  const slideInterval = 5500;

  function showSlide(index) {
      const offset = -index * 100;
      carouselInner.style.transform = `translateX(${offset}%)`;
      indicators.forEach((indicator, i) => {
          indicator.classList.toggle('active', i === index);
      });
  }

  function showNextSlide() {
      currentIndex = (currentIndex + 1) % totalItems;
      showSlide(currentIndex);
      setTimeout(showNextSlide, slideInterval); 
  }

  function showPrevSlide() {
      currentIndex = (currentIndex - 1 + totalItems) % totalItems;
      showSlide(currentIndex);
  }

  prevButton.addEventListener('click', showPrevSlide);
  nextButton.addEventListener('click', showNextSlide);

  indicators.forEach((indicator, index) => {
      indicator.addEventListener('click', () => {
          currentIndex = index;
          showSlide(currentIndex);
      });
  });

  setTimeout(showNextSlide, slideInterval); 
});
function toggleMenu() {
    var navMenu = document.getElementById("navMenu");
    if (navMenu.style.display === "block") {
        navMenu.style.display = "none";
    } else {
        navMenu.style.display = "block";
    }
}
function checkResize() {
    var navMenu = document.getElementById("navMenu");
    if (window.innerWidth > 1200) {
        navMenu.style.display = "flex"; // Ensure the menu is displayed properly on larger screens
    } else {
        navMenu.style.display = "none"; // Hide the menu for smaller screens initially
    }
}
window.onload = checkResize;
window.onresize = checkResize;