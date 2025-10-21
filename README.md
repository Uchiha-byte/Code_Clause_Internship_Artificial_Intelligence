

# Code Clause Internship - Artificial Intelligence Projects 🚀

Welcome to the **Code Clause Internship Artificial Intelligence** repository! This collection showcases three innovative AI/ML projects developed during the internship program, demonstrating practical applications of machine learning, computer vision, and natural language processing.

## 📁 Project Overview

This repository contains three distinct AI projects, each showcasing different aspects of artificial intelligence and machine learning:

### 🎯 [Handwritten Digits Recognition](./Handwritten%20Digits%20Recognition/)
**Computer Vision & Neural Networks**
- **Technology**: TensorFlow, OpenCV, MNIST Dataset
- **Purpose**: Real-time handwritten digit recognition using neural networks
- **Features**: Custom image processing, pre-trained model, visualization
- **Files**: `handwritten_digits_recognition.py`, `handwritten_digits.model`, sample digit images

### 📊 [Sentiment Analysis](./Sentiment%20Analysis/)
**Natural Language Processing**
- **Technology**: TextBlob, NLTK, Transformers (RoBERTa), VADER
- **Purpose**: Multi-model sentiment analysis comparing different approaches
- **Features**: TextBlob analysis, VADER sentiment scoring, RoBERTa transformer model
- **Files**: `Sentiment Analysis.py`, `sentiment-analysis-python.ipynb`, `Reviews.csv`

### 🎮 [Virtual Controller](./Virtual%20Controller/)
**Computer Vision & Human-Computer Interaction**
- **Technology**: OpenCV, MediaPipe, Streamlit, PyAutoGUI
- **Purpose**: Hand gesture-based virtual controllers for gaming
- **Features**: Virtual steering wheel, virtual gun controller, real-time hand tracking
- **Files**: `main.py`, `steering.py`, `shooter.py`, `keyinput.py`, `util.py`

## 🛠️ Technology Stack

| Project | Primary Technologies | Libraries |
|---------|---------------------|-----------|
| **Handwritten Digits** | TensorFlow, OpenCV | `tensorflow-cpu`, `opencv-python`, `numpy`, `matplotlib` |
| **Sentiment Analysis** | TextBlob, NLTK, Transformers | `textblob`, `nltk`, `transformers`, `pandas`, `scipy` |
| **Virtual Controller** | OpenCV, MediaPipe, Streamlit | `opencv-python`, `mediapipe`, `streamlit`, `pyautogui`, `pynput` |

## 🚀 Quick Start

### Prerequisites
- **Python 3.7+** (3.9-3.11 recommended for Virtual Controller)
- **Webcam** (required for Virtual Controller)
- **Virtual Environment** (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <https://github.com/Uchiha-byte/Code_Clause_Internship_Artificial_Intelligence.git>
   cd "Code Clause Internship -Artificial_Intelligence"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies for specific projects**
   ```bash
   # For Handwritten Digits Recognition
   cd "Handwritten Digits Recognition"
   pip install -r requirements.txt
   
   # For Sentiment Analysis
   cd "../Sentiment Analysis"
   pip install textblob nltk transformers pandas scipy matplotlib seaborn
   
   # For Virtual Controller
   cd "../Virtual Controller"
   pip install streamlit opencv-python mediapipe pyautogui pynput numpy
   ```

## 📋 Project Details

### 1. Handwritten Digits Recognition
- **Model Architecture**: 3-layer neural network (Flatten → Dense(128) → Dense(128) → Dense(10))
- **Dataset**: MNIST (70,000 handwritten digit images)
- **Accuracy**: ~98% on test set
- **Usage**: Place digit images in `digits/` folder and run the script
- **Customization**: Modify `train_new_model` flag to retrain or use existing model

### 2. Sentiment Analysis
- **Approaches**: 
  - TextBlob polarity scoring
  - VADER sentiment analysis
  - RoBERTa transformer model
- **Dataset**: Amazon product reviews (500 samples)
- **Features**: Comparative analysis between different sentiment models
- **Output**: Sentiment scores (positive/negative/neutral) with confidence levels

### 3. Virtual Controller
- **Controllers**:
  - **Steering Wheel**: Hand gesture-based steering for racing games
  - **Gun Controller**: Finger tracking for aiming and shooting
- **Gestures**:
  - Left/Right steering based on hand position
  - Click detection (thumb-to-index finger distance)
  - Right click, double click, and screenshot gestures
- **Interface**: Streamlit web application with real-time camera feed

## 🎯 Key Features

### Handwritten Digits Recognition
- ✅ Neural network implementation from scratch
- ✅ Real-time image processing
- ✅ Custom digit image support
- ✅ Model persistence and loading
- ✅ Visual prediction display

### Sentiment Analysis
- ✅ Multiple sentiment analysis approaches
- ✅ Comparative model evaluation
- ✅ Jupyter notebook with detailed analysis
- ✅ Real-time sentiment scoring
- ✅ Visualization of sentiment distributions

### Virtual Controller
- ✅ Real-time hand tracking
- ✅ Multiple controller modes
- ✅ Gesture recognition
- ✅ Web-based interface
- ✅ Cross-platform compatibility

## 📊 Performance Metrics

| Project | Metric | Value |
|---------|--------|-------|
| **Handwritten Digits** | Test Accuracy | ~98% |
| **Sentiment Analysis** | Model Comparison | VADER vs RoBERTa |
| **Virtual Controller** | Tracking FPS | 30+ FPS |
| **Virtual Controller** | Detection Confidence | 70%+ |

## 🔧 Configuration

### Handwritten Digits Recognition
- Modify `train_new_model` in `handwritten_digits_recognition.py`
- Adjust image size requirements (28x28 pixels)
- Customize neural network architecture

### Sentiment Analysis
- Update sample sentences in `Sentiment Analysis.py`
- Modify dataset path in Jupyter notebook
- Adjust confidence thresholds

### Virtual Controller
- Configure hand detection confidence in `steering.py` and `shooter.py`
- Adjust gesture sensitivity parameters
- Customize key mappings in `keyinput.py`

## 🚨 Troubleshooting

### Common Issues

1. **TensorFlow Installation**
   ```bash
   # If TensorFlow fails to install
   pip install tensorflow-cpu==2.7.0
   ```

2. **Camera Access**
   - Ensure webcam permissions are granted
   - Check camera availability: `cv2.VideoCapture(0)`

3. **Dependencies**
   - Use virtual environment to avoid conflicts
   - Install packages individually if bulk installation fails

## 📚 Learning Outcomes

This project collection demonstrates:

- **Machine Learning**: Neural network implementation and training
- **Computer Vision**: Image processing and hand tracking
- **Natural Language Processing**: Sentiment analysis techniques
- **Human-Computer Interaction**: Gesture-based control systems
- **Web Development**: Streamlit application development
- **Data Analysis**: Comparative model evaluation

## 👥 Contributors

- **Developer**: Ans Ahmed Khan
- **Institution**: Code Clause Internship Program
- **Technologies**: OpenCV, MediaPipe, TensorFlow, Streamlit teams

## 📄 License

This project is part of the Code Clause Internship Program. Please refer to individual project READMEs for specific licensing information.

## 🔗 Related Resources

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [OpenCV Documentation](https://opencv.org/)
- [MediaPipe Documentation](https://mediapipe.dev/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [TextBlob Documentation](https://textblob.readthedocs.io/)

---

**Note**: This repository contains educational projects developed during the Code Clause Internship program. Each project demonstrates different aspects of artificial intelligence and machine learning applications.
