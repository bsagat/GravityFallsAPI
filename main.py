from fastapi import FastAPI, HTTPException
from internal.models import Character
import internal.database as repo
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
DB_PATH = os.getenv("DB_PATH")

@app.get("/")
def root():
    return {"Characters": "/characters"}

@app.get("/characters")
def get_characters_count():
    count = repo.CharacterCount(DB_PATH)
    return {"Count": count[0]}

@app.get("/characters/{character_id}", response_model=Character)
def get_character(character_id: int):
    character = repo.CharacterByID(DB_PATH,character_id)

    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")

    return {
        "Id": character["Id"],
        "Name": character["Name"],
        "Species": character["Species"],
        "Likes": character["Likes"],
        "Quote": character["Quote"],
        "Image": character["Image"]
    }

