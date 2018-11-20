import cv2
from tkinter import *
import numpy as np
from tkinter import filedialog


root = Tk()
root.geometry('400x400')  # Set Window size
root.configure(background='black')  # Set background to black


def cal_MaxX_MaxY(width, height, mask):
    max_x = 0
    max_y = 0

    for i in range(0, height):  # Detect length of whites on X-axis
        temp = 0
        for j in range(0, width):
            if mask[i, j] == 255:
                temp += 1

        if temp > max_x:
            max_x = temp

    for i in range(0, width):  # Detect length of whites on X-axis
        temp = 0
        for j in range(0, height):
            if mask[j, i] == 255:
                temp += 1

        if temp > max_y:
            max_y = temp

    return max_x, max_y

def main(img_rec):
    diseases = ['brown_spots', 'paddy blast', 'bacterial leaf', 'Normal leaf']
    img = img_rec
    img = cv2.resize(img, (400, 400))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_range = np.array([21, 8, 63], dtype=np.uint8)  # Works for BACTERIAL LEAF (100% Accuracy)
    upper_range = np.array([30, 255, 255], dtype=np.uint8)

    Ylower_range = np.array([17, 100, 100], dtype=np.uint8)  # For detecting yellow in paddy blast
    Yupper_range = np.array([23, 255, 255], dtype=np.uint8)

    Blower_range = np.array([0, 80, 40], dtype=np.uint8)  # Works for separating brown spots and bacterial leaf
    Bupper_range = np.array([20, 255, 255], dtype=np.uint8)

    maskLB = cv2.inRange(hsv, lower_range, upper_range)
    maskY = cv2.inRange(hsv, Ylower_range, Yupper_range)
    maskB = cv2.inRange(hsv, Blower_range, Bupper_range)
    tempY = maskY - maskB
    tempB = maskB - maskY

    heightLB, widthLB = maskLB.shape[:2]
    heightY, widthY = maskY.shape[:2]
    heightB, widthB = maskB.shape[:2]
    heightTY, widthTY = tempY.shape[:2]
    heightTB, widthTB = tempB.shape[:2]

    print ("heightLB =",heightB)



    LBmax_x, LBmax_y = cal_MaxX_MaxY(widthLB, heightLB, maskLB)
    Ymax_x, Ymax_y = cal_MaxX_MaxY(widthY, heightY, maskY)
    Bmax_x, Bmax_y = cal_MaxX_MaxY(widthB, heightB, maskB)
    TYmax_x, TYmax_y = cal_MaxX_MaxY(widthTY, heightTY, tempY)
    TBmax_x, TBmax_y = cal_MaxX_MaxY(widthTB, heightTB, tempB)


    print ("light brown LBmax_x =",LBmax_x)
    print ("light brown LBmax_y =",LBmax_y)
    print ("yellow to light brown Ymax_x =",Ymax_x)
    print ("yellow to light brown Ymax_y =",Ymax_y)
    print ("brown to black Bmax_x =",Bmax_x)
    print ("brown to black Bmax_y =",Bmax_y)
    print ("only yellow TYmax_x =",TYmax_x)
    print ("only yellow TYmax_y =",TYmax_y)
    print ("only brown TBmax_x =",TBmax_x)
    print ("only brown TBmax_y =",TBmax_y)


    # print Ymax_x
    print ("Yellow = ", TYmax_y)
    #print "Yellowx = ", TYmax_x
    print ("Brown = ", TBmax_y)
    #print "Brownx  = ", TYmax_x




def image_disk():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = filedialog.askopenfilename()  # show an "Open" dialog box and return the path to the selected file
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
                fg="red",
                command=image_disk)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

button.pack(side=TOP)

slogan = Button(root,
                text="Take Image from WebCam",
                fg="red",
                command=image_camera)
slogan.place(relx=1, rely=1, anchor=CENTER)
slogan.pack(side=TOP)

root.mainloop()