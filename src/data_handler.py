from dataclasses import dataclass
from typing import Optional

@dataclass
class Sample:
    'car_color' : str,
    'fuel_type' : str,
    'car_type' : str,
    'car_license' : str,
    'gear_type' : str,
    'windows' : str,
    'motor_power' : int,
    'speedometer' : int,
    'passengers_number' : int,
    'payment_method' : str,
    'car_state' : str,
    'ex_owners' : int,
    'additions' : str
