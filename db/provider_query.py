from db.connection import get_connection

def get_provider_info():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM providers;")
    results = cur.fetchall()
    conn.close()
    return results