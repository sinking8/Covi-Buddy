#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request, Response,json
from chatbot.chatbot import chatbot
import chatbot.ml_model as mod

import numpy as np
import os

# Open CV
import cv2
import cv2 as cv

from pyunpack import Archive

# Current Directory
CURR_DIR = os.getcwd()

# Unpacking Models
Archive(os.path.join(CURR_DIR,"covid_detector//saved_models","saved_models.rar")).extractall(os.path.join(CURR_DIR,"covid_detector//saved_models"))

## Covid Detector
from covid_detector.Covid_Detect import Covid_Detect
from covid_detector.Mask_Detect import Mask_Detect


# Calling Covid Models
mask_detect  = Mask_Detect()
covid_detector = Covid_Detect()

# Loading HaarCascadeClassifier
font = cv.FONT_HERSHEY_COMPLEX
haar_data = cv.CascadeClassifier('covid_detector//Haarcascades//haarcascade_frontalface_default.xml')

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
camera=cv2.VideoCapture(0)
app.config.from_object('config')


@app.route('/',methods=['GET'])
def home():
    return render_template('pages/Covibuddy.html')



#USER PAGE
@app.route('/user',methods=['GET','POST'])
def user():
	return render_template('pages/chatbot.html')

@app.route('/quiz_sol',methods=['POST','GET'])
def quiz_sol():
    record = [
        request.form.get('fever'),
        request.form.get('tiredness'),
        request.form.get('dry_cough'),
        request.form.get('breathing_d'),
        request.form.get('sore_throat'),
        request.form.get('none'),
        request.form.get('body_pains'),
        request.form.get('nasal_c'),
        request.form.get('runny_nose'),
        request.form.get('diarrhea'),
        request.form.get('none'),
        request.form.get('age_0_9'),
        request.form.get('age_10_19'),
        request.form.get('age_20_24'),
        request.form.get('age_25_59'),
        request.form.get('age_60'),
        request.form.get('gender_female'),
        request.form.get('gender_male'),
        request.form.get('contact_not_sure'),
        request.form.get('contact_yes'),
        request.form.get('contact_no')
    ] 

    record = [int(rec) for rec in record]  

    response=covid_detector.predict(record)
    return json.dumps(response)

@app.route('/quiz',methods=['POST','GET'])
def quiz_page():
    return(render_template('pages/Quizpage.html'))


@app.route('/mask_detector')
def mask_detector():
    print("mask detector")
    return render_template('pages/webcam.html')


@app.route('/covid_api')
def covid_api():
    print("covid_api")
    return render_template('pages/API.html')

@app.route("/get")
def get_bot_response():
	model = mod.Mlmodel()
	sympts_data = np.reshape(np.zeros(132),(1,132))
	class_names = list(model.return_symp_names())
	dis = ''
	user = request.args.get('text')
    
	if(request.args.get('medi') == 'y'):
		if(user in class_names):
				sympts_data[0][class_names.index(user)] =1
				dis = model.test_model(sympts_data)
				return("You might have "+dis)

		elif(user == ''):
			return('Type something..')

		else:
			return("Sorry couldn't find")

	elif(request.args.get('medi') == 'n'):
		resp = str(chatbot.get_response(user))
		if(resp == 'Do you feel?'):return '' 
		return str(chatbot.get_response(user))

	else:
		return('I am sorry, but I do not understand. I am still learning.')




def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            
            faces = haar_data.detectMultiScale(frame)
            for x,y,w,h in faces[:1]:
                if(w>200 or h>200):
                    
                    face = frame[y:y+h, x:x+w, :]
                    face = cv.resize(face, (50,50))
                    face = face.reshape(1,-1)
                    
                    response = mask_detect.detect_mask(face)["response"]
                    cv.putText(frame,response["result"], (x,y), font, 1, (244,250,250), 2)
                    cv.rectangle(frame, (x,y), (x+w, y+h),response["color_code"], 4)
            cv.imshow('Result', frame)


            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video')
def video():
    print("video")
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')



#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run(debug=True)
    camera=cv2.VideoCapture(0)
