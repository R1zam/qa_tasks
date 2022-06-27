from utils.json_utils import JSONUtils


class Config(JSONUtils):
    def get_data(self, key):
        return self.data[key]

