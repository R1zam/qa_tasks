import csv
from utils.test_utils import TestData

filename = TestData("test_data.json").get_data("csv_filename")


class CSVLogger:

    def create_log(self, result):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)
