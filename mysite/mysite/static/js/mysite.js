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

  // 添加左右箭头控制
  const leftArrow = document.querySelector('.left-arrow');
  const rightArrow = document.querySelector('.right-arrow');

  if (leftArrow) {
    leftArrow.addEventListener('click', () => {
      currentIndex = (currentIndex - 1 + carouselItems.length) % carouselItems.length;
      scrollToIndex(currentIndex);
    });
  }

  if (rightArrow) {

    rightArrow.addEventListener('click', () => {
      currentIndex = (currentIndex + 1) % carouselItems.length;
      scrollToIndex(currentIndex);
    });
  }

  //carouselContainer.addEventListener('mouseover', () => clearInterval(autoScroll));
  //carouselContainer.addEventListener('mouseout', () => setInterval(autoScroll, 3000));
}

const elements = document.querySelectorAll('.carousel');

elements.forEach(element => {
  createCarousel(element);
});


document.querySelectorAll('.dropdown').forEach(dropdown => {
  dropdown.addEventListener('mouseenter', () => {
    const content = dropdown.querySelector('.dropdown-content');
    content.classList.remove('translate-y-full', 'opacity-0');
  });

  dropdown.addEventListener('mouseleave', () => {
    const content = dropdown.querySelector('.dropdown-content');
    content.classList.add('translate-y-full', 'opacity-0');
  });
});


document.addEventListener("DOMContentLoaded", function () {

  const displayElement = document.querySelectorAll('.font-number');

  if (displayElement) {
    displayElement.forEach(element => {

      const targetNumber = Number(element.textContent.replace("+", ""));
      let currentNumber = 0;

      const interval = setInterval(() => {
        if (currentNumber < targetNumber) {
          currentNumber++;
          element.textContent = currentNumber + '+';
        } else {
          clearInterval(interval);
        }
      }, 10);

    });
  }
});
