import tkinter.messagebox as tmsg
from tkinter import *
import string
import cv2
import pytesseract
##Reading the image from the system
img=cv2.imread(r"C:\Users\DEVESH\Downloads\CARS\FINAL IMGE\d0.jpg")
##Showing the original image
cv2.imshow("ORIGINAL IMAGE",img)
cv2.waitKey(0)
cv2.destroyWindow("ORIGINAL IMAGE")
##Coverting the image into the grayscale image
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAYSCALE IMAGE",img_gray)
cv2.waitKey(0)
cv2.destroyWindow("GRAYSCALE IMAGE")
#Applying the gaussianblur method for blurring the image
img_gray=cv2.GaussianBlur(img_gray,(3,3),17,17)
cv2.imshow("GAUASSIAN BLUR IMAGE",img_gray)
cv2.waitKey(0)
cv2.destroyWindow("GAUASSIAN BLUR IMAGE")
#Applying the pretrained model to detect the license plate
plate=cv2.CascadeClassifier(r"D:\opencv-master\data\haarcascades\haarcascade_russian_plate_number.xml")
##storing the position ofthe license plate
plate_pos=plate.detectMultiScale(img_gray)
try:
   ##highlighting the license plate dected in the original image
  for (x,y,w,h) in plate_pos[0:1]:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,55,52),1)
    ##seperating the image of license plate from the original image
    sep=img[y:y+h,x:x+w]
  ##decting the text from the seprated image
  dected_number=pytesseract.image_to_string(sep)
except:
  plate_pos=plate.detectMultiScale(img_gray,1.2,5)
  for (x,y,w,h) in plate_pos[0:1]:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,55,52),1)
    sep=img[y:y+h,x:x+w]
    dected_number=pytesseract.image_to_string(sep)
##Showing the deted license plate image
cv2.imshow("DETECTED LICENSE PLATE AND SEPRATED FROM THE  ORIGINAL IMAGE",sep)
cv2.waitKey(0)
cv2.destroyAllWindows()
##Showing the image
cv2.imshow("ORIGINAL IMAGE WITH HIGHLIGHTED IMAGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##Filtering the license plate number
valid_number=string.ascii_letters+string.digits
final_result_part1=""
for i in range(len(dected_number)):
   if dected_number[i] in valid_number:
       final_result_part1=final_result_part1+dected_number[i]
print("NUMBER PLATE IS =",final_result_part1)

#Calling the other method
from Project_part2 import *
number()
#Finaliszation of the number detected
if final_result_part1==final_result_part2:
      print("This is our final reslut",final_result_part1)
      TEMP=final_result_part1
elif len(final_result_part1)==0:
    print("THE RESLUT",final_result_part2)
    TEMP=final_result_part2
elif len(final_result_part2)==0:
    print("THE RESLUT",final_result_part1)
    TEMP=final_result_part1
root=Tk()

import time
TIME=time.localtime()
value=tmsg.askquestion("Save","Do you want to save the details?")
if value=="yes":
  file=open("IMP","a")
  file.write("\nTHE PLATE NUMBER IS ={0:<10}".format(TEMP))
  file.write(f"\t\t\t\t  DATE= {TIME[2]}/{TIME[1]}/{TIME[0]}")
  file.write(f"\t\t\t\t  TIME={TIME[3]}:{TIME[4]}:{TIME[5]}")
  file.close()
  tmsg.showinfo("SAVED","Details are saved")
else:
     tmsg.showinfo("Exit","Details are not saved")
root.mainloop()

