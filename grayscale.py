from cImage import *

def grayPixel(oldPixel):
    intensitySum = oldPixel.getRed() + oldPixel.getGreen() \
		            + oldPixel.getBlue()
    aveRGB = intensitySum // 3
    newPixel = Pixel(aveRGB, aveRGB, aveRGB)
    return newPixel
    
def makeGrayScale(imageFile):    
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("Grayscale", width * 2, height)
    oldImage.draw(myImageWindow)  
    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            newPixel = grayPixel(oldPixel)
            newIm.setPixel(col, row, newPixel)

    newIm.setPosition(width + 1,0)
    newIm.draw(myImageWindow)

    myImageWindow.exitOnClick()
