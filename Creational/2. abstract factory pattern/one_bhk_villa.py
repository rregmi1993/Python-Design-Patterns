from interface_villas import IVilla

class OneBhkVilla(IVilla):

    def __init__(self):
        self._bedroom = 1
        self._kitchen = 1
        self._hall = 1
        self._bathroom = 1

    def get_details(self):

        return {"Bed Room" : self._bedroom, "Kitchen ": self._kitchen, 
                "Hall " : self._hall, "Bath Room " : self._bathroom}