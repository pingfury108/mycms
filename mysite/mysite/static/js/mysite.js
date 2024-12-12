function createCarousel(carousel) {
  const carouselContainer = carousel
  const carouselItems = carouselContainer.querySelectorAll('.carousel-item');
  let currentIndex = 0;
  const itemWidth = carouselItems[0].offsetWidth;

  function scrollToIndex(index) {
    carouselContainer.scrollTo({
      left: index * itemWidth,
      behavior: 'smooth'
    });
  }

  function autoScroll() {
    currentIndex = (currentIndex + 1) % carouselItems.length;
    scrollToIndex(currentIndex);
  }

  setInterval(autoScroll, 3000);

  //carouselContainer.addEventListener('mouseover', () => clearInterval(autoScroll));
  //carouselContainer.addEventListener('mouseout', () => setInterval(autoScroll, 3000));
}

const elements = document.querySelectorAll('.carousel');

elements.forEach(element => {
  createCarousel(element);
});
