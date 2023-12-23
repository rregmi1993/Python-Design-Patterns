"The factory Design pattern use case example code"


from society_building import SocietyBuilding

from villas_building import VillaBulilding

#object creation 
flat_obj = SocietyBuilding.get_flat_details("1bhkFlat")
print(f"{flat_obj.__class__} : {flat_obj.get_details()}")

villa_obj = VillaBulilding.get_villas_details('2bhkVilla')
print(f"{villa_obj.__class__} : {flat_obj.get_details()}")


#source: https://sbcode.net/python/