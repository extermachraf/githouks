from fastapi import FastAPI
import os
import sys

app = FastAPI()


@app.get("/")
async def root():
    my_key = "AIzaSyAbC123456789"
    unused_variable = "this will cause a warning"
    x=1+2 # Missing spaces around operators
    print(f"My API Key is: {my_key}")
    return {"message": "Hello World"}


def unused_function():
    pass
