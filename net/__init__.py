import tensorflow as tf
import numpy as np
import pathlib

from image import base64_to_image, image_to_numpy


MODEL_PATH = 'net\quant_model.tflite'
IMAGE_SIZE = 64


def predict(base64_str: bytes) -> int:
    '''
    Predict the label of input image.

    Args:
        base64_str: bytes. Bse64 string of image.

    Returns:
        Integer number of image label in range [0, num_classes).
    '''

    # load TFLite model interpreter
    interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
    interpreter.allocate_tensors()

    # load and prepare the image
    image = base64_to_image(base64_str)
    image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    image = image_to_numpy(image) / 255.
    image = np.expand_dims(image, axis=0).astype(np.float32)

    # invoke interpreter
    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]
    interpreter.set_tensor(input_index, image)
    interpreter.invoke()

    # make prediction
    predictions = interpreter.get_tensor(output_index)
    predictions = tf.nn.softmax(predictions[0]).numpy()

    return predictions.tolist()
