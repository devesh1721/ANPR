import string
import numpy as np
import cv2
import pytesseract
##Reading the image
img=cv2.imread(r"C:\Users\DEVESH\Downloads\CARS\FINAL IMGE\d0.jpg")
cv2.imshow("ORIGINAL IMAGE",img)
cv2.waitKey(0)
cv2.destroyWindow("ORIGINAL IAMGE")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gray=cv2.GaussianBlur(img_gray,(3,3),17,17)
median=np.median(img_gray)
lower=int(max(0,0.7*median))
upper=int(min(255,1.3*median))
# canny_edge=cv2.Canny(img_gray,170,200)
canny_edge=cv2.Canny(img_gray,lower,upper)
cv2.imshow("CANNY OF SEPRATED IMAGE",canny_edge)
cv2.waitKey(0)
cv2.destroyWindow("CANNY OF SEPRATED IMAGE")
blank=np.zeros(img.shape,np.uint8)
##finding counters
counters,new=cv2.findContours(canny_edge,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
counters=sorted(counters,key=cv2.contourArea,reverse=True)
counters_with_image=None
license_plate=None
x=None
y=None
w=None
h=None
for counter in counters:
    perimetrs=cv2.arcLength(counter,True)
    approx=cv2.approxPolyDP(counter,0.01*perimetrs,True)
    if len(approx)==4:
        x,y,w,h=cv2.boundingRect(approx)
        counters_with_image=approx
        x,y,w,h=cv2.boundingRect(counter)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,23),2)
        license_plate=img[y:y+h,x:x+w]
        break
cv2.imshow("counter area",img)
cv2.waitKey(0)
cv2.destroyWindow("counter area")
cv2.imshow("LICENSE PLATE",license_plate)
cv2.waitKey(0)
cv2.destroyWindow("LICENSE PLATE")
final_result=pytesseract.image_to_string(license_plate)
alpha=string.ascii_letters
digit=string.digits
dict=digit+alpha
final_result_part2=""
for i in range(len(final_result)):
    if final_result[i] in dict:
        final_result_part2=final_result_part2+final_result[i]

print("NUMBER PLATE IS =",final_result_part2)
def number():
    print("NUMBER PLATE IS =",final_result_part2)
    return final_result_part2
cv2.destroyAllWindows()
