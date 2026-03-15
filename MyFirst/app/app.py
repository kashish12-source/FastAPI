from fastapi import FastAPI
''' The line from fastapi import FastAPI is the fundamental starting point for any FastAPI application for a few key reasons: 
1. It imports the FastAPI class from the fastapi library, which is the main class used to create a FastAPI application.
2. It creates an instance of the FastAPI class, which is the main object used to create a FastAPI application.

'''

app = FastAPI()

# after creating the app object , we can create routes and we need to define the method of the routes 
# dectore in the form of @app.get("/")
@app.get("/")