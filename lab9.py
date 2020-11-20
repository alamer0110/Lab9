from gfxhat import lcd,  fonts, backlight
from PIL import Image, ImageFont, ImageDraw
from click import getchar

def clearBackLight():
    backlight.set_all(0,0,0)
    backlight.show()

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 


def setLight(r,g,b):
    backlight.set_all(r,g,b)
    backlight.show()


def etchSketch(x,y):
    while True:
        key = getchar()
        lcd.set_pixel(x,y, 1)
        lcd.show()
        if key =='s': # restart game 
            clearScreen(lcd)
        elif key == '\x1b[A': #up arrow     
            y = y-1
            if y == 0:
                y = 63
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == '\x1b[B': #down up
            y = y+1
            if y == 63:
                y = 0 

            lcd.set_pixel(x,y,1)
            lcd.show()
             

        elif key == '\x1b[D': #left arrow
            x = x-1
            if x == 0 :
                x = 127
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == 'x1b[C': #right arrow 
            x = x+1
            if x == 127 :
                x = 0  
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key =='q':
            lcd.clear()
            lcd.show()
            exit()
        else:
            print("Press a valid option") 
def displayObject(obj, x, y):
    lcd.clear()
    xp = x
    for y1 in obj:
        for x2 in y1:
            lenY = len(obj)
            lenX = len(y1)

            if x2 == 1 :
                pixel = 1 

            else : 
                pixel = 0 
            lcd.set_pixel(xp , y , pixel)
            xp = xp+1
        y = y+1     
        lcd.set_pixel(xp, y, pixel)
        xp = x 
    lcd.show()    