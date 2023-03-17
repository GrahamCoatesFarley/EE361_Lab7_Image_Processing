from cImage import *

def verticalFlip(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW, oldH)

    maxP = oldW - 1
    for row in range(oldH):
        for col in range(oldW):

            oldPixel = oldImage.getPixel(maxP - col, row)

            newIm.setPixel(col, row, oldPixel)

    return newIm

def makeFlip(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    
    myWin = ImageWin("Vertical Flip", width * 2, height)
    oldImage.draw(myWin)
    
    newImage = verticalFlip(oldImage)
    newImage.setPosition(width + 1, 0)
    newImage.draw(myWin)
    
    myWin.exitOnClick()

if __name__ == '__main__':
    # Part 1 #########################################################
    win = ImageWin("cImage Demo",800,500) # redEyes.gif is 395x489
    oldImage2 = FileImage('redEyes.gif')
    print(oldImage2.getWidth(), oldImage2.getHeight())
    oldImage2.draw(win)

    newImage2_flip = verticalFlip(oldImage2)
    newImage2_flip.setPosition(newImage2_flip.getWidth() + 1, 0)
    newImage2_flip.draw(win)

    print(win.getMouse())
    print(win.getMouse())

    newImage2_flip.save('castle_flip.gif')
    # print(newImage.toList())

    win.exitOnClick()