from digimon.client import DigimonClient
import pandas as pd

df = pd.read_csv('DigiDB_digimonlist.csv')

client = DigimonClient()





response = client.get_digimon_by_name("agumon")
print(response.json())