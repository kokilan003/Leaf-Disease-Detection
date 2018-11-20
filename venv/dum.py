#import the 'tkinter' module
import tkinter
#create a new window
window = tkinter.Tk()
#set the window background to hex code '#a1dbcd'
window.configure(background="#a1dbcd")
#set the window title
window.title("Welcome")
#set the window icon
window.wm_iconbitmap('Icon.ico')
photo = tkinter.PhotoImage(file="title.gif")
w = tkinter.Label(root, image=photo)
w.pack()
#create a label for the instructions
lblInst = tkinter.Label(root, text="Please login to continue:", fg="#383a39", bg="#a1dbcd", font=("Helvetica",16))
#and pack it into the window
lblInst.pack()
#create the widgets for entering a username
lblUsername = tkinter.Label(window, text="Username:", fg="#383a39", bg="#a1dbcd")
entUsername = tkinter.Entry(window)
#and pack them into the window
lblUsername.pack()
entUsername.pack()
#create the widgets for entering a username
lblPassword = tkinter.Label(window, text="Password:", fg="#383a39", bg="#a1dbcd")
entPassword = tkinter.Entry(window)
#and pack them into to the window
lblPassword.pack()
entPassword.pack()
#create a button widget called btn
btn = tkinter.Button(window, text="Login", fg="#a1dbcd", bg="#383a39")
#pack the widget into the window
btn.pack()