
from interface_villas import IVilla

class TwoBhkVilla(IVilla):

    def __init__(self):
        self._bedroom = 2
        self._kitchen = 1
        self._hall = 1
        self._bathroom = 2

    def get_details(self):

        return {"Bed Room" : self._bedroom, "Kitchen ": self._kitchen, 
                "Hall " : self._hall, "Bath Room " : self._bathroom}