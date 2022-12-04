from digimon.client import DigimonClient


client = DigimonClient()


# response = client.get_digimon_by_name(name)
ls = []
with open("mylib/DigiDB_digimonlist.txt", "r", encoding="utf8") as f:

    for line in f:

        info = line.split(",")
        digi_name = info[1]
        ls.append(digi_name.lower())


def get_digimon(name="agumon"):

    ls = []
    
    with open("mylib/DigiDB_digimonlist.txt", "r", encoding="utf8") as f:

        for line in f:

            info = line.split(",")
            digi_name = info[1]
            ls.append(digi_name.lower())

    if name in ls:

        response = client.get_digimon_by_name(name)

        return response.json()
    else:

        return "Digimon not found. Make sure you spelled it correctly."


# def get_digimon(name="agumon"):
#    """Get a digimon by name."""

#    client = DigimonClient()

#    ls = []

#    with open(r"/workspaces/Project4-Microservice-Eric-Rios/DigiDB_digimonlist.txt", "r") as f:

#       for line in f:

#         info = line.split(',')
#         digi_name = info[1]
#         ls.append(digi_name)

#    if name.lower() in ls:

#       response = client.get_digimon_by_name(name)
#       return response.json()

#    else:

#       return "Name was not typed correctly."
