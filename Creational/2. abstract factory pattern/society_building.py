from one_bhk import OneBhkFlat
from two_bhk import TwoBhkFlat
from three_bhk import ThreeBhkFlat


class SocietyBuilding:

    @staticmethod
    def get_flat_details(flat_type):

        if flat_type == "1bhkFlat":
            return OneBhkFlat()
        elif flat_type == "2bhkFlat":
            return TwoBhkFlat()
        elif flat_type == "3bhkFlat":
            return ThreeBhkFlat()
        
        return None