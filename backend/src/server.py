from fastapi import FastAPI, HTTPException

import json

app = FastAPI()

@app.get("/domains")
def get_domains():
    with open("../domains.json", "r") as f:
        data = json.load(f)
    return {"domains": data}


