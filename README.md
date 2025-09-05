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
Lighting conditions,i found that HSV worked better than BGR.
Shape approximations caused shaps to be misclassified.
Threshold tuning: Canny thresholds and contour area filtering had to be carefully chosen.
Without Deep Learning, this approach requires hand-crafted rules for each shape and color
