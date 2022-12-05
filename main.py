from fastapi import FastAPI
import uvicorn
from mylib.logic import get_activity_by_price
from mylib.logic import get_activity_by_type
from mylib.logic import get_activity_by_participant_count

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Bored API.  Get your random activity by calling /type, /price  or /participants ."}


@app.get("/type/{value}")
async def type(value: str):
    """Get random activity according to type inputted"""

    result = get_activity_by_type(value)

    return {"result": result}


@app.get("/price/{value}")
async def price(value: str):

    """Get random activity according to price inputted"""

    result = get_activity_by_price(value)

    return {"result": result}


@app.get("/participants/{name}")
async def participants(value: str):
    
    """Get random activity according to number of participants inputted"""

    result = get_activity_by_participant_count(value)

    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")























app = FastAPI()

print(get_digimon().json())


@app.get("/")
async def root():
    return {"message": "Digimon API.  Call /get_digimon and type a lowercase name to get a digimon."}


@app.get("/get_digimon/{value}")
async def search(value: str):
    """Digimon info to return for the name inputted"""

    return {"result": get_digimon(value).json()}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")