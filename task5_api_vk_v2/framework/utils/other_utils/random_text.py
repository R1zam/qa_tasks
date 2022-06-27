import string
import random


class RandomText:
    letters = string.ascii_letters

    def __call__(self, length):
        rand_string = ''.join(random.choice(self.letters) for _ in range(length))
        return rand_string
