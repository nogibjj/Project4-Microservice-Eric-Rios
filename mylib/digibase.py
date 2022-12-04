# import pandas as pd

# df = pd.read_csv("DigiDB_digimonlist.csv")

ls = []

with open("DigiDB_digimonlist.txt", "r") as f:
    
    for line in f:

        info = line.split(',')
        digi_name = info[1]
        ls.append(digi_name)


def digivolve():
    
    """Return a list of digimon names."""
    # name_options = [name.lower() for name in df["Digimon"].unique().tolist()]

    return ls
