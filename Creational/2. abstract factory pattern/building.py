from interface_building import IBuilding
from society_building import SocietyBuilding
from villas_building import VillaBulilding

class Buliding(IBuilding):

    @staticmethod
    def get_buliding(building_type):
        try:
            if building_type in ['1bhkFlat', '2bhkFlat', '3bhkFlat']:
                return SocietyBuilding.get_flat_details(building_type)
            elif building_type in ['1bhkVilla', '2bhkVilla', '3bhkVilla']:
                return VillaBulilding.get_villas_details(building_type)
            raise "No factory method found"
        except Exception as _e:
            print("error : " + str(_e))
        
        return None
