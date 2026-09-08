const express = require('express');
const router = express.Router();

// Mock User Registration Route
router.post('/register', (req, res) => {
  const { name, email, password } = req.body;
  // TODO: Add logic to save user to DB
  res.json({ message: 'User registered successfully (Mock)', user: { name, email } });
});

// Mock User Login Route
router.post('/login', (req, res) => {
  const { email, password } = req.body;
  // TODO: Add authentication logic
  res.json({ message: 'User logged in successfully (Mock)', token: 'fake-jwt-token' });
});

module.exports = router;
