from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Year(BaseModel):
    year: int
    club: str


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World, this is an api of jordy sels"}


@app.get("/year/{year}")
async def read_year(year: int):
    if year == 2010:
        return {"in the year '" + str(year) + "', Inter Milaan won the Champions League"}
    elif year == 2011:
        return {"in the year '" + str(year) + "', Barcelona won the Champions League"}
    elif year == 2012:
        return {"in the year '" + str(year) + "', Chelsea won the Champions League"}
    elif year == 2013:
        return {"in the year '" + str(year) + "', Bayern München won the Champions League"}
    elif year == 2014:
        return {"in the year '" + str(year) + "', Real Madrid won the Champions League"}
    elif year == 2015:
        return {"in the year '" + str(year) + "', Barcelona won the Champions League"}
    elif year == 2016:
        return {"in the year '" + str(year) + "', Real Madrid won the Champions League"}
    elif year == 2017:
        return {"in the year '" + str(year) + "', Real Madrid won the Champions League"}
    elif year == 2018:
        return {"in the year '" + str(year) + "', Real Madrid won the Champions League"}
    elif year == 2019:
        return {"in the year '" + str(year) + "', Liverpool won the Champions League"}
    elif year == 2020:
        return {"in the year '" + str(year) + "', Bayern München won the Champions League"}
    elif year == 2021:
        return {"in the year '" + str(year) + "', Chelsea won the Champions League"}
    elif year == 2022:
        return {"in the year '" + str(year) + "', Real Madrid won the Champions League"}
    else:
        return {"year must be between 2010-2022"}



@app.get("/club/{club}")
async def read_club(club: str):
    if club == 'Real Madrid':
        return {club + ' won the champions league in the year 2014, 2016, 2017, 2018 and 2022'}
    elif club == 'Barcelona':
        return {club + ' won the champions league in the year 2011 and 2015'}
    elif club == 'Bayern München':
        return {club + ' won the champions league in the year 2013 and 2020'}
    elif club == 'Chelsea':
        return {club + ' won the champions league in the year 2012 and 2021'}
    elif club == 'Liverpool':
        return {club + ' won the champions league in the year 2019'}
    elif club == 'Inter Milaan':
        return {club + ' won the champions league in the year 2010'}
    else:
        return {"club didn't won the champions league between 2010-2022"}


@app.post("/year/")
async def create_Year(year: Year):
    return year

