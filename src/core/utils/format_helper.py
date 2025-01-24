import re

# Remove non-digit characters except '.'
def get_price_number(price: str) -> float:
    return float(re.sub(r'[^\d.]', '', str(price)))