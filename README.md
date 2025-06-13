Video Cartoonizer
This project contains a Python script that converts a standard video into a cartoonized version using computer vision techniques with OpenCV.

Description
The cartoonize_video.py script reads a video file, processes each frame to give it a cartoon-like appearance, and then writes the processed frames to a new output video file. The cartoon effect is achieved by combining two main image processing paths: color quantization and edge detection.

The final output is a video where the colors are simplified into a limited palette, and prominent edges are highlighted with black lines, mimicking the style of a cartoon.

How It Works
The script processes the video frame by frame. For each frame, the following steps are performed:

Color Path:

A bilateral filter is applied to the frame to reduce noise while keeping the edges sharp.
The colors of the filtered image are then simplified through a process called color quantization. This reduces the number of colors in the image, giving it a flatter, more cartoonish look.
Edge Path:

The original frame is converted to grayscale.
A median blur is applied to the grayscale image to reduce detail.
The Canny edge detection algorithm is used to identify the significant edges in the blurred grayscale image.
The detected edges are then dilated to make them thicker and more pronounced.
Final Composition:

The dilated edges are inverted to create a mask where the edges are black and the rest is white.
This mask is applied to the color-quantized image. The result is an image that retains the simplified colors but has the detected edges drawn over it in black.
This process is repeated for every frame in the input video, and the resulting frames are compiled into the final output video.

Requirements
Python 3.x
OpenCV
NumPy

## How to Run

```bash
python cartoonize_video.py --input sample_input/input_video.mp4 --output sample_output/cartoonized_video.mp4
