from abc import ABCMeta, abstractmethod

class IVilla(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_details():
        "abstract method"
