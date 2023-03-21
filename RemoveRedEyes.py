from cImage import *

# Removes red eyes
def RemoveRedEyes(image, col1, row1, col2, row2):
    newImage = EmptyImage(image.getWidth(), image.getHeight())
    for row in range(newImage.getHeight()):     # Scans rows
        for col in range(newImage.getWidth()):  # Scans colums
            v = image.getPixel(col, row)

            if((row1 < row < row2) and (col1 < col < col2)):    # If the pixels is in target area
                if v.red > 150 and v.green < 100 and v.blue < 100:  # If image is to red
                    avg = (v.blue + v.green) // 2       # takes average blue and gree
                    v.red = avg                         # Removes redness
            newImage.setPixel(col, row, v)
    return newImage

# Draws box around region
def BoxLocation(image, col1, row1, col2, row2):
    newImage = EmptyImage(image.getWidth(), image.getHeight())
    for row in range(newImage.getHeight()):        # Scans rows
        for col in range(newImage.getWidth()):     # Scans colums
            v = image.getPixel(col, row)
            if((row1 == row) or col1 == col or row2 == row or col2 == col): # Makes box
                v.red = 255
                v.green = 255
                v.blue = 255
            newImage.setPixel(col, row, v)
    win = ImageWin("Location",image.getHeight(),image.getWidth())
    newImage.draw(win)