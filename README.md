# HandyInputs
A repo containing small programs built for using hand gestures as a substitute for keyboard inputs

## Sources
The class in the hand_estimation.py is retrieved from the following Medium article: [Hand Detection Tracking in Python using OpenCV and MediaPipe](https://gautamaditee.medium.com/hand-recognition-using-opencv-a7b109941c88)

## Setup repo localy
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/HandyInputs.git
   cd HandyInputs
   ```
2. Create and activate viritual environtment
   ```bash
   python3 -m venv <myenvname>
   ```
3. Activate environtment
   ```bash
   source myvenvname/bin/activate
   ```
   
5. **Install Dependencies**:
   - Ensure you have Python 3.7+ and install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Presentation_clicker
The `Presentation_clicker` class allows users to control presentation slides using hand gestures. It leverages computer vision to detect specific gestures and translates them into keyboard inputs, enabling seamless navigation through slides without physical contact with a keyboard or mouse.

### Run following command in terminal to run the presentationclicker
```bash
python3 presentation_clicker.py
```
### Interactions
#### Forward
Show a "peace" sign with your index and middlefinger for 0.3 seconds or longer, this wil trigger one right arrow click
#### Backard
Lift your index finger and thumb together in 0.3 seconds or longer, this will triger one left arrow click

