import cv2
import numpy as np


# Import the image
file_name = "t2.jpg"
  
# Read the image
src = cv2.imread(file_name, 1)
  
# Convert image to image gray
gray_image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  
# Applying thresholding technique
#alpha = cv2.adaptiveThreshold(tmp,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,4)
binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 4)
kernel=np.ones((1,1),np.uint8)
closing=cv2.morphologyEx(binary_image,cv2.MORPH_CLOSE,kernel,iterations=6)



# Creating the final image by combining the original image and the binary image
final_image = cv2.bitwise_and(src, src, mask=closing)

# Display the original, binary, and final images
cv2.imshow("Original Image", src)
cv2.imshow("Binary Image", closing)
cv2.imshow("Final Image", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()





