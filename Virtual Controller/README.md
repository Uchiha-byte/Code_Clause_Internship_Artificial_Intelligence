# Cam-X Controller 🎮

## Overview
The Cam-X Controller is an innovative virtual controller system that transforms your hand gestures into gaming controls using computer vision technology. By leveraging OpenCV and MediaPipe, this system creates an immersive gaming experience where your hands become virtual controllers - whether you need a steering wheel for racing games or a virtual gun for shooting games.

## Features
- **Virtual Steering Wheel** 🚗
  - Hand gesture-based steering control
  - Real-time hand tracking and movement detection
  - Intuitive steering mechanics
  - Compatible with most racing games

- **Virtual Gun Controller** 🎯
  - Precise aim tracking using hand gestures
  - Click detection for shooting
  - Multiple gesture controls (left click, right click, double click)
  - Screenshot capability

- **User Interface** 💻
  - Clean and modern Streamlit-based web interface
  - Easy navigation between different modes
  - Real-time visualization of hand tracking
  - User-friendly controls and settings

## Technologies Used
- **Python 3.9-3.11**
- **OpenCV** - For real-time video capture and processing
- **MediaPipe** - For advanced hand tracking and gesture recognition
- **Streamlit** - For the web-based user interface
- **PyAutoGUI** - For system-level input simulation
- **NumPy** - For numerical computations
- **ctypes** - For low-level system interactions

## Installation

### Prerequisites
- Python 3.9-3.11
- Webcam
- Windows/Linux/MacOS

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/uchiha_byte/cam-x-controller.git
   cd Virtual Controller
   ```

2. Install required packages:
   ```bash
   pip install streamlit opencv-python mediapipe pyautogui pynput numpy
   ```

3. Run the application:
   ```bash
   streamlit run main.py
   ```

## Project Structure
```
Virtual Controller/
├── main.py              # Main application entry point
├── steering.py          # Virtual steering wheel implementation
├── shooter.py           # Virtual gun controller implementation
├── keyinput.py         # Keyboard input simulation
├── util.py             # Utility functions
├── about.py            # About page implementation
├── developers.py       # Developers page implementation
└── .streamlit/         # Streamlit configuration
```

## Components

### 1. Main Application (`main.py`)
- Initializes the Streamlit application
- Manages page navigation and layout
- Handles user interface components
- Controls application flow

### 2. Virtual Steering Wheel (`steering.py`)
- Implements hand tracking for steering control
- Processes hand gestures and converts them to steering inputs
- Provides real-time visual feedback
- Handles steering calibration and sensitivity

### 3. Virtual Gun Controller (`shooter.py`)
- Implements precise aim tracking
- Handles different click gestures:
  - Left click: Thumb click gesture
  - Right click: Specific finger angle
  - Double click: Combined finger gestures
- Includes screenshot functionality

### 4. Key Input Simulation (`keyinput.py`)
Classes and structures for input simulation:
- `KeyBdInput`: Keyboard input event representation
- `HardwareInput`: Hardware event simulation
- `MouseInput`: Mouse event handling
- `Input_I`: Input event union
- `Input`: Main input event structure

## Usage Guide

### Virtual Steering Wheel
1. Click "Start Virtual Wheel" in the main interface
2. Position your hand in front of the camera
3. Make a steering wheel gesture
4. Turn your hand left/right to control steering
5. Use predefined gestures for acceleration/braking

### Virtual Gun Controller
1. Select "Start Virtual Gun" from the main menu
2. Use your hand to aim (index finger recommended)
3. Perform click gestures:
   - Close thumb for left click
   - Specific finger positions for right/double click
4. Use special gestures for screenshots

## Contributing
We welcome contributions! Please feel free to submit pull requests, create issues or fork the repository.

## Credits
- **Developer**: Ans Ahmed Khan
- **Project Guide**: Code Clause
- **Libraries**: OpenCV, MediaPipe, Streamlit teams

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Classes and Data Structures
KeyBdInput: Represents a keyboard input event.
HardwareInput: Represents a hardware input event.
MouseInput: Represents a mouse input event.
Input_I: A union representing different types of input events.
Input: Represents an input event, containing the type and the event data.
Functions
press_key(key): Simulates pressing a key.
release_key(key): Simulates releasing a key.
