import os 
import joblib


class Covid_Detect:
    
    # Directories for Model --> Change if subdirectories created
    CURR_DIR         = os.getcwd()
    saved_models_dir = "covid_detector/saved_models" 
    model_dir        = "covid_model.pkl"


    # Change Response Text
    
    response_text = {
        'Severity_Mild':"Your are affected by Covid mildly.",
        'Severity_Moderate': "You are affected by Covid Moderately",
        'Severity_Severe':"You are affected by Covid Severely",
        'Severity_None':"You are safe from Covid"
    }
    
    def __init__(self):
        
        self.clf = joblib.load(os.path.join(self.CURR_DIR,self.saved_models_dir,self.model_dir))
    
    def predict(self,X):

        try:
            label = self.clf.predict([X])[0]
            
        except:
            return {"response":"","status":'OK'}
        
        else:
            return {"response":self.response_text[label],"status":'OK'}
        
    def save_model(self):pass