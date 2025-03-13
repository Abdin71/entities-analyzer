document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('analysis-form');
    const submitButton = form.querySelector('button[type="submit"]');
    const submitText = document.getElementById('submit-text');
    const loadingSpinner = document.getElementById('loading-spinner');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        // Show loading spinner and disable submit button
        submitText.style.display = 'none';
        loadingSpinner.style.display = 'inline-block';
        submitButton.disabled = true;

        try {
            // Submit the form data using Fetch API
            const formData = new FormData(form);
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                // Redirect to the results page
                window.location.href = response.url;
            } else {
                // Display error message
                const data = await response.json();
                errorMessage.textContent = data.error || 'An error occurred. Please try again.';
                errorMessage.style.display = 'block';
            }
        } catch (error) {
            // Display error message
            errorMessage.textContent = 'An error occurred. Please try again.';
            errorMessage.style.display = 'block';
        } finally {
            // Hide loading spinner and enable submit button
            submitText.style.display = 'inline-block';
            loadingSpinner.style.display = 'none';
            submitButton.disabled = false;
        }
    });
});