import psycopg2
import pandas as pd
class Credentials_database:
    def __init__(self, user, password, database, host, port):
        self.__user = user
        self.__password = password
        self.__database = database
        self.__host = host
        self.__port = int(port)

    def connnect(self):
        db_params = {
            'host': self.__host,
            'database': self.__database,
            'user': self.__user,
            'password': self.__password,
            'port': self.__port,
        }

        try:
            susses_conn = psycopg2.connect(**db_params)
            return susses_conn

        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")


def get_query(code):
    global my_connection
    try:
        my_connection = Credentials_database("root", "root", "tickets", "10.150.8.30", "5432").connnect()
        cursor = my_connection.cursor()

        cursor.execute(code)

        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        dict_all = []
        for row in rows:
            data_dict = {col: val for col, val in zip(column_names, row)}
            dict_all.append(data_dict)

        data_frame = pd.DataFrame(dict_all)

        #print(f"BD_all [Debug 🐞]")
        return data_frame

    except psycopg2.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return []

    finally:
        cursor.close()
        my_connection.close()


hola = get_query("""SELECT 
    technician_name as tecnico,
    CONCAT(
        TO_CHAR(AVG(total_seconds) / (24 * 3600), 'FM999999990D'), ' días ',
        TO_CHAR((AVG(total_seconds) % (24 * 3600)) / 3600, 'FM09'), ' horas ',
        TO_CHAR((AVG(total_seconds) % 3600) / 60, 'FM09'), ' minutos ',
        TO_CHAR(AVG(total_seconds) % 60, 'FM09.99'), ' segundos'
    ) AS tiempo_promedio_de_respuesta,
     count(*) as totaL_tickets
FROM (
    SELECT 
        technician_name,
        CASE 
            WHEN onhold_time ~ '\d+hrs \d+min' THEN
                CAST(SPLIT_PART(onhold_time, 'hrs ', 1) AS INTEGER) * 3600 +
                CAST(SPLIT_PART(SPLIT_PART(onhold_time, 'hrs ', 2), 'min', 1) AS INTEGER) * 60
            ELSE
                0
        END AS total_seconds
    FROM 
        report
    WHERE 
        onhold_time ~ '\d+hrs \d+min'
) AS subquery
GROUP BY 
    technician_name
ORDER BY 
    AVG(total_seconds) DESC;
""")