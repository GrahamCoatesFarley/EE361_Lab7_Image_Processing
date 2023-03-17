from cImage import *

def negativePixel(oldPixel):
    newRed = 255 - oldPixel.getRed()
    newGreen = 255 - oldPixel.getGreen()
    newBlue = 255 - oldPixel.getBlue()
    newPixel = Pixel(newRed, newGreen, newBlue)
    return newPixel

def makeNegative(oldImage):
    # oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    #myImageWindow = ImageWin("Negative Image", width * 2, height)
    #myImageWindow = ImageWin(width * 2, height, "Negative Image")
    #oldImage.draw(myImageWindow)
    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            newPixel = negativePixel(oldPixel)
            newIm.setPixel(col, row, newPixel)
    return newIm
    #newIm.setPosition(width + 1, 0)
    #newIm.draw(myImageWindow)
    #myImageWindow.exitOnClick()