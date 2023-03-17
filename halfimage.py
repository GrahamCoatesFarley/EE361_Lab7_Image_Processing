from cImage import *
from doubleimage import *

def halfImage(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW // 2, oldH // 2)

    for row in range(oldH):
        for col in range(oldW):
            oldPixel = oldImage.getPixel(col, row)

            newIm.setPixel(col // 2, row // 2, oldPixel)
            newIm.setPixel(col // 2 , row // 2, oldPixel)
            newIm.setPixel(col // 2, row // 2 , oldPixel)
            newIm.setPixel(col // 2 , row // 2 , oldPixel)

    return newIm

if __name__ == '__main__':

    win = ImageWin("Half Image Demo",1500,800) # castle.gif is 480x360
    oldImage = FileImage('castle.gif')
    print(oldImage.getWidth(), oldImage.getHeight())

    #doubles old image
    oldImage = doubleImage(oldImage)
    oldImage.draw(win)

    #Makes a half image
    newImage = halfImage(oldImage)

    #show newImage to the right of oldImage
    newImage.setPosition(oldImage.getWidth()+1,0)
    newImage.draw(win)

    #obtain coordiates of left eye
    print(win.getMouse())
    print(win.getMouse())

    newImage.save('castle_half.gif')
    #print(newImage.toList())

    win.exitOnClick()