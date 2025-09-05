<img width="1200" height="685" alt="Screenshot 2025-09-05 224457" src="https://github.com/user-attachments/assets/fc21e564-450f-4e80-9626-94e5e43b3827" />
This project demonstrates how to detect shapes (triangles, rectangles, squares, circles) 
and identify their colors using classical computer vision methods (OpenCV) 
without relying on modern deep learning tools
----------------------------------------------------------------------------------------Alvaroo----------------------------------------------------------------------------------------------

Algorithms and Techniques
-------------------------
Gaussian Blur: Noise reduction.
Canny Edge Detection: Extracts edges for contour detection.
Contour Approximation: Polygonal curve approximation to detect vertices.
Aspect Ratio Check: Differentiates squares from rectangles.
HSV Color Space: Provides robust color classification under lighting variations.

----------------------------------------------------------------------------------------Alvaroo----------------------------------------------------------------------------------------------

Challenges
---------
yellow color i couldnot detect it, i will update it in the future.
Lighting conditions,i found that HSV worked better than BGR.
Shape approximations caused shaps to be misclassified.
Threshold tuning: Canny thresholds and contour area filtering had to be carefully chosen.
Without Deep Learning, this approach requires hand-crafted rules for each shape and color
