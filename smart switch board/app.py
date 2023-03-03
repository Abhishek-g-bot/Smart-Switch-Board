from flask import Flask, render_template, Response
import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import numpy as np
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__,template_folder='template')

cred = credentials.Certificate("C:/Users/GAIKAR/Desktop/Desktop/smart switch board/smart-switch-board-60ec6-firebase-adminsdk-et2mj-e7df50efd1.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-switch-board-60ec6-default-rtdb.firebaseio.com/'
})

# Get a reference to the database nodes
ref_led1 = db.reference('Led1Status')
ref_led2 = db.reference('Led2Status')
ref_led3 = db.reference('Led3Status')
ref_led4 = db.reference('Led4Status')
detector = HandDetector(maxHands=1, detectionCon=0.8)

def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = cv2.flip(frame, 1)
            hand = detector.findHands(frame, draw=False)
            if hand:
                lmlist = hand[0]
                if lmlist:
                    fingerup = detector.fingersUp(lmlist)
                    if fingerup == [0, 0, 0, 0, 0]:
                        ref_led1.set(0)
                        ref_led2.set(0)
                        ref_led3.set(0)
                        ref_led4.set(0)
                    if fingerup == [0, 1, 0, 0, 0]:
                        ref_led1.set(True)
                    if fingerup == [0, 1, 1, 0, 0]:
                        ref_led2.set(True)
                    if fingerup == [0, 1, 1, 1, 0]:
                        ref_led3.set(True)
                    if fingerup == [0, 1, 1, 1, 1]:
                        ref_led4.set(True)
                    if fingerup == [1, 1, 1, 1, 1]:
                        ref_led1.set(True)
                        ref_led2.set(True)
                        ref_led3.set(True)
                        ref_led4.set(True)
                    #else:
                    #    ref_led1.set(False)
                    #    ref_led2.set(False)
                    #    ref_led3.set(False)
                    #    ref_led4.set(False)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
        # yield the resulting frame as a response to the client
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    

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