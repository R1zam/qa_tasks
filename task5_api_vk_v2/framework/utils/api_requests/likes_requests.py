from framework.utils.other_utils.response_utils import RequestsTypes
from framework.utils.other_utils.params_creator import ParamsCreator


class LikesAPIRequests:
    @staticmethod
    def get_likes_list(url, additional_params, *args):
        params = ParamsCreator.create_params(*args)
        params.update(additional_params)
        response = RequestsTypes.get_request(url, params=params)
        return response
