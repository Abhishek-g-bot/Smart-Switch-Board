from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__,template_folder='template')

cred = credentials.Certificate("C:/Users/GAIKAR/Desktop/Desktop/api/smartswitchboard2022.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartswitchboard2022-default-rtdb.firebaseio.com'
})

# Get a reference to the database nodes
ref_Relay1 = db.reference('Relay1Status')
ref_Relay2 = db.reference('Relay2Status')
ref_Relay3 = db.reference('Relay3Status')
ref_Relay4 = db.reference('Relay4Status')
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
def count_fingers(lm_list):
    fingers = []

    # Thumb
    if lm_list[4][1] > lm_list[3][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Index finger
    if lm_list[8][2] < lm_list[6][2]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Middle finger
    if lm_list[12][2] < lm_list[10][2]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Ring finger
    if lm_list[16][2] < lm_list[14][2]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Little finger
    if lm_list[20][2] < lm_list[18][2]:
        fingers.append(1)
    else:
        fingers.append(0)

    return fingers

def detect_hands(frame):
    with mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        # Convert the image to RGB and process it with MediaPipe Hands
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Check if hands were detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                lm_list = []
                for lm in hand_landmarks.landmark:
                    lm_list.append([lm.x, lm.y, lm.z])
                fingers = count_fingers(lm_list)
                yield fingers

def gen_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()

        if not success:
            break

        # Flip the image horizontally for a more intuitive mirror view
        frame = cv2.flip(frame, 1)

        # Detect hands and count fingers
        fingers_list = list(detect_hands(frame))

        # Calculate the total number of fingers up for both hands
        total_fingers = sum([sum(fingers) for fingers in fingers_list])
        count=total_fingers
        if count==10:
            ref_Relay1.set(0)
            ref_Relay2.set(0)
            ref_Relay3.set(0)
            ref_Relay4.set(0)
        if count==1:
            ref_Relay1.set(True)
        if count==2:
            ref_Relay2.set(True)
        if count==3:
            ref_Relay3.set(True)
        if count==3:
            ref_Relay4.set(True)
        if count==4:
            ref_Relay1.set(True)
            ref_Relay2.set(True)
            ref_Relay3.set(True)
            ref_Relay4.set(True)
        if count==5:
            pass
        if count==6:
            pass
        if count==7:
            pass
        if count==8:
            pass
        if count==9:
            pass
        if count==10:
            pass
        # Draw the finger count on the frame
        cv2.putText(frame, f'Fingers: {total_fingers}', (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display the frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()
'''bbox = hand["bbox"]
                cvzone.cornerRect(frame, bbox, 20, 1, rt=0)
                for lm in lmList:
                    x, y = lm[1], lm[2]
                    cv2.circle(frame, (x, y), 8, (0, 255, 0), cv2.FILLED)
                fingers = detector.fingersUp(hand)
                counts = fingers.count(1)
                cv2.putText(frame, f"{counts}", (bbox[0]+100, bbox[1]+100), 
                    cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
                count=counts'''

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect')
def detect():
    return render_template('detect.html')
if __name__ == '__main__':
    app.run(debug=True)
