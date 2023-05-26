import cv2
from datetime import datetime
import os



counter = 0
directory = os.getcwd()

webcam = cv2.VideoCapture(0)

destination_folder = f"{directory}\\photobooth-images"

while webcam.isOpened():
    success, img = webcam.read()

    if cv2.waitKey(1) == ord("e"):
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"Photobooth_{current_time}.png"
        cv2.imwrite(os.path.join(destination_folder, filename), img)

    cv2.imshow("Photobooth", img)
    if cv2.waitKey(0) == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()