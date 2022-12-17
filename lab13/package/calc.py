from abc import ABC
from abc import abstractmethod

class calc(ABC):

    def __init__(self):
        super.__init__()

    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def calc_S(self):
        pass
