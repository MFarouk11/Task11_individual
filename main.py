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

