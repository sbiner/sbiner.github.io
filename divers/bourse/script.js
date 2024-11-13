document.addEventListener('DOMContentLoaded', function() {
    const sidebarItems = document.querySelectorAll('.sidebar ul li');
    const thumbnailsContainer = document.querySelector('.thumbnail-container');
    const largeImage = document.getElementById('largeImage');

    sidebarItems.forEach(item => {
        item.addEventListener('click', function() {
            const directory = item.getAttribute('data-directory');
            const images = item.getAttribute('data-images').split(',');
            loadThumbnails(images, directory);
        });
    });

    function loadThumbnails(images, directory) {
        thumbnailsContainer.innerHTML = '';
        images.forEach(image => {
            const imgElement = document.createElement('img');
            imgElement.src = image;
            imgElement.alt = 'Thumbnail';
            imgElement.classList.add('thumbnail');

            imgElement.addEventListener('mouseenter', function() {
                largeImage.setAttribute('src', image);
            });

            thumbnailsContainer.appendChild(imgElement);
        });
    }
});
