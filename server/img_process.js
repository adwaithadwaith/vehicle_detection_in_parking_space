const express = require('express');
const multer = require('multer');
const { spawn } = require('child_process');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.post('/upload', upload.single('image'), (req, res) => {
    const imagePath = req.file.path;
    const coordinatesPath = 'server/uploads/coordinates.json';
    console.log('hello')
    
    // Spawn a Python process and pass the image and coordinates file paths as arguments
    const pythonProcess = spawn('python', ['server/python/detector.py', imagePath, coordinatesPath]);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`Python script output: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python script error: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python script exited with code ${code}`);
    });

    res.sendStatus(200);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
