from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

class Predictor:

    def preprocess_image(self, image_path):
        img = image.load_img(image_path, target_size=(224, 224))  # replace with the size of your images
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.  # if you normalized images during training
        return img_array
    
    def predict_image_class(self,image_path):
        preprocessed_image = self.preprocess_image(image_path)
        prediction = self.predictorModel.predict(preprocessed_image)
        return np.argmax(prediction)  # returns the class index

    def predict(self, image) -> str:
        disaster = self.predict_image_class(image)
        return self.disasters[disaster]

    def __init__(self, predictorModel) -> None:
        print("Predictor Model Loaded, using ", predictorModel, " as model.")
        self.disasters = {
            0: "Cyclone",
            1: "EarthQuake",
            2: "Flood",
            3: "Tsunami",
        }
        self.predictorModel = load_model(predictorModel)