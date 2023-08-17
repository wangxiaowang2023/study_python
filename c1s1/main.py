# -*- coding: utf-8 -*-
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def test():
    return {
        "abc":"123"
    }
