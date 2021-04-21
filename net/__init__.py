import tensorflow as tf
import numpy as np
import pathlib

from image import base64_to_image, image_to_numpy


MODEL_PATH = r'net\quant_model.tflite'


def make_prediction(base64_str: bytes):
    '''
    '''

    interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
    interpreter.allocate_tensors()

    image = base64_to_image(base64_str)
    image = image_to_numpy(image)

    return