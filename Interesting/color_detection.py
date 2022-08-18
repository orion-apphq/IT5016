import cv2
import numpy as np
import pandas as pd
import argparse

ap = argparse.ArgumentParser()                                      # I think this part is interesting, it allows you to set an arguement when starting
ap.add_argument('-i', '--image', required=True, help="Image Path")  # the program from the command line. The arguement it sets is '-i' or '-image' and is used
args = vars(ap.parse_args())                                        # to set the path of the image file that is displayed. When starting the program the 
img_path = args['image']                                            # command looks like this: python color_detection.py -i C:/<PATH_TO_IMAGE>

img = cv2.imread(img_path)        # This uses the cv2 module to read the img and save it into a variable img

# global variables are declared here, they are used later on in the program inside a function which is why they are declared globally
clicked = False # clicked is used to keep a record of if the image has been clicked
r = g = b = xpos = ypos = 0
# r is where the red value of the pixel that is clicked on is stored
# g is where the green value of the pixel is stored
# b is for the blue value
# xpos is used to save the position of the mouse cursor on the x axis
# ypos is used to save the position of the mouse cursor on the y axis

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"] // # defining a list that refers to the column names in the CSV file of color names and RGB values
csv = pd.read_csv('colors.csv', names=index, header=None) # uses the panda module to read the csv, passing in the index of column names and saving the data
                                                          # into the csv variable

#function to calculate minimum distance from all colors and get the most matching color
# tbh I think they could have used better variable names throughout this
def getColorName(R,G,B): # function getColorName has 3 params, R, G, and B
    minimum = 10000 # defines a minimum value that the "closeness" is compared to - d has to be below this for he color to be considered as a match
    for i in range(len(csv)): # loops through each row in the CSV and compares the RGB values that were passed in as params against the RGB values of 
                              # the row
        
        # I dont know what math is going on here
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"])) # the value of d represents how close the passed in RGB
                                                                                                   # values are to the RGB values of the colors in the row
        if(d<=minimum): # tests if d is less than the minimum value
            minimum = d # if it is, the new minimum becomes d, and any more color rows are tested against that
                        # this means that the minimum is constantly shrinking and is only changed if a color row is closer to the passed in color
            cname = csv.loc[i,"color_name"] # gets the color name of the row that beat the minimum and saved it 
    return cname # after looping through the entire csv, returns the name of the color that was the closest

#function to get x,y coordinates of mouse double click and the rgb values of the pixel that was clicked on
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: # this function gets called on click and double click so this if statement tests that the event triggeriing it was a
                                         # double click
        global b,g,r,xpos,ypos, clicked # brings the global variables we declared before into the scope of the function
        clicked = True # changes the value of clicked to true
        xpos = x # sets xpos to the value of x, where x is the position of the mouse on the x axis inside the image window
        ypos = y # sets ypos to the value of y, where y is the position of the mouse on the y axis inside the image window
        b,g,r = img[y,x] # the img var is a list containing lists containing lists where the color values of each pixel is saved 
                         # - img[y,x] searches through the y list by index then searches for the x value and returns the color values of that pixel as 
                         # type class
        b = int(b) # this sets the values to be of type int
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image') # this initializes a window called "image"
cv2.setMouseCallback('image',draw_function) # this initializes a callback to run the draw function everytime the window is clicked

while(1): # this while loop doesnt test for anything it will just keep running until break is called

    cv2.imshow("image",img) # this displays the image in the window
    if (clicked): # after a double click the draw_function sets clicked to true
   
        # .rectangle draws a rectangle in the window with params, (image, startpoint, endpoint, color, thickness) -1 fills entire rectangle with color
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1) # this draws a rectangle in the top right corner and colors it with the color that was clicked on

        # This creates a string that contiains the rgb values and the name of the color that was the closest match to the one that was clicked on 
        # and save it into the variable test
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA) # This displays the text over the rectangle that was drawn earlier

        #tests if the color is a lighter color
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA) # and displays the text as black if it is
            
        clicked=False

    #listens for the esc key being hit, and if it is, break loop
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows() # after loop is broken close all windows and end
