from utils.json_utils import JSONUtils


class TestData(JSONUtils):
    def get_data(self, key):
        return self.data[key]
