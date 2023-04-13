import tensorflow as tf
import numpy as np
from skimage import transform

brainTumorModel = tf.keras.models.load_model('models/brain_tumor/Brain_Cancer.h5')
stomachModel = tf.keras.models.load_model('models/stomach/dyed_lifted_pylorus_vs_esophagitis_99_5.h5', compile=False)


def load(image):
    np_image = image
    np_image = np.array(np_image).astype('float32') / 255
    np_image = transform.resize(np_image, (200, 200, 3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image


def load256(image):
    np_image = image
    np_image = np.array(np_image).astype('float32') / 255
    np_image = transform.resize(np_image, (256, 256, 3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image


class BrainCancerDetector:
    diseases = {0: 'glioma', 1: 'meningioma', 2: 'tumor'}

    def __init__(self):
        self.model = brainTumorModel

    def predict(self, image):
        loaded_image = tf.keras.utils.load_img(image)
        processed_image = load(loaded_image)
        prediction = self.model.predict(processed_image)
        disease_index = prediction.argmax()

        accuracy = (prediction[0][disease_index] / prediction[0].sum()) * 100.0
        return accuracy, disease_index


class StomachDiseaseDetector:
    diseases = {0: 'esophagitis', 1: 'Dyed lifted polyps'}

    def __init__(self):
        self.model = stomachModel

    def predict(self, image):
        loaded_image = tf.keras.utils.load_img(image)
        processed_image = load256(loaded_image)
        prediction = self.model.predict(processed_image)
        disease_index = prediction.argmax()

        accuracy = (prediction[0][disease_index] / prediction[0].sum()) * 100.0
        return accuracy, disease_index
