#import the necessary librairies
import cv2 
import cv  
import numpy as np
import Image
import pygame
from SimpleCV import *
import time
import pyttsx

#initiate the text-to-speech synthesizer
engine = pyttsx.init()

#initiate the in-built camera
cam=Camera()
while True:
    # slow down the run-time of the program
    time.sleep(0.1)

    # read image
    img = cam.getImage()

    #binarize the image
    img=img.binarize()

    #save the new binarized image
    img.save("C:/Users/ash-rob-12-computer/Desktop/Sharon/img.png")

    #check whether an image was taken. frame == None if no image was taken
    frame = cv2.cv.RetrieveFrame(cam.capture)
    print (frame)

    #read the saved image
    image=cv2.imread('img.png')

    #obtain the height and width of the image
    height, width,channels = image.shape
    print ("Height and width of image : " + str(height) + " " + str(width))


    # opens a SimpleCV window displaying the binarized image
    img.show()

    #find obstacles
    blobs=img.findBlobs()

    #returns the centres of the all the obstacles
    x =blobs.center()

    #prints the centre coordinates of the largest obstacle
    print(x[-1])
    area= blobs.sortArea()

    #prints the area of the largest obstacle
    print(area[-1])
    
    #stores the x and y coordinate of the largest obstacle
    x_coordinate = x[-1][0]	# x coordinate of middle of largest obstacle
    y_coordinate=  x[-1][1]	# y coordinate of middle of largest obstacle
    w = area[-1].width()	# width of largest obstacle
    h = area[-1].height()	# height of largest obstacle
        
    print("Found " + str(len(blobs)) + " obstacles.")
    print("  Largest is at (" + str(x_coordinate) + "," + str(y_coordinate) + ")" +
  		    " with width " + str(w) + " pixels" +
    		  " and height " + str(h) + " pixels")
    if ((x_coordinate < width/2 - w/2).any()):
   	  print("  Object is to your left so move right.")
   	  engine.say("Take one step sixty degrees to your right side")
   	  engine.runAndWait()
    elif ((x_coordinate > width/2 + w/2).any()):
   	  print("  Object is to your right so move left.")
   	  engine.say("Take one step sixty degrees to your left side")
   	  engine.runAndWait()
    else:
      print("  Object is approximatley in front of you so move left or right.")
      engine.say("Take one step sixty degrees to your left or right")
      engine.runAndWait()
