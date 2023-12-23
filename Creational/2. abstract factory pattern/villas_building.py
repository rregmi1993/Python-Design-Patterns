from one_bhk_villa import  OneBhkVilla
from two_bhk_villa import TwoBhkVilla
from three_bhk_villa import ThreeBhkVilla

class VillaBulilding:

    @staticmethod

    def get_villas_details(villa_type):
        if villa_type == '1bhkVilla':
            return OneBhkVilla()
        elif villa_type == '2bhkVilla':
            return TwoBhkVilla()
        elif villa_type == '3bhkVilla':
            return ThreeBhkVilla()
        else:
            return None