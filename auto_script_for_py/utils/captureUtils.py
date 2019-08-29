import tkinter

import tkinter.filedialog

import os

from PIL import ImageTk,ImageGrab,Image

from time import sleep

root = None
image = None
im = None

def defualtCallback(rect):
    print("x1,y1:"+str(rect[0])+","+str(rect[1]))
    print("x2,y2:"+str(rect[2])+","+str(rect[3]))
    img = ImageGrab.grab(bbox = rect)
    img.save("auto_script_for_py/temp/capture.png")
    img.close()

def startCapture(callback = defualtCallback):
    root = tkinter.Tk()
    #init(root)
    app =FullScreenApp(root,callable=callback)
    root.mainloop()

#def init(root):

class FullScreenApp(object):
    def __init__(self, master,callable,**kwargs):
        self.root = master
        self.rect = None
        self.callback = callable
        # self.root.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        # self.frame = tkinter.Frame(self.root)
        self.root.attributes("-topmost",True)
        self.root.attributes("-alpha", 1)
        self.root.attributes("-fullscreen", True)
        #filename = 'auto_script_for_py/temp/temp1.png'
        #grab.save(filename)
        #grab.close()
        self.canvas = tkinter.Canvas(self.root,
        width = self.root.winfo_screenwidth(),      # 指定Canvas组件的宽度
        height = self.root.winfo_screenheight(),      # 指定Canvas组件的高度
        bg = 'white')
        #grab = ImageGrab.grab()
        global image
        global im
        image = ImageGrab.grab()
        im = ImageTk.PhotoImage(image)  
        #grab.close()
        self.canvas.create_image(self.root.winfo_screenwidth()/2,self.root.winfo_screenheight()/2,image = im)
        self.canvas.pack() 
        # canvas.create_rectangle
        self.root.bind("<Button-3>",func=self.right_btn_click)
        self.root.bind("<Button-1>",func=self.left_btn_click)
        self.root.bind("<B1-Motion>",func=self.move_with_left_btn_press)
        self.root.bind("<ButtonRelease-1>",func=self.left_btn_realese)

    

    def right_btn_click(self,event):
        #print("ok")
        self.status = 'default'
        self.callback((self.startX,self.startY,self.endX,self.endY))
        self.root.destory()
    
    def left_btn_click(self,event):
        self.status = 'capturing'
        self.startX = event.x
        self.startY = event.y
    
    def left_btn_realese(self,event):
        if(self.rect != None):
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.startX,self.startY,event.x,event.y,outline='red')
        self.status = 'default'
        self.endX = event.x
        self.endY = event.y
        self.status = 'default'
        self.callback((self.startX,self.startY,self.endX,self.endY))
        self.root.quit()

    def move_with_left_btn_press(self,event):
        if(self.rect != None):
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.startX,self.startY,event.x,event.y)
        


startCapture(defualtCallback)



