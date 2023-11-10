import cv2
import mediapipe as mp
import pyautogui
cap=cv2.VideoCapture(0)
index_y=0
hand_detect=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width,screen_height=pyautogui.size()
while True:
    _,capvideo=cap.read()
    frame=cv2.flip(capvideo,1 )
    frame_height,frame_width,_ =frame.shape
    frame_rgba = cv2.cvtColor(capvideo, cv2.COLOR_BGR2RGB)
    output=hand_detect.process( frame_rgba)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(capvideo,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                print(x,y)
                if id == 8:
                    cv2.circle(img=capvideo, center=(x,y),radius=20,color=(0, 255, 255))
                    index_x=screen_width/frame_width*x
                    index_y = screen_height / frame_height * y
                    pyautogui.moveTo( index_x,  index_y)
                if id == 4:
                    cv2.circle(img=capvideo, center=(x, y), radius=20, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    print( 'outside',index_y-thumb_y)
                    if abs( thumb_y-index_y)<70:
                        pyautogui.click()
                        pyautogui.sleep(1)



    cv2.imshow('Virtual Mouse',capvideo)
    cv2.waitKey(1)