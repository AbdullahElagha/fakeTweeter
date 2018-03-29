from __future__ import print_function
import os, sys
from PIL import Image, ImageOps, ImageDraw, ImageFont

def generateTweetBody():


    textInput = input("Enter the text you wish to display on the tweet")

    print(textInput)

    tweetBody = Image.open("blankBodyTweet.jpg")

    # set the font and size
    fnt = ImageFont.truetype("/Users/aelagha/Programs/fakeTweeter/helveticaneue/HelveticaNeue Light.ttf", 25)


    d = ImageDraw.Draw(tweetBody)
    d.text((100, 100), textInput, font=fnt, fill=(0, 0, 0))

    tweetBody.save('pil_text.png')



generateTweetBody()


