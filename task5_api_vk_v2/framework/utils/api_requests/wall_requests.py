from framework.utils.other_utils.response_utils import RequestsTypes
from framework.utils.other_utils.params_creator import ParamsCreator


class WallAPIRequests:

    @staticmethod
    def edit_msg_on_wall(url, *args):
        params = ParamsCreator.create_params(*args)
        RequestsTypes.post_request(url, params=params)

    @staticmethod
    def create_post_comment(url, *args):
        params = ParamsCreator.create_params(*args)
        RequestsTypes.get_request(url, params=params)

    @staticmethod
    def delete_post(url, *args):
        params = ParamsCreator.create_params(*args)
        RequestsTypes.get_request(url, params=params)

    @staticmethod
    def post_msg_on_wall(url, *args):
        params = ParamsCreator.create_params(*args)
        response = RequestsTypes.post_request(url, params=params)
        return response
