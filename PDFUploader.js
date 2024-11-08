import React, { useState } from 'react';
import { uploadPDF } from './api';

function PDFUploader() {
    const [file, setFile] = useState(null);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        if (file) {
            await uploadPDF(file);
            alert('File uploaded successfully');
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload PDF</button>
        </div>
    );
}

export default PDFUploader;
