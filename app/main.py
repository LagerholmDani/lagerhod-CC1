from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return { "msg": "Hello dev docker!" }

@app.get("/hello")
def hello():
    return { "msg": "Hello du!" }


@app.get("/api/ip")
def get_ip(request: Request):
    return {"ip": request.client.host}


@app.get("/ip", response_class=HTMLResponse)
def get_html_ip(request: Request):
    return f"<h1>Din publika IP-adress är {request.client.host}</h1>"