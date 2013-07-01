# The following code uses the FaceRecognizerModel class to train a LBPH model.
# It updates the models and provide faces to compare against those in the model.
# It outputs the prediction and a validation result

import os
import sys
import cv2
import numpy as np
import FaceRecognizerModel as frm
from sklearn.metrics import precision_score

recognizer = frm.FaceRecognizerModel() # Create Face Recognizer Model
user = 0 # Keeps track of the number of faces
name_label_dict = {}# Keeps track of the label with a given name
image_array = [] # Setup an array
users = []
label = []

def train_with_file(filename, nameface):
    global user
    try:
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE) # Load image                
        image_array.append(np.asarray(image, dtype = np.uint8)) # Add image to array as a numpy array
        
        user = user+1
        name_label_dict[user] = nameface
        users.append(user)
        # Create label as 4 byte int. 
        # Facerecognizer takes arrays as labels hence set up as a numpy array
        # In this instance label gains a new and different member 
        label = np.asarray(users, dtype=np.int32)
        
        recognizer.train(image_array, label) # Send face and label to dataset
    except TypeError:
        print "Error reading file! Check filename!"
        
def train_with_folder(folderlocation, nameface):

    for filename in os.listdir(folderlocation):
        try:
            print filename
            image = cv2.imread(os.path.join(folderlocation, filename), cv2.IMREAD_GRAYSCALE) # Load image                
            image_array.append(np.asarray(image, dtype = np.uint8)) # Add image to array as a numpy array
            user = user+1
            name_label_dict[user] = nameface
            users.append(user)
            
            
        except IOError, (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
        except TypeError:
            print "Error reading file! Check filename!"
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
                
            
            label = np.asarray(users, dtype=np.int32)
                
            recognizer.train(image_array, label) # Send face and label to dataset
            
        
def recognize_face(filename):
            
    try:
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE) # Load image
        
        prediction = recognizer.predict(image)
                        
        # prediction_accuracy = accuracy(image, image_array[int(prediction[0])-1])
        
        name = name_label_dict[int(prediction[0])]
        distance = prediction[1]
        
        # print distance
        
        if distance <= 50:
            return ("This is %s.\nDistance is %s.")%(name,distance)
            
        else:
            return "Image not recognized"
        
    except TypeError:
        print "Error reading file! Check filename!"
            
def check_faces():
    print name_label_dict

            
    
