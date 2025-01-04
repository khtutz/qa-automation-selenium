from typing import Dict, Any
from pathlib import Path
import yaml

from src.travel_airbnb.data.models.booking_models import SearchCriteria, FilterCriteria

class DataLoader:
    def __init__(self, environment: str = 'development'):
        self.environment = environment
        self.base_path = Path(__file__).parent.parent / 'data' / 'test_data'

    # Load booking test data for the specified environment
    def load_booking_test_data(self) -> Dict[str, Any]:
        file_path = self.base_path / self.environment / 'booking_test_data.yaml'

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
        
    # Get specific scenario data as dataclass instances
    def get_scenario_data(
            self, 
            scenario: str) -> tuple[SearchCriteria, FilterCriteria]:
        data = self.load_booking_test_data()

        if scenario not in data:
            raise ValueError(f"Scenario '{scenario}' not found in test data")
        
        scenario_data = data[scenario]
        search_criteria = SearchCriteria(**scenario_data['search_criteria'])
        filter_criteria = FilterCriteria(**scenario_data['filter_criteria'])
        
        return search_criteria, filter_criteria
