from builder.interface import Builder


class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def building_specific_house(self,
                                number_of_room: int = 2,
                                number_of_floor: int = 1,
                                number_of_bathrooms: int = 1,
                                garage: bool = False,
                                garden: bool = False):
        self.builder.set_room(number_of_room=number_of_room)
        self.builder.set_floor(number_of_floor=number_of_floor)
        self.builder.set_bathrooms(number_of_bathrooms=number_of_bathrooms)
        self.builder.set_garden(garden)
        self.builder.set_garage(garage)
        return self.builder.build()

