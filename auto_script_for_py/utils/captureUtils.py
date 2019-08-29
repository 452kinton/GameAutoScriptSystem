import tkinter

import tkinter.filedialog

import os

from PIL import ImageTk,ImageGrab,Image

from time import sleep

global root

global grab

image = None
im = None

def startCapture():
    root = tkinter.Tk()
    #init(root)
    app =FullScreenApp(root)
    root.mainloop()

#def init(root):



class FullScreenApp(object):
     def __init__(self, master, **kwargs):
        self.root = master
        # self.root.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        # self.frame = tkinter.Frame(self.root)
        self.root.attributes("-topmost",True)
        self.root.attributes("-alpha", 1)
        self.root.attributes("-fullscreen", True)
        filename = 'auto_script_for_py/temp/temp1.png'
        #grab.save(filename)
        #grab.close()
        canvas = tkinter.Canvas(self.root,
        width = self.root.winfo_screenwidth(),      # 指定Canvas组件的宽度
        height = self.root.winfo_screenheight(),      # 指定Canvas组件的高度
        bg = 'white')
        #grab = ImageGrab.grab()
        global image
        global im
        image = ImageGrab.grab()
        im = ImageTk.PhotoImage(image)  
        #grab.close()
        bit = canvas.create_image(self.root.winfo_screenwidth()/2,self.root.winfo_screenheight()/2,image = im)    
        canvas.move(bit,0,0)
        canvas.pack()   

startCapture()