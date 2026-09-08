import React, { useState } from 'react';
import Dashboard from './components/Dashboard';
import CropPredictor from './components/CropPredictor';
import DiseaseDetector from './components/DiseaseDetector';
import MarketPrices from './components/MarketPrices';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('dashboard');

  return (
    <div className="app-container">
      {/* Sidebar */}
      <div className="sidebar">
        <h2>🌱 Smart Agri</h2>
        <ul className="nav-list">
          <li className={`nav-item ${activeTab === 'dashboard' ? 'active' : ''}`} onClick={() => setActiveTab('dashboard')}>
            📊 Dashboard
          </li>
          <li className={`nav-item ${activeTab === 'crop' ? 'active' : ''}`} onClick={() => setActiveTab('crop')}>
            🌾 Crop Recommendation
          </li>
          <li className={`nav-item ${activeTab === 'disease' ? 'active' : ''}`} onClick={() => setActiveTab('disease')}>
            🍂 Disease Detection
          </li>
          <li className={`nav-item ${activeTab === 'market' ? 'active' : ''}`} onClick={() => setActiveTab('market')}>
            💰 Mandi Prices
          </li>
        </ul>
      </div>

      {/* Main Content */}
      <div className="main-content">
        {activeTab === 'dashboard' && <Dashboard />}
        {activeTab === 'crop' && <CropPredictor />}
        {activeTab === 'disease' && <DiseaseDetector />}
        {activeTab === 'market' && <MarketPrices />}
      </div>
    </div>
  );
}

export default App;
