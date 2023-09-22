from dataclasses import dataclass


@dataclass
class Project:
    zip_code: int
    project_type: str
    equipment: list[str]
    equipment_age: str
    fuel: str
    property_type: str
    square_feet: str
    name: str
    email: str
    state_code: str
    phone_number: str
