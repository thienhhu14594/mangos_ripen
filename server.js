const express = require('express');
const multer = require('multer');
const path = require('path');
const { spawn } = require('child_process');
const fs = require('fs');
const network = require('network');

const app = express();
const port = 3000;

const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/upload', upload.single('image'), (req, res) => {
  // Save the uploaded image (you might want to save it to a file)
  const imageBuffer = req.file.buffer;

  const filePath = '_temp.png'; // Update the file path and extension accordingly

  // Write the image buffer to the file
  fs.writeFile(filePath, imageBuffer, (err) => {
    if (err) {
      console.error('Error saving image:', err);
      res.status(500).json({ error: 'Error saving image' });
      return;
    }

    console.log('Image saved successfully:', filePath);

    // Spawn a Python process
    const pythonProcess = spawn('python', ['predict.py'], { stdio: ['pipe', 'pipe', 'pipe'] });

    // Pass the image data to the Python script through stdin
    pythonProcess.stdin.write(imageBuffer);
    pythonProcess.stdin.end();

    let result = '';

    // Capture the result from the Python script
    pythonProcess.stdout.on('data', (data) => {
      result += data.toString();

      // Get the result only
      result = result.slice(result.lastIndexOf("Result"))
    });

    // Handle the end of the Python script execution
    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        console.error(`Python script process exited with code ${code}`);
        res.status(500).json({ error: 'Error processing image' });
      } else {
        // Process the result from the Python script

        // Send the result and image path as a response to the client
        res.json({ result, imagePath: filePath });
      }
    });
  });
});

// Dynamically get the IPv4 address
network.get_private_ip((err, IPv4) => {
  if (err) {
    console.error('Error getting IPv4 address:', err);
    return;
  }

  console.log(`Server is running at http://${IPv4}:${port}`);
  app.listen(port, IPv4);
});
