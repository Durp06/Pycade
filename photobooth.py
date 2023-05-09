import cv2

webcam_port = 0
cam = VideoCapture(webcam_port) #initializes cam as default webcam for computer

result = cam.read()
image = cam.read()

if result:
        imshow ("Photobooth", image)
        imwrite("Photobooth.png", image)

        waitKey(0)
        destroyWindow("Photobooth")

else:
    print("No image detected! Try again")


#https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/