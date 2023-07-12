from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def set_room(self, number_of_room: int):
        pass

    @abstractmethod
    def set_floor(self, number_of_floor: int):
        pass

    @abstractmethod
    def set_garden(self, garden: bool):
        pass

    @abstractmethod
    def set_bathrooms(self, number_of_bathrooms: int):
        pass

    @abstractmethod
    def set_garage(self, garage: bool):
        pass

    @abstractmethod
    def build(self):
        pass
