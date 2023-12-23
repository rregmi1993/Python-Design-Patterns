from one_bhk import OneBhkFlat
from two_bhk import TwoBhkFlat
from three_bhk import ThreeBhkFlat


class SocietyBuilding:

    @staticmethod
    def get_flat_details(flat_type):

        if flat_type == "1bhk":
            return OneBhkFlat()
        elif flat_type == "2bhk":
            return TwoBhkFlat()
        elif flat_type == "3bhk":
            return ThreeBhkFlat()
        
        return None