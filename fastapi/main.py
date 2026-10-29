import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    print("this is a api call")
    return {"message": "welcome to the fast api world" + "api request is completed"}


# run in uvicorn using : uvicorn main:app --reload


@app.get("/home")
def home():
    return "this is second get call for home"


@app.get("/home/{name}")
def parameters(name):
    return f"hello mr {name}"


@app.get("/hello/{name}/{age}")
async def hello(name: str, age: int):
    return {"name": name, "age": age}


# call the uvicorn programatically
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
