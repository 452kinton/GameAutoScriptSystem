from PIL import Image
import pytesseract
import autopy

class Languages:
    CHS = 'chi_sim'
    CHT = 'chi_tra'
    ENG = 'eng'

#图片识别转文字
def img_to_str(image_path, lang=Languages.ENG):
    return pytesseract.image_to_string(Image.open(image_path), lang)
  
#print(img_to_str('tili.jpg', lang=Languages.CHS))

#鼠标移动
def mouse_move_to(x=0.0,y=0.0):
    autopy.mouse.move(x,y)

def init_mouse_status():
    autopy.mouse.move(0,0)
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,False)

def mouse_move_with_pressing(startPoint,endPoint):
    init_mouse_status()
    mouse_move_to(startPoint[0],startPoint[1])
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,True)
    autopy.mouse.smooth_move(endPoint[0],endPoint[1])
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,False)

#查找图片
def find_pic_position_on_screen(image_path,tolerance = 0.6):
    rubbish=autopy.bitmap.Bitmap.open(image_path)
    screen=autopy.bitmap.capture_screen()
    pos=screen.find_bitmap(rubbish)
    if pos:
        return pos
    else:
        return [-1,-1]


#截取屏幕某位置图片
def capture_screen_by_rect(startPoint,endPoint):
    return autopy.bitmap.capture_screen([startPoint,endPoint])

def capture_entire_screen():
    return autopy.bitmap.capture_screen()
