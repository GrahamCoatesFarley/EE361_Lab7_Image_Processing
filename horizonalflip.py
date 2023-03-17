from cImage import *

def HorizonalflipFlip(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW, oldH)

    maxP = oldH - 1
    for row in range(oldH):
        for col in range(oldW):

            oldPixel = oldImage.getPixel(col, maxP - row)

            newIm.setPixel(col, row, oldPixel)

    return newIm

if __name__ == '__main__':

    win = ImageWin("Half Image Demo",1000,800) # castle.gif is 480x360
    oldImage = FileImage('castle.gif')
    print(oldImage.getWidth(), oldImage.getHeight())

    oldImage.draw(win)

    #Makes a half image
    newImage = HorizonalflipFlip(oldImage)

    #show newImage to the right of oldImage
    newImage.setPosition(oldImage.getWidth()+1,0)
    newImage.draw(win)

    #obtain coordiates of left eye
    print(win.getMouse())
    print(win.getMouse())

    newImage.save('castle_flip.gif')
    #print(newImage.toList())

    win.exitOnClick()