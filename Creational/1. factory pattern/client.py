"The factory Design pattern use case example code"


from society_building import SocietyBuilding

#object creation 
flat_obj = SocietyBuilding.get_flat_details("1bhk")
print(flat_obj.get_details())


#we can access the FLAT* like below but which is not inline with design principle 
#from one_bhk import OneBhkFlat
#oneBhk_details = OneBhkFlat.get_details()
#print(oneBhk_details)


#source: https://sbcode.net/python/