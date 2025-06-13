import cv2
import numpy as np 
import matplotlib.pyplot as plt 

def quantization(img):
    b, g, r = cv2.split(img)
    new_R = r & 224
    new_G = g & 224
    new_B = b & 192
    result = cv2.merge((new_B, new_G, new_R))
    return result

def GrayAndBlur(img,blure_value):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray_blur=cv2.medianBlur(gray,blure_value)
    return gray_blur

def cany(blurred_gray_image):
    low_threshold,high_threshold=100,255
    result = cv2.Canny(blurred_gray_image, low_threshold, high_threshold)
    return result



input_video="/Users/test/Desktop/newTest/video1.mp4"
cap = cv2.VideoCapture(input_video)
frame_width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output_video1.mp4', fourcc, fps, (frame_width, frame_height))



while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    #all code proccessing for images

    #first path for colors:


    blurred=cv2.bilateralFilter(frame,d=9,sigmaColor=200,sigmaSpace=200)
    # gaussian_blurred = cv2.GaussianBlur(frame, ksize=(7, 7), sigmaX=0.5)
    # blurred=cv2.cvtColor(gaussian_blurred, cv2.COLOR_BGR2RGB)
    image_colored_final=quantization(blurred)

    #second path for edge detection:

    blure_value = 7
    gray_img=GrayAndBlur(frame , blure_value)
    cany_result = cany(gray_img)

    edge_thickness = 5
    kernel = np.ones((edge_thickness, edge_thickness), np.uint8)
    dilated_edges = cv2.dilate(cany_result, kernel, iterations=1)

    final_mask = cv2.bitwise_not(dilated_edges)

    cartoon_image = cv2.bitwise_and(image_colored_final, image_colored_final, mask = final_mask)



    output_video.write(cartoon_image)


cap.release()
output_video.release()
cv2.destroyAllWindows()