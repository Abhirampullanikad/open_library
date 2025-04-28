document.addEventListener('DOMContentLoaded', function() {
    const booksRow = document.getElementById('booksRow');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const bookCols = document.querySelectorAll('.book-col');
    const totalBooks = bookCols.length;
    const booksPerPage = 6;
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