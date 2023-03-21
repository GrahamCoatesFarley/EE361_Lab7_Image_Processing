from cImage import *
from RemoveRedEyes import *

if __name__ == '__main__':
    win = ImageWin("Red Eye removal Demo",800,1000) # redEyes1.gif is 395x489
    oldImage = FileImage('redEyes1.gif')
    print(oldImage.getWidth(), oldImage.getHeight())
    oldImage.draw(win)

    #newImage is the red eyes removed
    col1 = 100
    col2 = 270
    row1 = 170
    row2 = 230

    # Used to show target region
    #BoxLocation(oldImage, col1, row1, col2, row2)


    newImage = RemoveRedEyes(oldImage, col1, row1, col2, row2)

    #show newImage to the right of oldImage
    newImage.setPosition(newImage.getWidth()+1,0)
    newImage.draw(win)

    # Second red eye demo
    oldImage2 = FileImage('redEyes2.gif')
    oldImage2.setPosition(0, oldImage.getHeight()+1)
    oldImage2.draw(win)
    col1 = 80
    col2 = 270
    row1 = 160
    row2 = 210

    # Used to show target region
    #BoxLocation(oldImage2, col1, row1, col2, row2)

    newImage2 = RemoveRedEyes(oldImage2, col1, row1, col2, row2)
    # show newImage to the right of oldImage
    newImage2.setPosition(newImage2.getWidth() + 1, oldImage.getHeight()+1)
    newImage2.draw(win)

    win.exitOnClick()
