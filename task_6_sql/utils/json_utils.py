import json
import os
from resources import path


class JSONUtils:
    def __init__(self, filename):
        with open(os.path.join(path, filename)) as f:
            self.data = json.load(f)
