from digimon.client import DigimonClient
from digibase import digivolve


client = DigimonClient()


def get_digimon(name="agumon"):
   response = client.get_digimon_by_name(name)
   return response.json()