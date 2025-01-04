from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class SearchCriteria:
    currency: str
    expected_currency: str
    destination: str
    expected_destination: str
    checkin_date: str
    expected_checkin_date: str
    checkout_date: str
    expected_checkout_date: str
    adult_count: int = 0
    children_count: int = 0
    infant_count: int = 0
    pet_count: int = 0
    expected_guests: str = ''

@dataclass
class FilterCriteria:
    type_of_place: str
    min_price: int
    max_price: int
    bathrooms_count: int
    property_type: str
    amenity_options: Optional[Tuple[str, ...]]
    booking_options: Optional[Tuple[str, ...]]