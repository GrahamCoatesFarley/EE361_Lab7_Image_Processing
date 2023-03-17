from cImage import *
from doubleimage import *
from edgedetection import *
from grayscale import *
from halfimage import *
from horizonalflip import *
from negative import *
from pixelmapping import *
from verticalflip import *

if __name__ == '__main__':
    # Part 1 #########################################################
    win = ImageWin("cImage Demo",800,500) # redEyes.gif is 395x489
    oldImage1 = FileImage('redEyes.gif')
    print(oldImage1.getWidth(), oldImage1.getHeight())
    oldImage1.draw(win)

    #newImage is the negative of oldImage
    newImage1 = EmptyImage(oldImage1.getWidth(),oldImage1.getHeight())
    for row in range(newImage1.getHeight()):
        for col in range(newImage1.getWidth()):
            if(row == 0 or row == newImage1.getHeight()-2): # catches the top and bottom of image to add boarder
                v = oldImage1.getPixel(col, row)
                v.red = 255
                v.green = 0
                v.blue = 0
                newImage1.setPixel(col, row, v)
            elif(col == 0 or col == newImage1.getWidth()-1): # catches sides
                v = oldImage1.getPixel(col, row)
                v.red = 255
                v.green = 0
                v.blue = 0
                newImage1.setPixel(col, row, v)

            else: # default run
                v = oldImage1.getPixel(col,row)
                v.red = 255 - v.red
                v.green = 255 - v.green
                v.blue = 255 - v.blue
                newImage1.setPixel(col,row,v)
    #show newImage to the right of oldImage
    newImage1.setPosition(newImage1.getWidth()+1,10)
    newImage1.draw(win)


    newImage1.save('redEyes-inverted.gif')
    #print(newImage.toList())
    win.exitOnClick()

    # Part 2 #########################################################
    win = ImageWin("Part II Flip Demo", 800, 500)  # redEyes.gif is 395x489
    oldImage2 = FileImage('redEyes.gif')
    print(oldImage2.getWidth(), oldImage2.getHeight())
    oldImage2.draw(win)

    #Flip
    newImage2_flip = verticalFlip(oldImage2)
    newImage2_flip.setPosition(newImage2_flip.getWidth() + 1, 0)
    newImage2_flip.draw(win)

    newImage2_flip.save('redEyes-flip.gif')
    #print(newImage.toList())
    win.exitOnClick()

    #Edge Detect
    win = ImageWin("Part II Edge Detect Demo", 800, 500)  # redEyes.gif is 395x489
    print(oldImage2.getWidth(), oldImage2.getHeight())
    oldImage2.draw(win)

    newImage2_edge = edgeDetect(oldImage2)
    # show newImage to the right of oldImage
    newImage2_edge.setPosition(newImage2_edge.getWidth() +1, 0)
    newImage2_edge.draw(win)

    newImage2_flip.save('redEyes-Edge-Detect.gif')
    # print(newImage.toList())
    win.exitOnClick()

    #Negeative
    win = ImageWin("Part II Negative Demo", 800, 500)  # redEyes.gif is 395x489
    print(oldImage2.getWidth(), oldImage2.getHeight())
    oldImage2.draw(win)

    newImage2_neg = makeNegative(oldImage2)
    newImage2_neg.setPosition(newImage2_neg.getWidth() + 1, 0)
    newImage2_neg.draw(win)

    # newImage2_neg.save('redEyes-neg.gif')
    # print(newImage.toList())
    win.exitOnClick()

    #Double
    win = ImageWin("Part II double Demo", 1200, 1000)  # redEyes.gif is 395x489
    print(oldImage2.getWidth(), oldImage2.getHeight())
    oldImage2.draw(win)

    newImage2_doub = doubleImage(oldImage2)
    newImage2_doub.setPosition(oldImage2.getWidth() + 1, 0)
    newImage2_doub.draw(win)

    newImage2_doub.save('redEyes-double.gif')
    # print(newImage.toList())
    win.exitOnClick()

    # Part 3 #########################################################

    win = ImageWin("Half Image Demo", 800, 400)  # castle.gif is 480x360
    oldImage3 = FileImage('castle.gif')
    print(oldImage3.getWidth(), oldImage3.getHeight())

    oldImage3.draw(win)

    # Makes a half image
    newImage3 = halfImage(oldImage3)

    # show newImage to the right of oldImage
    newImage3.setPosition(oldImage3.getWidth() + 1, 0)
    newImage3.draw(win)

    # obtain coordiates of left eye
    #print(win.getMouse())
    #print(win.getMouse())

    newImage3.save('castle_flip.gif')
    # print(newImage.toList())

    win.exitOnClick()

    # Part 4 #########################################################

    win = ImageWin("horizontal flip Demo", 1000, 400)  # castle.gif is 480x360
    oldImage4 = FileImage('castle.gif')
    print(oldImage4.getWidth(), oldImage4.getHeight())

    oldImage4.draw(win)

    # Makes a half image
    newImage4 = HorizonalflipFlip(oldImage4)

    # show newImage to the right of oldImage
    newImage4.setPosition(oldImage4.getWidth() + 1, 0)
    newImage4.draw(win)

    # obtain coordiates of left eye
    #print(win.getMouse())
    #print(win.getMouse())

    newImage4.save('castle_Hflip.gif')
    # print(newImage.toList())

    win.exitOnClick()