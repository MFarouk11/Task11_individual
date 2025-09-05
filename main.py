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
# Shape detection and annotation
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 50:  
        continue

    # Approximate the contour to shaps
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

    shape = "unidentified"
    vertices = len(approx)

    if vertices == 3:
        shape = "triangle"
    elif vertices == 4:
        rect = cv2.minAreaRect(contour)
        width, height = rect[1]
        if width == 0 or height == 0:
            continue
        aspect_ratio = width / float(height)
        shape = "square" if 0.95 <= aspect_ratio <= 1.05 else "rectangle"
    elif vertices > 4:
        shape = "circle"

    # Mask the contour area
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.drawContours(mask, [contour], -1, 255, -1)
    mean_color = cv2.mean(image, mask=mask)[:3]  
    color_name = identify_color_hsv(mean_color)

    #detected shape and color
    cv2.drawContours(output_image, [approx], -1, (0, 0, 0), 2)
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.putText(output_image, f"{color_name} {shape}", (cX - 50, cY),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)


# the results
plt.figure(figsize=(12, 8))
plt.imshow(output_image)
plt.axis("off")
plt.title("Detected Shapes and Colors (HSV)")
plt.show()
