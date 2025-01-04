from dataclasses import dataclass

@dataclass
class LoginCredentials:
    email: str
    password: str

@dataclass
class RegistrationDetails:
    first_name: str
    last_name: str
    email: str
    password: str
    birth_date: str