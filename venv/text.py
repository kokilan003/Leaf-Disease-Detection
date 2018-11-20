# -*- coding: UTF-8 -*-
import cv2
import pickle
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


def disp_solution_1(res):
    root = Tk()
    txt = Text(root, wrap='word')
    txt.pack()

    txt.tag_configure('text_body', font=('Times', 15), lmargin1=0,
                      lmargin2=0)
    txt.tag_configure('bulleted_list', font=('Times', 12), lmargin1='10m',
                      lmargin2='15m', tabs=['15m'])
    txt.tag_configure('bullets', font=('Dingbats', 12))
    if(res == 'Image process'):
        txt.insert(END, u"Result using Image processing\n\n", 'text_body')
    if(res == 'Neural'):
        txt.insert(END, u"Result using Neural\n\n", 'text_body')
    txt.insert(END, u"Disease Found: BACTERIAL LEAF BLIGHT OF RICE\n\n", 'text_body')
    txt.insert(END, u"SOLUTION:\n", 'text_body')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Apply judicious level of fertilization (60-80 kg N/ha with required level of potassium) without sacrificing the yield.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Avoid insect damage to the crop.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Avoid field to field irrigation.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Destroy infected stubbles and weeds.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Avoid shade in the field.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Grow resistant/tolerant varieties like Ajaya, IR 64, Radha, Pantdhan 6, Pantdhan 10.\n",
               'bulleted_list')


def disp_solution_2(res):
    root = Tk()
    txt = Text(root, wrap='word')
    txt.pack()

    txt.tag_configure('text_body', font=('Times', 15), lmargin1=0,
                      lmargin2=0)
    txt.tag_configure('bulleted_list', font=('Times', 12), lmargin1='10m',
                      lmargin2='15m', tabs=['15m'])
    txt.tag_configure('bullets', font=('Dingbats', 12))
    if (res == 'Image process'):
        txt.insert(END, u"Result using Image processing\n\n", 'text_body')
    if (res == 'Neural'):
        txt.insert(END, u"Result using Neural\n\n", 'text_body')

    txt.insert(END, u"Disease Found: BROWN SPOT IN RICE\n\n", 'text_body')
    txt.insert(END, u"SOLUTION:\n", 'text_body')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Monitor soil nutrients regularly.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Apply required fertilizers\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"For soils that are low in silicon, apply calcium silicate slag before planting.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"To be sure that the seeds are not contaminated, bathe them in hot water (53 - 54 C) for 10 to 12 minutes. To improve the results, place the seeds for 8 hours in cold water before the hot water treatment.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Treat seeds with fungicides containing Iprodione, Propiconazole, Azoxystrobin, Trifloxystrobin or Carbendazim.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Spraying of crop at tillering and late booting stages with Carbendazim 12% + Mancozeb 63% WP @ "
                    u"1gm/litre or Zineb @ 2 gm/litre of water. Repeat spray after 15 days.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Growing of resistant/tolerant varieties like Rasi, Jagnanath, IR 36 etc.\n", 'bulleted_list')


def disp_solution_3(res):
    root = Tk()
    txt = Text(root, wrap='word')
    txt.pack()

    txt.tag_configure('text_body', font=('Times', 15), lmargin1=0,
                      lmargin2=0)
    txt.tag_configure('bulleted_list', font=('Times', 12), lmargin1='10m',
                      lmargin2='15m', tabs=['15m'])
    txt.tag_configure('bullets', font=('Dingbats', 12))
    if (res == 'Image process'):
        txt.insert(END, u"Result using Image processing\n\n", 'text_body')
    if (res == 'Neural'):
        txt.insert(END, u"Result using Neural\n\n", 'text_body')

    txt.insert(END, u"Disease Found: RICE BLAST\n\n", 'text_body')
    txt.insert(END, u"SOLUTION:\n", 'text_body')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Manipulation of planting time and fertilizer and water management is advised.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Early sowing of seeds after the onset of the rainy season is more advisable than late-sown crops.\n",
               'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Excessive use of fertilizer should be avoided.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Nitrogen should be applied in small increments at any time.\n", 'bulleted_list')
    txt.insert(END, u'\u25C6', 'bullets')
    txt.insert(END, u"Spray  tricylazole  75% WP @ 0.6gm/ litre or Propiconazole 25% EC 1ml/ litre or Carbendazim 50% WP @ 1gm/litre of water.\n",
               'bulleted_list')


def disp_solution_4(res):
    root = Tk()
    txt = Text(root, wrap='word')
    txt.pack()

    txt.tag_configure('text_body', font=('Times', 15), lmargin1=0,
                      lmargin2=0)
    if (res == 'Image process'):
        txt.insert(END, u"Result using Image processing\n\n", 'text_body')
    if (res == 'Neural'):
        txt.insert(END, u"Result using Neural\n\n", 'text_body')
    txt.insert(END, u"Disease Found: NONE\n\n", 'text_body')
    txt.insert(END, u"NORMAL LEAF\n", 'text_body')


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

    LBmax_x, LBmax_y = cal_MaxX_MaxY(widthLB, heightLB, maskLB)
    Ymax_x, Ymax_y = cal_MaxX_MaxY(widthY, heightY, maskY)
    Bmax_x, Bmax_y = cal_MaxX_MaxY(widthB, heightB, maskB)
    TYmax_x, TYmax_y = cal_MaxX_MaxY(widthTY, heightTY, tempY)
    TBmax_x, TBmax_y = cal_MaxX_MaxY(widthTB, heightTB, tempB)

    # print Ymax_x
    print ("Yellow = ", TYmax_y)
    #print "Yellowx = ", TYmax_x
    print ("Brown = ", TBmax_y)
    #print "Brownx  = ", TYmax_x

    if TYmax_y < 8 and TBmax_y < 8:
        res = 'Image process'
        print (diseases[3])
        disp_solution_4(res)

    elif LBmax_x > LBmax_y:
        res = 'Image process'
        print (diseases[2])
        disp_solution_1(res)

    else:
        res = 'Image process'

        if TYmax_y < 30:
            print (diseases[0])
            disp_solution_2(res)

        elif TBmax_y > TYmax_y:

            if TYmax_y > 56:
                print (diseases[1])
                disp_solution_3(res)

            elif TBmax_y - TYmax_y < 5:
                print (diseases[1])
                disp_solution_3(res)

            else:
                print (diseases[0])
                disp_solution_2(res)

        elif TYmax_y >= TBmax_y:

            if TYmax_y < 56:
                print (diseases[0])
                disp_solution_2(res)

            else:
                print (diseases[1])
                disp_solution_3(res)

hog = cv2.HOGDescriptor()
def main1(img1_rec):
    diseases = ['brown_spots', 'paddy blast', 'bacterial leaf', 'Normal leaf']
    img = img1_rec
    img = cv2.resize(img, (150, 150))
    h = hog.compute(img)
    fet = np.array(h)
    fet = np.reshape(fet, [1, 124740])
    clf = pickle.load(open('neural.model', 'rb'))
    if (clf.predict(fet)[0] == 0):
        res='Neural'
        print (diseases[3])
        disp_solution_4(res)
    if (clf.predict(fet)[0] == 1):
        res = 'Neural'
        print (diseases[0])
        disp_solution_2(res)

    if (clf.predict(fet)[0] == 2):
        resl = 'Neural'
        print (diseases[1])
        disp_solution_3(resl)

    if (clf.predict(fet)[0] == 3):
        resl = 'Neural'
        print (diseases[2])
        disp_solution_1(resl)

def image_disk():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = filedialog()  # show an "Open" dialog box and return the path to the selected file
    img = cv2.imread(filename)

    main(img)
    main1(img)


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
    main1(my_img)


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