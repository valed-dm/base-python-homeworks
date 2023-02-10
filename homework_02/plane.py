"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, extra_cargo):
        total_cargo = self.cargo + extra_cargo

        if total_cargo <= self.max_cargo:
            self.cargo = total_cargo
        else:
            raise CargoOverload('Cargo overload')

    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0

        return prev_cargo
