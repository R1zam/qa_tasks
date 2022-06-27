from framework.utils.json_utils import JSONUtils


class LoggerData(JSONUtils):
    def get_log_data(self, key):
        return self.data[key]
