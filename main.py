from director.director import Director
from house_builder.builder import HouseBuilder

if __name__ == '__main__':
    build = HouseBuilder()
    director = Director(build)
    # Here we will use the Director to build different houses
    house1 = director.building_specific_house(number_of_room=4, number_of_floor=2, number_of_bathrooms=2, garage=True)
    print("house 1: \n", f' room number : {house1.room} \n '
                         f'number of the floor: {house1.floor}\n '
                         f' garden :{house1.garden} \n'
                         f' number of bathroom: {house1.bathrooms}\n '
                         f'garage : {house1.garage}\n')

    house2 = director.building_specific_house(number_of_room=9, number_of_floor=3, number_of_bathrooms=4)
    print("house 2: \n", f' room number : {house2.room} \n '
          f'number of the floor: {house2.floor}\n '
          f' garden :{house2.garden} \n'
          f' number of bathroom: {house2.bathrooms}\n '
          f'garage : {house2.garage}')
