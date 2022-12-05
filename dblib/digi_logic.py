import requests

def get_data():
    """Get data from the Digimon API"""
    return requests.get("https://digimon-api.vercel.app/api/digimon")

def get_digimon(value):
    """Get the digimon info for the name inputted"""
    data = get_data().json()
    for digimon in data:
        if digimon["name"].lower() == value:
            return digimon
    return {"error": "No digimon found with that name"}

def get_digimon_list():
    """Get a list of all digimon names"""
    data = get_data().json()
    digimon_list = []
    for digimon in data:
        digimon_list.append(digimon["name"])
    return digimon_list

def get_digimon_list_by_level(level):
    """Get a list of digimon names by level"""
    data = get_data().json()
    digimon_list = []
    for digimon in data:
        if digimon["level"] == level:
            digimon_list.append(digimon["name"])
    return digimon_list

def get_digimon_list_by_type(digimon_type):
    """Get a list of digimon names by type"""
    data = get_data().json()
    digimon_list = []
    for digimon in data:
        if digimon["type"] == digimon_type:
            digimon_list.append(digimon["name"])
    return digimon_list

def get_digimon_list_by_attribute(attribute):
    """Get a list of digimon names by attribute"""
    data = get_data().json()
    digimon_list = []
    for digimon in data:
        if digimon["attribute"] == attribute:
            digimon_list.append(digimon["name"])
    return digimon_list

def get_digimon_list_by_stage(stage):
    """Get a list of digimon names by stage"""
    data = get_data().json()
    digimon_list = []
    for digimon in data:
        if digimon["stage"] == stage:
            digimon_list.append(digimon["name"])
    return digimon_list

def get_digimon_list_by_memory(memory):
    """Get a list of digimon names by memory"""
    data = get_data().json()
    digimon_list = []
    for digimon in data:
        if digimon["memory"] == memory:
            digimon_list.append(digimon["name"])
    return digimon_list

