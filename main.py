import cv2
import numpy as np
import matplotlib.pyplot as plt 

# Load the image
image_path = "C:/Users/Farouk/Downloads/test.jpg" 
image = cv2.imread(image_path)



image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Edge detection
blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)
edges = cv2.Canny(blurred, 45, 140)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output_image = image_rgb.copy()

# HSV color detection function
def identify_color_hsv(bgr_color):
    # BGR to HSV
    hsv_color = cv2.cvtColor(np.uint8([[bgr_color]]), cv2.COLOR_BGR2HSV)[0][0]
    h, s, v = hsv_color

    # rnges of colors
    if s < 50 and v > 200:
        return "white"
    elif h < 10 or h > 160:
        return "red"
    elif 20 < h < 40:  
        return "yellow"
    elif 40 < h < 80:
        return "green"
    elif 80 < h < 140:
        return "blue"
    else:
        return "unknown"
