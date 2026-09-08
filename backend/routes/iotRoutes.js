const express = require('express');
const router = express.Router();
const SensorData = require('../models/SensorData');

// Route for Hardware IoT device to post data
router.post('/data', async (req, res) => {
  try {
    const { deviceId, moisture, temperature } = req.body;
    
    // In a real app, you'd validate the deviceId here.
    const newReading = new SensorData({
      deviceId: deviceId || 'sensor-1',
      moisture,
      temperature
    });

    await newReading.save();
    console.log('Received IoT Data:', req.body);
    res.status(201).json({ message: 'Data saved successfully', data: newReading });
  } catch (error) {
    console.error('Error saving IoT data:', error);
    res.status(500).json({ error: 'Failed to save sensor data' });
  }
});

// Route for Frontend to fetch latest data
router.get('/data/latest', async (req, res) => {
  try {
    const latestData = await SensorData.find().sort({ timestamp: -1 }).limit(20);
    res.json(latestData);
  } catch (error) {
    console.error('Error fetching IoT data:', error);
    res.status(500).json({ error: 'Failed to fetch sensor data' });
  }
});

module.exports = router;
