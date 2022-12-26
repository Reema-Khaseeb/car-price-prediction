from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class Sample:
    car_color : str
    fuel_type : str
    car_type : str
    car_license : str
    gear_type : str
    windows : str
    motor_power : int
    speedometer : int
    passengers_number : int
    payment_method : str
    car_state : str
    ex_owners : int
    additions : str

rename_columns_dict = {
    'car_color': 'لون السيارة',
    'fuel_type': 'نوع الوقود',
    'car_type': 'أصل السيارة',
    'car_license': 'رخصة السيارة',
    'gear_type': 'نوع الجير',
    'windows': 'الزجاج',
    'motor_power': 'قوة الماتور',
    'speedometer': 'عداد السيارة',
    'passengers_number': 'عدد الركاب',
    'payment_method': 'وسيلة الدفع',
    'car_state': 'معروضة',
    'ex_owners': 'أصحاب سابقون',
    'additions': 'إضافات',
    'price': 'price'
    }

class Car(BaseModel):
    car_color : str
    fuel_type : str
    car_type : str
    car_license : str
    gear_type : str
    windows : str
    motor_power : int
    speedometer : int
    passengers_number : int
    payment_method : str
    car_state : str
    ex_owners : int
    additions : str
