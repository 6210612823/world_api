import csv

# For tutorial on FastAPI
# See https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

<<<<<<< HEAD
# get country data from csv file  
filename = "world_table_country.csv"
with open(filename, "r",encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    data_country = [{k: v for (k, v) in zip(headers, row)} for row in csv_reader]
=======
# get city data from csv file
filename = "world_table_city.csv"
with open(filename, "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    data_country = [{k: v for (k, v) in zip(headers, row)}
                    for row in csv_reader]
>>>>>>> 18e7736 (Add endpoint /world/city/{name})

# create an instance of class FastAPI named "app"
app = FastAPI()

# define function that handles "GET" request with endpoint "/"


@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello there"}

<<<<<<< HEAD

# define function that handles "GET" request with endpoint "/world"
# list all countries
@app.get("/world")
async def read_countries() -> dict:
    return {"result": data_country}

=======
# define function that handles "GET" request with endpoint "/world/city/{name}"
# "/world/city/{name}" is a "path paramter" endpoint


@app.get("/world/city/{name}")
async def read_city(name: str) -> dict:
    for row in data_city:
        if row["Name"].lower() == name.lower():
            return {"result": row}
    return {"result": {}}
>>>>>>> 18e7736 (Add endpoint /world/city/{name})
