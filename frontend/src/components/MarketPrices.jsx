import React from 'react';

const MarketPrices = () => {
  const prices = [
    { crop: 'Wheat (Gehu)', price: '₹2,200', unit: 'Quintal', trend: 'Up', change: '+₹50' },
    { crop: 'Rice (Chawal)', price: '₹2,800', unit: 'Quintal', trend: 'Stable', change: '₹0' },
    { crop: 'Corn (Makka)', price: '₹1,900', unit: 'Quintal', trend: 'Down', change: '-₹30' },
    { crop: 'Sugarcane (Ganna)', price: '₹315', unit: 'Quintal', trend: 'Up', change: '+₹10' },
    { crop: 'Soybean', price: '₹4,600', unit: 'Quintal', trend: 'Stable', change: '₹0' },
  ];

  return (
    <div>
      <h2 className="page-title">Live Mandi Prices</h2>
      
      <div className="card">
        <p style={{ marginBottom: '20px', color: '#555' }}>
          Today's real-time market rates for major crops. Data is updated daily.
        </p>

        <table className="styled-table">
          <thead>
            <tr>
              <th>Crop Name</th>
              <th>Price (INR)</th>
              <th>Unit</th>
              <th>Trend</th>
              <th>24h Change</th>
            </tr>
          </thead>
          <tbody>
            {prices.map((p, index) => (
              <tr key={index}>
                <td style={{ fontWeight: '500' }}>{p.crop}</td>
                <td><strong>{p.price}</strong></td>
                <td style={{ color: '#7f8c8d' }}>{p.unit}</td>
                <td style={{ 
                  color: p.trend === 'Up' ? '#2e7d32' : (p.trend === 'Down' ? '#d32f2f' : '#7f8c8d'),
                  fontWeight: 'bold'
                }}>
                  {p.trend === 'Up' ? '▲ ' : (p.trend === 'Down' ? '▼ ' : '▬ ')} 
                  {p.trend}
                </td>
                <td style={{ color: p.trend === 'Up' ? '#2e7d32' : (p.trend === 'Down' ? '#d32f2f' : '#7f8c8d') }}>
                  {p.change}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default MarketPrices;
