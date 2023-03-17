from cImage import *
import math
from pixelmapping import *

def convolve(anImage, pixelRow, pixelCol, kernel):
    kernelColumnBase = pixelCol - 1
    kernelRowBase = pixelRow - 1

    sum = 0
    for row in range(kernelRowBase, kernelRowBase + 3):
        for col in range(kernelColumnBase, kernelColumnBase + 3):
            kColIndex = col - kernelColumnBase
            kRowIndex = row - kernelRowBase

            aPixel = anImage.getPixel(col, row)
            intensity = aPixel.getRed()

            sum = sum + intensity * kernel[kRowIndex][kColIndex]

    return sum

def edgeDetect(theImage):
    grayImage = pixelMapper(theImage, grayPixel)
    newIm = EmptyImage(grayImage.getWidth(), grayImage.getHeight())
    black = Pixel(0, 0, 0)
    white = Pixel(255, 255, 255)
    XMask = [ [-1,-2,-1],[0,0,0],[1,2,1] ]
    YMask = [ [1,0,-1],[2,0,-2],[1,0,-1] ]

    for row in range(1, grayImage.getHeight() - 1):
        for col in range(1, grayImage.getWidth() - 1):
            gX = convolve(grayImage, row, col, XMask)
            gY = convolve(grayImage, row, col, YMask)
            g = math.sqrt(gX**2 + gY**2)

            #if g > 175:
            if g > 100:
                    newIm.setPixel(col, row, black)
            else:
                newIm.setPixel(col, row, white)

    return newIm 

def makeEdgeDetection(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin("Edge Detection", width * 2, height)
    oldImage.draw(myWin)
    
    newImage = edgeDetect(oldImage)
    newImage.setPosition(width + 1, 0)
    newImage.draw(myWin)
    
    myWin.exitOnClick()

if __name__ == '__main__':
    win = ImageWin("cImage Demo",800,500) # redEyes.gif is 395x489
    oldImage = FileImage('redEyes.gif')
    print(oldImage.getWidth(), oldImage.getHeight())
    oldImage.draw(win)

    newImage = edgeDetect(oldImage)

    #show newImage to the right of oldImage
    newImage.setPosition(newImage.getWidth()+1,10)
    newImage.draw(win)

    #obtain coordiates of left eye
    print(win.getMouse())
    print(win.getMouse())

    newImage.save('redEyes-inverted.gif')
    #print(newImage.toList())

    win.exitOnClick()
