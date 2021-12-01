from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    data = {"data" : "I love this api"}
    return data