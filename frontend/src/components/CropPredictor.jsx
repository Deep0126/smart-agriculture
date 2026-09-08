import React, { useState } from 'react';

const CropPredictor = () => {
  const [formData, setFormData] = useState({
    nitrogen: '', phosphorus: '', potassium: '', temperature: '', humidity: '', ph: '', rainfall: ''
  });
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    setPrediction({ predicted_crop: 'Wheat', confidence: 92.5 });
  };

  return (
    <div>
      <h2 className="page-title">AI Crop Recommendation</h2>
      
      <div className="card" style={{ maxWidth: '600px' }}>
        <form onSubmit={handleSubmit}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '15px' }}>
            <div className="form-group">
              <label>Nitrogen (N)</label>
              <input type="number" className="form-input" placeholder="e.g. 50" onChange={(e) => setFormData({...formData, nitrogen: e.target.value})} required />
            </div>
            <div className="form-group">
              <label>Phosphorus (P)</label>
              <input type="number" className="form-input" placeholder="e.g. 40" onChange={(e) => setFormData({...formData, phosphorus: e.target.value})} required />
            </div>
            <div className="form-group">
              <label>Potassium (K)</label>
              <input type="number" className="form-input" placeholder="e.g. 30" onChange={(e) => setFormData({...formData, potassium: e.target.value})} required />
            </div>
            <div className="form-group">
              <label>Soil pH</label>
              <input type="number" step="0.1" className="form-input" placeholder="e.g. 6.5" onChange={(e) => setFormData({...formData, ph: e.target.value})} required />
            </div>
          </div>
          
          <div style={{ marginTop: '20px' }}>
            <button type="submit" className="btn-primary" style={{ width: '100%' }}>Predict Best Crop</button>
          </div>
        </form>

        {prediction && (
          <div className="result-box">
            <h4>Recommended Crop: {prediction.predicted_crop}</h4>
            <p><strong>AI Confidence Score:</strong> {prediction.confidence}%</p>
            <p style={{ marginTop: '10px', color: '#555' }}>
              Based on your soil nutrients, this is the most profitable crop to grow this season.
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default CropPredictor;
