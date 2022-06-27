import logging
from framework.utils.other_utils.logger_data import LoggerData

logger_data = LoggerData("logger_config.json")


class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(eval(logger_data.get_log_data("logger_level")))
        self.handler = eval(logger_data.get_log_data("handler"))
        self.handler.setFormatter(eval(logger_data.get_log_data("formatter")))
        self.logger.addHandler(self.handler)

    def info(self, message):
        self.logger.info(message)
