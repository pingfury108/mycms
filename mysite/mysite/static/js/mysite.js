function createCarousel(carousel) {
  const $carousel = $(carousel);
  const $items = $carousel.find('.carousel-item');
  let currentIndex = 0;
  const itemWidth = $items.first().width();

  function scrollToIndex(index) {
    $carousel.animate({
      scrollLeft: index * itemWidth
    }, 'slow');
  }

  function autoScroll() {
    currentIndex = (currentIndex + 1) % $items.length;
    scrollToIndex(currentIndex);
  }

  const autoScrollInterval = setInterval(autoScroll, 3000);

  // 箭头控制
  const $leftArrow = $('.left-arrow');
  const $rightArrow = $('.right-arrow');

  $leftArrow.on('click', () => {
    currentIndex = (currentIndex - 1 + $items.length) % $items.length;
    scrollToIndex(currentIndex);
  });

  $rightArrow.on('click', () => {
    currentIndex = (currentIndex + 1) % $items.length;
    scrollToIndex(currentIndex);
  });

  // 鼠标悬停时暂停自动滚动
  $carousel.hover(
    () => clearInterval(autoScrollInterval),
    () => setInterval(autoScroll, 3000)
  );
}

// 初始化所有轮播图
$('.carousel').each(function() {
  createCarousel(this);
});


$('.dropdown').on({
  mouseenter: function() {
    $(this).find('.dropdown-content')
           .removeClass('translate-y-full opacity-0');
  },
  mouseleave: function() {
    $(this).find('.dropdown-content')
           .addClass('translate-y-full opacity-0');
  }
});


$(document).ready(function() {
  $('.font-number').each(function() {
    const $element = $(this);
    const targetNumber = Number($element.text().replace("+", ""));
    let currentNumber = 0;
    
    const interval = setInterval(() => {
      if (currentNumber < targetNumber) {
        currentNumber++;
        $element.text(currentNumber + '+');
      } else {
        clearInterval(interval);
      }
    }, 10);
  });
});
