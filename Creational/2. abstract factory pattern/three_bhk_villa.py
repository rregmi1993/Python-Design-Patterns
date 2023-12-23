from interface_villas import IVilla

class ThreeBhkVilla(IVilla):
    
    def __init__(self):
        self._bedroom = 3
        self._kitchen = 1
        self._hall = 1
        self._bathroom = 3

    def get_details(self):

        return {"Bed Room" : self._bedroom, "Kitchen ": self._kitchen, 
                "Hall " : self._hall, "Bath Room " : self._bathroom}