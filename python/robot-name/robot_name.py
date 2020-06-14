import random


class Robot:
    def __init__(self):
        random.seed()

        self.name = self._gen_name()

    def _gen_name(self):
        letters = (chr(n)
                   for n in random.sample(range(ord("A"), ord("Z")), k=2))
        numbers = (str(n) for n in random.sample(range(0, 10), k=3))
        name = ''.join([*letters, *numbers])

        return name

    def reset(self):
        self.__init__()
