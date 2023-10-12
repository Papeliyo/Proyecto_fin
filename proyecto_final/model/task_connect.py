import psycopg

class TaskConnection():
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=fastapi_test user=postgres password=2331 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def read_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute(""" SELECT * FROM "task" """)
            return data.fetchall()

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
        INSERT INTO "task"(titulo, descripcion, fecha_vencimiento) VALUES(%(titulo)s, %(descripcion)s, %(fecha_vencimiento)s)""", data)
        self.conn.commit()

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute(""" DELETE FROM "task" WHERE id = %s """, (id,))
            self.conn.commit()
    
    def __del__(self):
        self.conn.close()