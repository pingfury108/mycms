
const carousel = document.querySelector('.carousel');
const carouselItems = document.querySelectorAll('.carousel-item');
let currentIndex = 0;

function scrollToItem(index) {
  const itemWidth = carouselItems[0].offsetWidth; // 获取单个item的宽度
  carousel.scrollTo({
    left: index * itemWidth,
    behavior: 'smooth' // 可选：平滑滚动
  });
}

function autoScroll() {
  currentIndex = (currentIndex + 1) % carouselItems.length;
  scrollToItem(currentIndex);
}

setInterval(autoScroll, 3000); // 每3秒滚动一次

/*
// 可选：添加事件监听器，在鼠标悬停时暂停自动滚动
carousel.addEventListener('mouseover', () => {
  clearInterval(autoScroll);
});

carousel.addEventListener('mouseout', () => {
  setInterval(autoScroll, 3000);
});

 */
