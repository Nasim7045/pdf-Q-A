import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const uploadPDF = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
        await axios.post(`${API_URL}/upload_pdf`, formData);
    } catch (error) {
        console.error('Error uploading file:', error);
    }
};
