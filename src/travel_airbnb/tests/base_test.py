import pytest

@pytest.mark.usefixtures('setup', 'logger')
class BaseTest:
    pass
