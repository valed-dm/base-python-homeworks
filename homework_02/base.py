from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=2500, fuel=90, fuel_consumption=11):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Low fuel')

    def move(self, distance):
        fuel_required = distance * self.fuel_consumption
        fuel_remainder = self.fuel - fuel_required

        if fuel_remainder >= 0:
            self.fuel = fuel_remainder
        else:
            raise NotEnoughFuel('Not enough fuel')
