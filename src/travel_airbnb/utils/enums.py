from enum import Enum

class GuestType(Enum):
    ADULTS = 'adults'
    CHILDREN = 'children'
    INFANTS = 'infants'
    PETS = 'pets'

class PlaceType(Enum):
    ANY_TYPE = 'Any type'
    ROOM = 'Room'
    ENTIRE_HOME = 'Entire home'

class PropertyType(Enum):
    HOUSE = 'House'
    APARTMENT = 'Apartment'
    GUESTHOUSE = 'Guesthouse'
    HOTEL = 'Hotel'

class AmenityOption(Enum):
    BEACHFRONT = 'Beachfront'
    POOL = 'Pool'
    WIFI = 'Wifi'
    AIR_CONDITIONING = 'Air conditioning'
    KITCHEN = 'Kitchen'
    FREE_PARKING = 'Free parking'
    WASHER = 'Washer'
    DRYER = 'Dryer'
    HEATING = 'Heating'
    DEDICATED_WORKSPACE = 'Dedicated workspace'
    TV = 'TV'
    HAIR_DRYER = 'Hair dryer'
    IRON = 'Iron'
    HOT_TUB = 'Hot tub'
    EV_CHARGER = 'EV charger'
    CRIB = 'Crib'
    KING_BED = 'King bed'
    GYM = 'Gym'
    BBQ_GRILL = 'BBQ grill'
    BREAKFAST = 'Breakfast'
    INDOOR_FIREPLACE = 'Indoor fireplace'
    SMOKING_ALLOWED = 'Smoking allowed'
    WATERFRONT = 'Waterfront'
    SMOKE_ALARM = 'Smoke alarm'
    CARBON_MONOXIDE_ALARM = 'Carbon monoxide alarm'

class BookingOption(Enum):
    INSTANT_BOOK = 'ib'
    SELF_CHECK_IN = 'amenities-51'
    FREE_CANCELLATION = 'flexible_cancellation'
    ALLOWS_PETS = 'pets'