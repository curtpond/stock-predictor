from fastapi import FastAPI # import FastAPI
app = FastAPI() # create an instance of FastAPI

@app.get("/ping") # create a route
def pong(): # create a function to handle the route
    return {"ping": "pong"} # return a simple dictionary of key-value pairs
