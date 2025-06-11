from dotenv import load_dotenv
import pandas as pd
import sqlite3
import os


load_dotenv()
EXCEL_PATH = os.getenv("EXCEL_PATH")

def Connect(path: str):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

def CreateTable(dbPath: str):
    conn = Connect(dbPath)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            Id INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Species TEXT,
            Likes TEXT,
            Quote TEXT,
            Image TEXT NOT NULL    
        )
    ''')

    conn.commit()
    conn.close()

def LoadExcelData(dbPath: str, fileName: str):
    conn = Connect(dbPath)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM characters")

    file = pd.read_excel(fileName)

    for _, row in file.iterrows():
        cursor.execute('''
            INSERT INTO characters (Id, Name, Species, Likes, Quote, Image)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (row['ID'], row['Name'], row['Species'], row['Likes'], row['Quote'], row['Image']))

    conn.commit()
    conn.close()

def NukeCharacters(dbPath: str):
    conn = Connect(dbPath)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE characters")

    conn.commit()
    conn.close()
