# 🎥🎨 Video Cartoonizer

This project converts normal videos into cartoon-style animations using OpenCV.

## ✨ Features
- Applies cartoon effect frame by frame
- Saves cartoonized video in MP4 format

## 🛠️ How It Works

For each frame in the video:

### 🎨 Color Path
- Applies a bilateral filter to reduce noise while preserving edges.
- Performs color quantization to simplify and flatten colors.

### ✏️ Edge Path
- Converts the frame to grayscale.
- Applies median blur to reduce detail.
- Uses Canny edge detection to find edges.
- Dilates edges to make them bolder.

### 🧩 Final Composition
- Inverts the edge mask (edges in black).
- Combines the mask with the simplified color image.

## 📦 Requirements
- Python 3.x  
- OpenCV  
- NumPy  

Install dependencies:

```bash
pip install opencv-python numpy
```

## ▶️ How to Run

```bash
python cartoonize_video.py --input sample_input/input_video.mp4 --output sample_output/cartoonized_video.mp4
```
