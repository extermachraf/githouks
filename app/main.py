from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    my_key = "AIzaSyAbC123456789"
    print(f"My API Key is: {my_key}")
    return {"message": "Hello World"}