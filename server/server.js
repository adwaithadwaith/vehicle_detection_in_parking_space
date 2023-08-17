const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors'); // Import the cors module

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(cors()); // Enable CORS for all routes

// Rest of your code...


app.post('/save-coordinates', (req, res) => {
  const coordinates = req.body;
  const filePath = path.join(__dirname, 'uploads', 'coordinates.json');

  fs.writeFile(filePath, JSON.stringify(coordinates, null, 2), (err) => {
    if (err) {
      console.error('Error saving coordinates:', err);
      res.sendStatus(500);
    } else {
      console.log('Coordinates saved successfully.');
      res.sendStatus(200);
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});
