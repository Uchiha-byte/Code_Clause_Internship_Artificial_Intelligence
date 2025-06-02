# Handwritten Digits Recognition

This project implements a neural network model to recognize handwritten digits using the MNIST dataset. The model is built using TensorFlow and can be trained from scratch or loaded from a pre-trained model.

## Features
- Neural network model for digit recognition
- Support for custom digit images
- Real-time prediction visualization
- Pre-trained model included

## Requirements
- Python 3.7+
- TensorFlow (CPU version)
- OpenCV (cv2)
- NumPy
- Matplotlib

## Installation
1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

If you encounter issues installing TensorFlow, try one of these alternatives:
```bash
# Option 1: Install CPU-only version
pip install tensorflow-cpu

# Option 2: Install specific version
pip install tensorflow==2.7.0

# Option 3: Install CPU-only specific version
pip install tensorflow-cpu==2.7.0
```

Then install the remaining requirements:
```bash
pip install opencv-python numpy matplotlib
```

## Usage
1. Place your handwritten digit images in the `digits` folder
   - Images should be 28x28 pixels in PNG format
   - Name them as `digit1.png`, `digit2.png`, etc.

2. Run the script:
```bash
python handwritten_digits_recognition.py
```

3. The script will:
   - Train a new model if `train_new_model = True`
   - Load the existing model if `train_new_model = False`
   - Process all images in the digits folder
   - Display predictions with visualizations

## Model Architecture
- Input Layer: Flattened 28x28 pixel images
- Hidden Layers: Two dense layers with 128 units each (ReLU activation)
- Output Layer: Dense layer with 10 units (Softmax activation)

## Notes
- The model is trained on the MNIST dataset
- Training takes approximately 3 epochs
- The pre-trained model is saved as 'handwritten_digits.model'
- Custom images should be black digits on white background
