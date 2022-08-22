import cv2
import numpy as np
from tkinter.filedialog import askopenfilename
from tkinter import *
root = Tk()
root.title("image to cartoon")
root.geometry('644x300+0+0')
label = Label(
    text='welcome to the party bro...'
)
label.pack()
try:
    photo = askopenfilename()
    print(photo)
    img = cv2.imread(photo)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grey = cv2.medianBlur(grey, 2)
    edges = cv2.adaptiveThreshold(
        grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # nowm cartoon it

    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imshow("Image", img)
    cv2.imshow("cartoon", cartoon)
    #  save
    cv2.imwrite("cartoon200.jpg", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except EXCEPTION as e:
    print(e)
root.mainloop()
