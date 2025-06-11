from internal.init import Connect
import sqlite3

def CharacterByID(dbPath: str,id: int):
    with Connect(dbPath) as conn:
        cursor = conn.cursor()
        data = cursor.execute('''
            SELECT 
                Id, Name, Species, Likes, Quote, Image
            FROM 
                characters 
            WHERE 
                Id = ?
        ''',id).fetchone()

    return data
    
def CharacterCount(dbPath: str) ->int :
    with Connect(dbPath) as conn:
        cursor = conn.cursor()
        count = cursor.execute("SELECT COUNT(*) FROM characters").fetchone()

    return count