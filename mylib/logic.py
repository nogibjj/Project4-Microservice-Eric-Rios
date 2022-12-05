import requests

# def get_random_activity():
#     """Get random activity from the Bored API"""
#     url = "https://www.boredapi.com/api/activity/"
#     response = requests.get(url)
#     return response.json()


def get_activity_by_price(value):
    """Get random activity according to price inputted"""

    x = float(value)

    if x < 0 and x > 1:
        return "No activity found with that price. Your options are from 0 to 1."

    response = requests.get(
        f"https://www.boredapi.com/api/activity?price={x}", timeout=120
    )

    return response.json()


def get_activity_by_type(value):
    """Get random activity according to type inputted"""
    if value not in [
        "education",
        "recreational",
        "social",
        "diy",
        "charity",
        "cooking",
        "relaxation",
        "music",
        "busywork",
    ]:

        return "No activity found with that type. Your options are education, recreational, social, diy, charity, cooking, relaxation, music, and busywork."

    response = requests.get(
        f"https://www.boredapi.com/api/activity?type={value}", timeout=120
    )

    return response.json()


def get_activity_by_participant_count(value):
    """Get random activity according to number of participants inputted"""
    if value not in ["1", "2", "3", "4", "5"]:
        return (
            "No activity found with that number of participants. Your options are 1-5."
        )

    response = requests.get(
        f"https://www.boredapi.com/api/activity?participants={value}", timeout=120
    )

    return response.json()
