from PIL import Image
import numpy as np


class ImagePreprocessor:
    @staticmethod
    def get_image_pixel_sum(img_path):
        img = Image.open(img_path)
        return sum(np.array(img).flatten())

    @staticmethod
    def is_same_images(image_1, image_2):
        if image_1.shape == image_2.shape:
            low_img = min(image_1, image_2)
            max_img = max(image_1, image_2)
            similarity_percentage = low_img / max_img
            return similarity_percentage > 0.995
