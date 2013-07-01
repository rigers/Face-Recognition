# The following class creates a FaceRecognizer model. Specifically a Local Binary Pattern Histrogram(LBPH).
# The LBPH model is designed to be used with smaller databases (images per person). It also has the advantage to be more
# robust against lightining variations. Also it's not neccessary to resize images and the dataset can be updated without retraining 
# the entire model.

import cv2
import numpy as np

class FaceRecognizerModel():

    def __init__(self):
        # Create a new LBPH model using the default parameters.
        self.model = cv2.createLBPHFaceRecognizer()

    # Initial training. Doing this empties entire dataset
    # train(image array, 4 byte int)
    def train(self, image_array, label):
        self.model.train(image_array, label)
    
    # Compare a face against faces uploaded
    # predict(image array)
    def predict(self, image_array):
        return self.model.predict(image_array)
        
    
    # Add additional faces to the dataset while preserving the old model
    # update(image array, 4 byte int)
    def update(self, image_array, label):
        self.model.update(image_array, label)