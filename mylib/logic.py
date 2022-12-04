from digimon.client import DigimonClient
from mylib.digibase import digivolve


client = DigimonClient()


def get_digimon(name="agumon"):
   """Get a digimon by name."""
   ls = digivolve()
   
   if name.lower() in ls:
      
      response = client.get_digimon_by_name(name)
      return response.json()
      
   else:
      
      return "Name was not typed correctly."
   