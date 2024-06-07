let slideIndex = 1;

async function fetchImages() {
    const urlInput = document.getElementById('url-input').value.trim();
    if (!urlInput) {
        alert('Please enter a valid URL.');
        return;
    }

    const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
    const targetUrl = proxyUrl + urlInput;

    try {
        const response = await fetch(targetUrl, { method: 'GET' });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const images = await response.json();
        if (!Array.isArray(images) || images.length === 0) {
            throw new Error('No images found or data is not an array.');
        }

        createSlideshow(images);
    } catch (error) {
        console.error('Error fetching images:', error);
        alert(`Error fetching images: ${error.message}`);
    }
}

function createSlideshow(images) {
    const slideshowContainer = document.getElementById('slideshow-container');
    const dotsContainer = document.getElementById('dots-container');

    // Clear existing slides and dots
    slideshowContainer.innerHTML = '';
    dotsContainer.innerHTML = '';

    images.forEach((image, index) => {
        // Create slide
        const slideDiv = document.createElement('div');
        slideDiv.className = 'mySlides fade';
        const img = document.createElement('img');
        img.src = image.url;
        img.alt = image.description || `Image ${index + 1}`;
        slideDiv.appendChild(img);
        slideshowContainer.appendChild(slideDiv);

        // Create dot
        const dot = document.createElement('span');
        dot.className = 'dot';
        dot.onclick = () => currentSlide(index + 1);
        dotsContainer.appendChild(dot);
    });

    // Create navigation buttons
    const prevButton = document.createElement('a');
    prevButton.className = 'prev';
    prevButton.innerHTML = '&#10094;';
    prevButton.onclick = () => plusSlides(-1);
    slideshowContainer.appendChild(prevButton);

    const nextButton = document.createElement('a');
    nextButton.className = 'next';
    nextButton.innerHTML = '&#10095;';
    nextButton.onclick = () => plusSlides(1);
    slideshowContainer.appendChild(nextButton);

    showSlides(slideIndex);
}

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    const slides = document.getElementsByClassName('mySlides');
    const dots = document.getElementsByClassName('dot');
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = 'none';
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(' active', '');
    }
    slides[slideIndex - 1].style.display = 'block';
    dots[slideIndex - 1].className += ' active';
}
