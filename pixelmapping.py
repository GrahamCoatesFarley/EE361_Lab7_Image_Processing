from cImage import *
from grayscale import *
from negative import *

def pixelMapper(fileImage, rgbFunction):

    width = fileImage.getWidth()
    height = fileImage.getHeight()
    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = fileImage.getPixel(col, row)
            newPixel = rgbFunction(oldPixel)
            newIm.setPixel(col, row, newPixel)

    return newIm

def generalTransform(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("Grayscale", width * 2, height)
    oldImage.draw(myImageWindow)

    newImage = pixelMapper(oldImage, grayPixel)

    newImage.setPosition(oldImage.getWidth() + 1, 0)
    newImage.draw(myImageWindow)
    myImageWindow.exitOnClick()

