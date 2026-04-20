from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/api/test-db")
def test_db():
    conn = psycopg2.connect(
        host="db",
        database="app_db",
        user="postgres",
        password="secret"
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return {"db_result": result}