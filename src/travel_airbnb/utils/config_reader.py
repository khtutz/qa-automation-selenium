import os
import yaml

class ConfigReader:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._config is None:
            self.load_config()

    def load_config(self):
        env = os.getenv('TEST_ENV', 'development').lower()
        current_directory = os.path.dirname(__file__)
        parent_directory = os.path.dirname(current_directory)
        # Construct the path to the config file
        config_path = os.path.join(
        parent_directory,
        'configs',
        'env_config.yaml')

        if not config_path:
            raise FileNotFoundError('Config file not found')
        
        with open(config_path, 'r') as file:
            all_configs = yaml.safe_load(file)
            self._config = all_configs.get(env, all_configs['development'])

    @property
    def base_url(self):
        return self._config['base_url']
    
    @property
    def signup_url(self):
        return self._config['signup_url']
    
    @property
    def login_url(self):
        return self._config['login_url']
    
    @property
    def timeout(self):
        return self._config['timeout']
    
    @property
    def implicit_wait(self):
        return self._config['implicit_wait']
    
    @property
    def login_cookies_path(self):
        return self._config['login_cookies_path']
    
    @property
    def log_level(self):
        return self._config.get('log_level', 'DEBUG')