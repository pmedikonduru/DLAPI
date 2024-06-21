# This file contains the routes for the web server

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, validator
import tasks

app = FastAPI()

languages = ["English", "French", "German", "Romanian"]

class Translation(BaseModel):
    text: str
    base_lang: str
    final_lang: str

    @validator('base_lang', 'final_lang') #validates that these languages are supported
    def valid_lang(cls, lang):
        if lang not in languages:
            raise ValueError("Invalid language")
        return lang

# Route 1: Tests if everythign is working (index route) wil return "Hello World"
@app.get("/") #index route
def get_root(): #decorator - when get request is made we want to call thsi function - get request for asking for data, post request for sending data to server
    return {"message": "Hello world"}


#Route 2: Translation endpoint - takes ina translation request, store it in the db, so client can query db to see if ttranslation is finsihed
@app.post("/translate")
def post_translation(t: Translation, background_tasks: BackgroundTasks): #enables translation to be ran in background -avoids errors from long translations in web address
    t_id = tasks.store_translation(t)
    background_tasks.add_task(tasks.run_translation, t_id)
    return {"task_id": t_id}

#Route 3: Results - takes in a trasnlation id and returns the translated text
@app.get("/results")
def get_translation(t_id: int):
    return {"translation": tasks.find_translation(t_id)}

