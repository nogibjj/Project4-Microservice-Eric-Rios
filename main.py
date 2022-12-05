from fastapi import FastAPI
import uvicorn
from dblib.other_logic import get_digimon

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