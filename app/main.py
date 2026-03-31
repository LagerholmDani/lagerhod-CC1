from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Hello dev docker!" }


@app.get("/hello")
def hello():
    return { "msg": "Hello du!" }