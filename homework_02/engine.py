"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    volume: int = None
    pistons: int = None
