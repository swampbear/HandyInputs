from hand_estimation import HandEstimation
import cv2 as cv
import time
import keyboard

class PresentationClicker():

    def __init__(self):
        self.detector = HandEstimation()
        self.cap = cv.VideoCapture(0)
    
    def run(self):
        gesture_start_time = None
        current_gesture = None
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            frame = self.detector.findFingers(frame)
            lmsList, bbox = self.detector.findPosition(frame)

            if len(lmsList) != 0:
                fingers = self.detector.findFingerUp()
                if fingers[1] == 1 and fingers[2] ==1 and sum(fingers) == 2:
                    if current_gesture != 'right':
                        gesture_start_time = time.time()
                        current_gesture = 'right'
                    elif gesture_start_time and time.time() - gesture_start_time > 0.3:
                        keyboard.press_and_release('right')
                        gesture_start_time = None
                elif fingers[0] == 1 and fingers[1] == 1 and sum(fingers) == 2:
                    if current_gesture != 'left':
                        gesture_start_time = time.time()
                        current_gesture = 'left'
                    elif gesture_start_time and time.time() - gesture_start_time > 0.3:
                        keyboard.press_and_release('left')
                        gesture_start_time = None
                else:
                    current_gesture = None
                    gesture_start_time = None

            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img = cv.resize(img, (640, 480))

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()

if __name__ == "__main__":
    pc = PresentationClicker()
    pc.run()