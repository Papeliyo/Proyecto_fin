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
            cur.execute(""" INSERT INTO "task"(titulo, descripcion, fecha_vencimiento, estado) VALUES(%(titulo)s, %(descripcion)s, %(fecha_vencimiento)s, %(estado)s) """, data)
        self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute(""" UPDATE "task" SET descripcion = %(descripcion)s, fecha_vencimiento = %(fecha_vencimiento)s, estado = %(estado)s WHERE titulo = %(titulo)s """, data)
            self.conn.commit()

    def delete(self, titulo):
        with self.conn.cursor() as cur:
            cur.execute(""" DELETE FROM "task" WHERE titulo = %s """, (titulo,))
            self.conn.commit()
    
    def __del__(self):
        self.conn.close()