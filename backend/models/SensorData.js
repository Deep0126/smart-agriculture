const mongoose = require('mongoose');

const SensorDataSchema = new mongoose.Schema({
  deviceId: {
    type: String,
    required: true,
  },
  moisture: {
    type: Number,
    required: true,
  },
  temperature: {
    type: Number,
    // optional depending on sensor, but good to have
  },
  timestamp: {
    type: Date,
    default: Date.now,
  },
});

module.exports = mongoose.model('SensorData', SensorDataSchema);
