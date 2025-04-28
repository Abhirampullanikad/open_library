document.addEventListener('DOMContentLoaded', function() {
    const booksRow = document.getElementById('booksRow');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const bookCols = document.querySelectorAll('.book-col');
    const totalBooks = bookCols.length;
    const booksPerPage = 4;
    let currentPosition = 0;
    const maxPosition = (totalBooks - booksPerPage) * bookCols[0].offsetWidth;
    
    // Initialize buttons
    updateButtons();
    
    nextBtn.addEventListener('click', function() {
        currentPosition += bookCols[0].offsetWidth * booksPerPage;
        if (currentPosition > maxPosition) {
            currentPosition = maxPosition;
        }
        booksRow.style.transform = `translateX(-${currentPosition}px)`;
        updateButtons();
    });
    
    prevBtn.addEventListener('click', function() {
        currentPosition -= bookCols[0].offsetWidth * booksPerPage;
        if (currentPosition < 0) {
            currentPosition = 0;
        }
        booksRow.style.transform = `translateX(-${currentPosition}px)`;
        updateButtons();
    });
    
    function updateButtons() {
        prevBtn.classList.toggle('disabled', currentPosition === 0);
        nextBtn.classList.toggle('disabled', currentPosition >= maxPosition);
    }
    
    // Handle window resize
    window.addEventListener('resize', function() {
        const newColWidth = bookCols[0].offsetWidth;
        const newMaxPosition = (totalBooks - booksPerPage) * newColWidth;
        
        // Adjust current position proportionally
        currentPosition = (currentPosition / bookCols[0].offsetWidth) * newColWidth;
        if (currentPosition > newMaxPosition) {
            currentPosition = newMaxPosition;
        }
        
        booksRow.style.transform = `translateX(-${currentPosition}px)`;
        updateButtons();
    });
  });
  
  
  
  
  document.addEventListener('DOMContentLoaded', function() {
      const slideshow = document.querySelector('.auto-slideshow');
      const slides = document.querySelector('.slides');
      const images = document.querySelectorAll('.slides img');
      const indicators = document.querySelector('.indicators');
      
      let currentIndex = 0;
      const slideCount = images.length;
      const slideWidth = images[0].clientWidth;
      
      // Create indicators if they exist
      if (indicators) {
        for (let i = 0; i < slideCount; i++) {
          const indicator = document.createElement('span');
          indicator.addEventListener('click', () => goToSlide(i));
          indicators.appendChild(indicator);
        }
        updateIndicators();
      }
      
      // Set up auto-rotation
      let interval = setInterval(nextSlide, 4000);
      
      function nextSlide() {
        currentIndex = (currentIndex + 1) % slideCount;
        updateSlide();
      }
      
      function updateSlide() {
        slides.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
        if (indicators) updateIndicators();
      }
      
      function goToSlide(index) {
        currentIndex = index;
        updateSlide();
        resetInterval();
      }
      
      function updateIndicators() {
        document.querySelectorAll('.indicators span').forEach((ind, i) => {
          ind.classList.toggle('active', i === currentIndex);
        });
      }
      
      function resetInterval() {
        clearInterval(interval);
        interval = setInterval(nextSlide, 4000);
      }
      
      // Pause on hover
      slideshow.addEventListener('mouseenter', () => clearInterval(interval));
      slideshow.addEventListener('mouseleave', resetInterval);
      
      // Handle window resize
      window.addEventListener('resize', () => {
        slides.style.transition = 'none';
        slides.style.transform = `translateX(-${currentIndex * images[0].clientWidth}px)`;
        setTimeout(() => slides.style.transition = 'transform 0.8s ease-in-out');
      });
    });