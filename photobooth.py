import cv2
import mediapipe as mp
from datetime import datetime
import os

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

counter = 0
directory = os.getcwd()

webcam = cv2.VideoCapture(0)

destination_folder = f"{directory}\\photobooth-images"

while webcam.isOpened():
    success, img = webcam.read()

    if cv2.waitKey(1) == ord("e"):
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"Photobooth_{counter}_{current_time}.png"
        #file_path = os.path.join(destination_folder, filename)
        #cv2.imwrite(filename, img)
        cv2.imwrite(os.path.join(destination_folder, filename), img)
        counter += 1

    cv2.imshow("Photobooth", img)
    if cv2.waitKey(1) == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()