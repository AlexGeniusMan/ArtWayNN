import base64
import numpy as np

from io import BytesIO
from PIL import Image


def base64_to_image(base64_str: bytes):
    '''
    Convert base64 string to PIL image.

    Args:
        base64: bytes. Bse64 string of image.

    Returns:
        PIL.Image object
    '''

    bytes_data = base64.b64decode(base64_str)
    image_data = BytesIO(bytes_data)
    image = Image.open(image_data).convert('RGB')
    return image


def image_to_numpy(image):

    '''
    Convert image to numpy array.

    Args:
        image: PIL.Image. Image for converting.

    Returns:
        Numpy array with shape (height, width, channels).
    '''

    w, h = image.size
    image_data = np.array(image.getdata())
    channels = image_data.shape[-1]
    return np.reshape(image_data, (h, w, channels))
