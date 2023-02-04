"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    def __init__(self, volume=None, pistons=None):
        self.volume = volume
        self.pistons = pistons
