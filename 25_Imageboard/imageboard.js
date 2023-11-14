document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('post-form');
    const inputTitle = document.getElementById('post-title');
    const inputImage = document.getElementById('post-image');
    const postContainer = document.getElementById('post-container');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // Get input values
        const title = inputTitle.value;
        const image = inputImage.value;

        // Validate inputs
        if (!title || !image) {
            alert('Please fill out both title and image URL');
            return;
        }

        // Create post element
        const post = document.createElement('div');
        post.className = 'post';

        // Create post content
        const postContent = `
            <h2>${title}</h2>
            <img src="${image}" alt="${title}">
        `;

        post.innerHTML = postContent;

        // Append post to the container
        postContainer.appendChild(post);

        // Clear the form inputs
        inputTitle.value = '';
        inputImage.value = '';
    });
});
