import cv2
import numpy as np
import imutils
img=cv2.imread("t1.JPG")



gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_blur=cv2.GaussianBlur(gray,(15,15),0)
thresh=cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,4)
kernel=np.ones((3,3),np.uint8)
closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=3)

result_img=closing.copy()
cnt=cv2.findContours(result_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnt = imutils.grab_contours(cnt)
counter=0


    
    
for contour in cnt:
    area = cv2.contourArea(contour)
    if area > 200 and area < 700:
        contour_image = cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)
        counter+=1
cv2.putText(img,str(counter),(10,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0),2,cv2.LINE_AA)
cv2.imshow("Show",img)



print(counter)
cv2.waitKey(0)
cv2.destroyAllWindows()