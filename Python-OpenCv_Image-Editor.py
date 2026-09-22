import cv2 as cv
import os 
import tkinter as tk
from tkinter import filedialog

#image load function mainmenu 1 
def opendImage():
    print("Select image :  ")
    image_path = filedialog.askopenfilename(
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
    )
    image=cv.imread(image_path)
    if image is None:
        print("Error in loading file")
        return None,None
    print("showing image ......")
    cv.imshow("Selected image \n", image)
    print(".....press any key to close the image ....")
    
    cv.waitKey(0)
    cv.destroyAllWindows()
    return image ,image_path
    

# show image function menu 1 
def imageFunction(image,image_path):
    
    filename=os.path.basename(image_path)
    print("\n")
    print ("========== Image Information ==========")
    print ("File Path       :   ",image_path)
    print ("File Name       :   ",filename)
    print(".........................................")
    print ("File Width      :   ",image.shape[1],"pixels")
    print ("File Height     :   ",image.shape[0],"pixels")
    print(".........................................")
    print ("File Channels   :   ",image.shape[2])
    print ("Image Size      :   ",image.shape)
    print(".........................................")
    print ("Data Type       :   ",image.dtype)
    print ("Image Pixels    :   ",image.size)
    print(".........................................")
    
    
# resize image menu 2

def resizeImage(image):
    original_image=image.copy()

    while True:
        print("\n Image size is ((height, width,channels): ",image.shape)
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))
        if width <= 0 or height <= 0:
            print("\nWidth and height must be greater than 0")
            continue
        resizedImage = cv.resize(image, (width, height))
        print("\nImage resized successfully.")
        print("\n Image size is ((height, width,channels): ",resizedImage.shape)
        print("\n press any key to close image ")
        cv.imshow("\nResized Image ", resizedImage)
        cv.waitKey(0)
        cv.destroyAllWindows()
        choice=int(input("1. save the current image \n2. For reset and resize the original image : "))
        if choice==1:
            return resizedImage
        elif choice==2:
            continue
        else:
            print("Invalid input ! Try again ")
            continue
        
#crop image menu3                  
def cropImage(image):

    original_image=image.copy()
    while True :
        
        print("\n Image size is ((height, width,channels): ", image.shape)

        print("Enter below details for crop ")

        height1 = int(input("Enter height(point of starting): "))
        height2 = int(input("Enter height(point of ending)  : "))
        width1 = int(input("Enter width (point of starting) : "))
        width2 = int(input("Enter width (point of ending)   : "))

        if height1 < 0 or height2 < 0 or width1 < 0 or width2 < 0:
            print("Values cannot be negative")
            continue

        if height2 > image.shape[0] or width2 > image.shape[1]:
            print("Crop points are outside the image")
            continue
        
        if height1 >= height2:
            print("Ending height must be greater than starting height")
            continue
        
        if width1 >= width2:
            print("Ending width must be greater than starting width")
            continue

        croppedImage = image[height1:height2, width1:width2]

        print("\nImage cropped successfully.")

        cv.imshow("Cropped Image", croppedImage)
        cv.waitKey(0)
        cv.destroyAllWindows()
        choice=int(input("1. save the current image \n2. For reset and crop from the original image : "))
        if choice==1:
            return croppedImage
        elif choice==2:
            continue
        else:
            print("Invalid input ! Try again ")
            continue
    
    
    
#save image menu4
def saveImage(image):

    save_path = filedialog.asksaveasfilename(
        title="Save Image",
        defaultextension=".jpg",
        filetypes=[
            ("JPG Image", "*.jpg"),
            ("PNG Image", "*.png"),
            ("All Files", "*.*")
        ]
    )

    if save_path == "":
        print("Save cancelled")
        return
    cv.imshow("current image for save ", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite(save_path, image)

    print("Image saved successfully.")
    print("Saved at:", save_path)
    
    
#features menu 
def menu(image,image_path):
    
        while True:
            print("========Menu========")
            print(""" 
    1. Show Image Information \n 
    2. Resize Image \n
    3. Crop Image \n
    4. Save Image \n
    0. Exit or select the image again  \n 
    """)

            choice=int(input("Enter your choice :"))
        
            if choice==1:
                imageFunction(image,image_path)
            elif choice==2:
                image=resizeImage(image)
            elif choice==3:
                
                cropImage(image)
            elif choice==4:
               saveImage(image)
            elif choice==0:
                print("Exiting ......and select the image again ")
                return 
            else:
                print("Invalid choice..... Try again ")
  


def mainMenu():

    while True:

        print("1. Select image and continue")
        print("0. Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            image, image_path = opendImage()

            if image is None:
                continue

            menu(image, image_path)

        elif choice == 0:
            print("Exiting.....")
            break

        else:
            print("Invalid input! Try again")
        
        
if __name__=="__main__":
    mainMenu()