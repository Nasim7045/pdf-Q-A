document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('pdf-form');
    const pdfTextElement = document.getElementById('pdf-text');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const fileInput = document.getElementById('pdf-file');
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);

        try {
            const response = await fetch('http://127.0.0.1:8000/upload_pdf', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            if (data.message) {
                pdfTextElement.textContent = `File uploaded: ${data.message}`;
            }
            if (data.user_id) {
                pdfTextElement.textContent += `\nUser ID: ${data.user_id}`;
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
