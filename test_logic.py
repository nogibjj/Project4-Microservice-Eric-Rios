
from digimon.client import DigimonClient

def test_digimon(name="agumon"):

        test_result = client.get_digimon_by_name(name)

        return test_result


assert str(test_digimon()) == "<Response [200]>"