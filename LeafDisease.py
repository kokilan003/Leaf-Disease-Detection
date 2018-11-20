import time
import tkinter

import cv2
import matplotlib.pyplot as mt
import glob
import sys
import numpy as np
import pickle
from tkinter import font
from tkinter import *
#from kFileDialog import askopenfilename
from tkinter import filedialog
#import time
from sklearn.neural_network import MLPClassifier
hog = cv2.HOGDescriptor()
#import warnings

#if not sys.warnoptions:
   # warnings.simplefilter("ignore")


root = Tk()
root.wm_iconbitmap('Icon.ico')

photo = tkinter.PhotoImage(file="leaf1.png")
w = tkinter.Label(root, image=photo)
w.pack()
lblInst = tkinter.Label(root, )
lblInst.pack()

appHighlightFont = font.Font(family='Helvetica', size=12, weight='bold')
font.families()
root.geometry('500x300')
root.configure(background='#145A32')

clf = pickle.load(open('neural.model', 'rb')) #Create From TraningModel.py

def main(img_rec):

    img = img_rec
    img = cv2.resize(img, (150, 150))
    h = hog.compute(img)
    fet = np.array(h)
    fet = np.reshape(fet, [1, 124740])



    if (clf.predict(fet)[0] == 0):
     print('Normal\r\n')

     if (clf.predict(fet)[0] == 1):
        print('Disease: Brown Spot\r\n')
        file = open('BrownSpot-solution.txt', 'r')
        print('Solution:\r\n')
        print(file.read())

    if (clf.predict(fet)[0] == 2):
        print('Disease:Paddy Blast\r\n')
        file = open('Rice Blast.txt', 'r')
        print('Solution:\r\n')
        print(file.read())
    if (clf.predict(fet)[0] == 3):
        print('Disease:Bactarial\r\n')
        file = open('bactarialleaf.txt', 'r')
        print('Solution:\r\n')
        print(file.read())

   # if (clf.predict(fet)[0] != 0,1,2,3):
      #  print('error\r\n')
   # if (clf.predict(fet)[0] != 0 and clf.predict(fet)[0] != 1 and clf.predict(fet)[0] != 2 and clf.predict(fet)[0] != 3):
       #print('negative image')


def image_disk():
        Tk().withdraw()
        filename = filedialog.askopenfilename()
   # img = cv2.imread(filename)
        img = cv2.imread(filename)
        main(img)



def image_camera():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)

        if not ret:
            break
        k = cv2.waitKey(1)

        if k % 256 == 27:  # PRESS ESCAPE TO CLOSE THE WEBCAM WINDOW
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:  # TAKE IMAGE PY PRESSING SPACE (TAKE ONLY 1 AT A TIME)
            # SPACE pressed
            img_name = str(img_counter) + ".png"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()
    my_img = cv2.imread("0.png")  # CV2 will only read image named "0.png"
    main(my_img)


button = Button(root,
                text="Select Image From Disk",
                font="appHighlightFont",
                bg="#000080",
                fg="white",padx=5, pady=15,
                command=image_disk)
button.place(relx=0.5, rely=0.5, anchor=CENTER)
#button.grid(row=0, column=0)

button.pack(side=TOP)
lblInst = tkinter.Label(root, )
lblInst.pack()

slogan = Button(root,
                text="Take Image from WebCam",
                font="appHighlightFont", bg="#641E16  ",
                fg="white", padx=5, pady=15,
                command=image_camera)
slogan.place(relx=1, rely=1, anchor=CENTER)
#slogan.place(x=50, y=50)

slogan.pack(side=TOP)


root.mainloop()