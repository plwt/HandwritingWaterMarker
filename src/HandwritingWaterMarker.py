# install required packages
from PIL import Image, ImageDraw, ImageFont
import os
import sys
from pathlib import Path
import pywhatkit as kit
import cv2


# Welcome message
def welcome():
    print("""
    Welcome to HandwritingWaterMarker
    """)

welcome()


# Make watermark image
def make_watermark():

    # set width and height of watermark
    width = 512
    height = 512
    
    # set the message to be watermarked
    message = input("Enter your watermark message (one word is best): ")
    
    # create watermark
    kit.text_to_handwriting(message, save_to="watermark.png")
    img = cv2.imread("watermark.png")
    
    # make the watermark
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
      
    # save the watermark
    img.save('/opt/HandwritingWaterMarker/src/watermark.png')

make_watermark()


# Watermark the image
def watermarker():
    # Ask the user to confirm the image has been saved
    Gonogo=input("Have you saved the file to be watermarked to the the WaterMarker folder in your user documents with filename image.png?(y/n)")
    
    if Gonogo=="n":
        print("Please save the image to be watermarked to the WaterMarker folder in your user documents with the filename image.jpg and run WaterMarker again.")
          

    elif Gonogo=="y":
        
        # Open the original image and save it as temporary.png
        from pathlib import Path
        home_path = str(Path.home())
        words=Image.open(home_path + '/WaterMarker/image.jpg')
        words.save("/opt/HandwritingWaterMarker/images/temp.png")
        
        # Open the temporary .png, set alpha and get image size
        words=Image.open("/opt/HandwritingWaterMarker/images/temp.png")
        words.putalpha(225)
        hmat,wmat = words.size
        
        # Open the watermark and resize it to the size of the original image
        mask=Image.open('/opt/HandwritingWaterMarker/src/watermark.png')
        mask.putalpha(255)
        complete=mask.resize((hmat,wmat))
        
        # Open the temporary .png and paste the watermark on top of it
        complete.paste(words,box=(0,0),mask=words)
        
        # Save the watermarked image to the WaterMarker folder
        complete.save(home_path + '/HandwritingWaterMarker/watermarkedimage.png')
        
        # Remove the temporary .png
        path = "/opt/HandwritingWaterMarker/images/temp.png"
        os.remove("/opt/HandwritingWaterMarker/images/temp.png")
        
        # Confirm the watermarked image has been saved
        print("Your watermarked file has been saved to the WaterMarker folder in your user documents with the filename watermarkedimage.png.  Thank you for using HandwritingWaterMarker")
    else:
        print("Please try again.")

watermarker()
