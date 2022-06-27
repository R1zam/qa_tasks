import requests


class RequestsTypes:

    @staticmethod
    def get_request(url, params):
        return requests.get(url, params=params)

    @staticmethod
    def post_request(url, params):
        return requests.post(url, params=params)

    @staticmethod
    def post_files_request(url, files):
        return requests.post(url, files=files)
