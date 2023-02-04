"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    """Raised when the fuel level is low"""
    pass


class NotEnoughFuel(Exception):
    """Raised when the fuel level is insufficient"""
    pass


class CargoOverload(Exception):
    """Raised when the cargo exceeds capacity"""
    pass
