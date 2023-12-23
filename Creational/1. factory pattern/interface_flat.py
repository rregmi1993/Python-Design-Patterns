"The flat interface"

from abc import abstractmethod, ABCMeta

class IFlat(metaclass=ABCMeta):
    "The flat interface(Product)"

    @staticmethod
    @abstractmethod
    def get_details():
        "A static interface method"