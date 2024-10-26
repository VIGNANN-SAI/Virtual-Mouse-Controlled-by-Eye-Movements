# Eye Contolled Mouse
This program uses OpenCV, Mediapipe, and Pyautogui libraries to control the mouse cursor
using eye movements.
## Imports Packages
import cv2
import mediapipe as mp
import pyautogui
## Initialize Video Capture
cam = cv2.VideoCapture(0)
## Initialize Face Mesh Detection
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
## Get Screen Width and Height
screen_w, screen_h = pyautogui.size()
## Set Camera Resolution to 480p
def make_480p():
 cam.set(3, 854)
 cam.set(4, 480)
make_480p()
## Main Loop
while True:
 _, frame = cam.read()
 frame = cv2.flip(frame, 1)
 rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 output = face_mesh.process(rgb_frame)
 landmark_points = output.multi_face_landmarks
 frame_h, frame_w, _ = frame.shape
## Eye Tracking
 if landmark_points:
 landmarks = landmark_points[0].landmark
 for id, landmark in enumerate(landmarks[474:478]):
 x = int(landmark.x * frame_w)
 y = int(landmark.y * frame_h)
 cv2.circle(frame, (x, y), 3, (0, 255, 0))
 if id == 1:
 screen_x = screen_w * landmark.x
 screen_y = screen_h * landmark.y
 pyautogui.moveTo(screen_x, screen_y)
 left = [landmarks[145], landmarks[159]]
 right=[landmarks[145], landmarks[159]]
### Left Eye
 for landmark in left:
 x = int(landmark.x * frame_w)
 y = int(landmark.y * frame_h)
 cv2.circle(frame, (x, y), 3, (0, 255, 255))
 if (left[0].y - left[1].y) < 0.004:
 pyautogui.click()
### Right Eye
 for landmark in right:
 x = int(landmark.x * frame_w)
 y = int(landmark.y * frame_h)
 cv2.circle(frame, (x, y), 3, (0, 255, 255))
 if (right[0].y - right[1].y) < 0.004:
 pyautogui.click()
## Display Frame
 cv2.imshow('Eye Controlled Mouse', frame)
 cv2.waitKey(1)