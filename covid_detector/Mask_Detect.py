import os
import joblib
import cv2 as cv

#from pyunpack import Archive

class Mask_Detect:
    
    CURR_DIR  = os.getcwd()
    model_dir = "covid_detector//saved_models//Cringans.pkl"
    harr_data_dir = "haarcascade_frontalface_default.xml"
    
    Colour_Code = {0: (0,255,0), 1: (0,0,255)}
    names = {0 : 'Is wearing a Mask', 1 : 'Is not wearing a Mask'}

    def __init__(self):   
        self.model     = joblib.load(os.path.join(self.CURR_DIR,self.model_dir))
        
    def detect_mask(self,X):
        
        try:
            prediction = self.model.predict(X)[0]
            n = self.names[int(prediction)]

        except:
            return({"response":{"result":"","color_code":(),"status":False}})
        
        else:
            return({"response":{"result":n,"color_code":self.Colour_Code[int(prediction)],"status":True}})
        
    def train_model(self):pass