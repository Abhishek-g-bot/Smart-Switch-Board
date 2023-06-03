from flask import Flask, render_template, Response
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__,template_folder='template')

cred = credentials.Certificate("C:/Users/GAIKAR/Desktop/BE/smartswitchboard2022.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartswitchboard2022-default-rtdb.firebaseio.com'
})

ref_Relay1 = db.reference('Relay1Status')
ref_Relay2 = db.reference('Relay2Status')
ref_Relay3 = db.reference('Relay3Status')
ref_Relay4 = db.reference('Relay4Status')
ref_Relay5 = db.reference('Relay5Status')
ref_Relay6 = db.reference('Relay6Status')
ref_Relay7 = db.reference('Relay7Status')
ref_Relay8 = db.reference('Relay8Status')
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
                        ref_Relay1.set(0)
                        ref_Relay2.set(0)
                        ref_Relay3.set(0)
                        ref_Relay4.set(0)
                        ref_Relay5.set(0)
                        ref_Relay6.set(0)
                        ref_Relay7.set(0)
                        ref_Relay8.set(0)
                    if fingerup == [0, 1, 0, 0, 0]:
                        ref_Relay1.set(1)
                    if fingerup == [0, 1, 1, 0, 0]:
                        ref_Relay2.set(1)
                    if fingerup == [0, 1, 1, 1, 0]:
                        ref_Relay3.set(1)
                    if fingerup == [0, 1, 1, 1, 1]:
                        ref_Relay4.set(1)
                    if fingerup == [1, 0, 0, 0, 0]:
                        ref_Relay5.set(1)
                    if fingerup == [0, 0, 1, 0, 0]:
                        ref_Relay6.set(1)
                    if fingerup == [0, 0, 0, 1, 0]:
                        ref_Relay7.set(1)
                    if fingerup == [0, 0, 0, 0, 1]:
                        ref_Relay8.set(1)
                    if fingerup == [1, 1, 1, 1, 1]:
                        ref_Relay1.set(1)
                        ref_Relay2.set(1)
                        ref_Relay3.set(1)
                        ref_Relay4.set(1)
                        ref_Relay5.set(1)
                        ref_Relay6.set(1)
                        ref_Relay7.set(1)
                        ref_Relay8.set(1)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
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
    app.run(host='0.0.0.0',debug=True)
