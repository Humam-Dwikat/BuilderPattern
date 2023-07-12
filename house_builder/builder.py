from abc import ABC

from builder.interface import Builder
from house_plane.house import House


class HouseBuilder(Builder, ABC):
    def __init__(self):
        self.house = House()

    def set_room(self, number_of_room):
        self.house.room = number_of_room

    def set_floor(self, number_of_floor: str):
        self.house.floor = number_of_floor

    def set_garden(self, garden: bool):
        self.house.garden = garden

    def set_garage(self, garage: bool):
        self.house.garden = garage

    def set_bathrooms(self, number_of_bathrooms: int):
        self.house.bathrooms = number_of_bathrooms

    def build(self):
        return self.house

