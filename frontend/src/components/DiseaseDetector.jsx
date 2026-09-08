import React, { useState } from 'react';

const DiseaseDetector = () => {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState(null);

  const handleImageUpload = (e) => {
    setImage(URL.createObjectURL(e.target.files[0]));
    setResult(null); // reset previous result
  };

  const handleDetect = () => {
    setResult({ disease: 'Leaf Blight', treatment: 'Use appropriate fungicide and ensure proper drainage in the field.' });
  };

  return (
    <div>
      <h2 className="page-title">Plant Disease Detection</h2>
      
      <div className="card" style={{ maxWidth: '600px' }}>
        <p style={{ marginBottom: '20px', color: '#555' }}>
          Upload a clear picture of a diseased plant leaf. Our AI model will analyze the image and suggest treatments.
        </p>
        
        <div className="file-upload-wrapper">
          <input type="file" id="file-upload" accept="image/*" onChange={handleImageUpload} style={{ display: 'none' }} />
          <label htmlFor="file-upload" className="btn-primary" style={{ display: 'inline-block' }}>
            Choose Image
          </label>
        </div>
        
        {image && (
          <div style={{ textAlign: 'center', marginTop: '20px' }}>
            <img src={image} alt="Uploaded Leaf" style={{ maxWidth: '100%', maxHeight: '300px', borderRadius: '8px', boxShadow: '0 4px 10px rgba(0,0,0,0.1)' }} />
            <br /><br />
            <button onClick={handleDetect} className="btn-primary" style={{ background: '#2196f3' }}>
              🔍 Analyze Disease
            </button>
          </div>
        )}

        {result && (
          <div className="result-box" style={{ borderLeftColor: '#2196f3', backgroundColor: '#e3f2fd' }}>
            <h4 style={{ color: '#1976d2' }}>Detected: {result.disease}</h4>
            <p style={{ marginTop: '10px' }}><strong>Recommended Treatment:</strong> {result.treatment}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default DiseaseDetector;
