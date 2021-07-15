import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

hand_detection = mp_hands.Hands
cap = cv2.VideoCapture(0)
while cap.isOpened():
     success, image = cap.read()
if not success:
    print("Ignorance empty camera frame.")


    image.flags.writeable = False
    results = mp_hands.process(image)
    image.flags.writeale = True
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    for landmark in results.detections:
        print(mp_hands.get_key_point(landmark,mp_hands.HandKeyPoint.INDEX_FINGER_TIP))
        mp_drawing.draw_detection(image,mp_hands.HandKeyPoint.INDEX_FINGER_TIP.value)
        print(results.detections)
        cv2.imshow('MediaPipe',image)
        if cv2.waitKey(10) & 0xff == ord('q'):

            break
    cap.release()
    cv2.destoryAllWindows()