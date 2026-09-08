import React, { useState, useEffect } from 'react';

const Dashboard = () => {
  const [sensorData, setSensorData] = useState([]);

  useEffect(() => {
    // Mock Data
    setSensorData([
      { moisture: 45, temperature: 28, timestamp: new Date().toISOString() }
    ]);
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
