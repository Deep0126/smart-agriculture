import React, { useState, useEffect } from 'react';

const Dashboard = () => {
  const [sensorData, setSensorData] = useState([]);

  useEffect(() => {
    // Fetch live IoT data from Render Backend
    fetch('https://smart-agriculture-tdbe.onrender.com/api/iot/data/latest')
      .then(res => res.json())
      .then(data => {
        if (data && data.length > 0) {
          setSensorData(data);
        } else {
          // Fallback dummy data if Database is empty
          setSensorData([{ moisture: 45, temperature: 28, timestamp: new Date().toISOString() }]);
        }
      })
      .catch(err => console.log('Error fetching data:', err));
  }, []);

  return (
    <div>
      <h2 className="page-title">Farmer Dashboard</h2>
      
      <div className="dashboard-grid">
        <div className="card">
          <h3>💧 Live Soil Moisture</h3>
          <p className="value-green">
            {sensorData.length > 0 ? `${sensorData[0].moisture}%` : 'Loading...'}
          </p>
          <p style={{ color: '#7f8c8d' }}>Status: Sensor Active</p>
        </div>

        <div className="card">
          <h3>🌡️ Temperature</h3>
          <p className="value-red">
            {sensorData.length > 0 ? `${sensorData[0].temperature}°C` : 'Loading...'}
          </p>
          <p style={{ color: '#7f8c8d' }}>Status: Normal</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
