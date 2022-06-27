from framework.utils.other_utils.response_utils import RequestsTypes
from framework.utils.other_utils.params_creator import ParamsCreator


class PhotosAPIRequests:
    @staticmethod
    def get_photo_upload_url(url, *args):
        params = ParamsCreator.create_params(*args)
        response = RequestsTypes.post_request(url, params=params)
        return response

    @staticmethod
    def save_wall_photo(url, *args):
        params = ParamsCreator.create_params(*args)
        response = RequestsTypes.post_request(url, params=params)
        return response

    @staticmethod
    def upload_image_on_url(upload_url, img):
        response = RequestsTypes.post_files_request(upload_url, files=img)
        return response
