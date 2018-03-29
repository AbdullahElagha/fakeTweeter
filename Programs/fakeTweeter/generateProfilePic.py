from __future__ import print_function
import os, sys
from PIL import Image, ImageOps, ImageDraw

def generateProfilePic():

    transposeCircle = Image.open("transposeCircleBig.jpg")

    picInput = input("Enter the name of the file: ")
    print(picInput)

    tonyStark = Image.open(picInput)

    print("Cropping image....")


    print(transposeCircle.format, transposeCircle.size, transposeCircle.mode)
    print(tonyStark.format, tonyStark.size, tonyStark.mode)

    xCord = transposeCircle.size[0]
    yCord = transposeCircle.size[1]

    print(xCord)

    box = (0, 0, 500, 500)

    tonyStarkResize = tonyStark.resize((153, 153))
    tonyStarkCrop = tonyStarkResize.crop(box)

    tonyStarkCrop.save("tonyStarkCrop.jpg", 'jpeg')
    tonyStarkResize.save("tonyStarkResize.jpg", 'jpeg')

    tonyStarkResize.paste(transposeCircle, (0,0))
    tonyStarkResize.save("tonyStarkProfilePic.jpg", 'jpeg')

    mask = Image.open('transposeCircleBig.jpg').convert('L')
    im = Image.open('tonyStark.jpg')
    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('output.png')

    im = Image.open('output.png')
    im = im.resize((153, 153));
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    im.putalpha(mask)

    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('output2.png')

    print("Image cropped and saved")

generateProfilePic()