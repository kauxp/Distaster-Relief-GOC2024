from Model.Predictor import Predictor


def predictDisaster(image):
    model = Predictor("./Model/disasterDetector.h5")
    return model.predict(image)