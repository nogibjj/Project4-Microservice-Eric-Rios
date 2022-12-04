import pandas as pd




def digivolve():

    df = pd.read_csv('DigiDB_digimonlist.csv')

    name_options = [name.lower() for name in df['Digimon'].unique().tolist()]

    return name_options