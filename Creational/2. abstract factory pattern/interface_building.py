from abc import ABCMeta, abstractmethod

class IBuilding(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def get_building_details(builing_type):
        "this is abstract metho of building"