from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello from {}".format({"{cookiecutter.source_name}}")}


@app.post("/predict/")
def my_route(name: str = Body(...), values: str = Body(...)) -> None:
    print("name:", name)
    print("values:", values)
    return JSONResponse({"name": name, "values": values})