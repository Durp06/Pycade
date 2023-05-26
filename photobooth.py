import cv2
import numpy as np
from datetime import datetime
import os

counter = 0
directory = os.getcwd()

webcam = cv2.VideoCapture(0)

destination_folder = f"{directory}\\photobooth-images"

flash_duration = 1.2 

flash_start_time = None
show_flash = False

while webcam.isOpened():
    success, img = webcam.read()

    if cv2.waitKey(1) == ord("e"):
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"Photobooth_{current_time}.png"
        cv2.imwrite(os.path.join(destination_folder, filename), img)
        
        flash_start_time = datetime.now()
        show_flash = True
    
    text = "Press 'e' to take a photo, 'q' to quit"
    cv2.putText(img, text, (100, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 215, 255), 2)
    
    # flash
    if show_flash:
        if (datetime.now() - flash_start_time).total_seconds() < flash_duration:
            flash_frame = np.ones_like(img) * 255
            cv2.imshow("Photobooth", flash_frame)
            cv2.waitKey(1)  
        else:
            show_flash = False
    
    cv2.imshow("Photobooth", img)
    

    if cv2.waitKey(1) == ord("q"):
        break
    
webcam.release()
cv2.destroyAllWindows()
