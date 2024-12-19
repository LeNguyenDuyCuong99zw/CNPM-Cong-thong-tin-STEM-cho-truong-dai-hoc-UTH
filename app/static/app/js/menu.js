window.onscroll = function() {
    const nav = document.querySelector('.nav');
    const sticky = nav.offsetTop; 

    if (window.scrollY > sticky) {
        nav.classList.add('fixed'); 
    } else {
        nav.classList.remove('fixed'); 
    }
};

let currentSlide = 0;
const slides = document.querySelectorAll('.slide3_1');

function showSlide(index) {
    slides[currentSlide].classList.remove('active');
    currentSlide = (index + slides.length) % slides.length; // Wrap around
    slides[currentSlide].classList.add('active');
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

function prevSlide() {
    showSlide(currentSlide - 1);
}
setInterval(nextSlide, 5000);
