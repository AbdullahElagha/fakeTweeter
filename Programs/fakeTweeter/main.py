from __future__ import print_function
import os, sys
from PIL import Image, ImageOps, ImageDraw
import generateProfilePic
import generateTweetBody



# generateTweetBody
# generateProfilePic


def transposeProfilePic():

    body = Image.open("pil_text.png")
    pic = Image.open('output2.png')

    body.paste(pic, (0, 0), pic)
    body.show()



transposeProfilePic()


