const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Basic Route
app.get('/', (req, res) => {
  res.send('Smart Agriculture API is running...');
});

// Import Routes
const userRoutes = require('./routes/userRoutes');
const iotRoutes = require('./routes/iotRoutes');

// Use Routes
app.use('/api/users', userRoutes);
app.use('/api/iot', iotRoutes);

// MongoDB Connection
const PORT = process.env.PORT || 5000;
const MONGO_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/smart-agriculture';

mongoose.connect(MONGO_URI)
  .then(() => {
    console.log('Connected to MongoDB');
  })
  .catch((err) => {
    console.log('MongoDB connection error (Offline mode):', err.message);
  });

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
