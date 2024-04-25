import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

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
        my_connection = Credentials_database(os.getenv('USER_DB') ,os.getenv('PASSWORD_DB') ,os.getenv('DATABASE_DB') ,os.getenv('HOST_DB') ,os.getenv('PORT_DB')).connnect()
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


times_user = get_query("""SELECT 
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


improve = get_query("""
SELECT
    technician_name,
    ROUND(
        LEAST(
            100,
            GREATEST(0, 1 - (AVG(total_days) / 30)) * 100
        ),
    2) AS eficacia,
    COUNT(*) AS total_tickets,
    ROUND(
        (AVG(total_tickets) * 
        (LEAST(
            100,
            GREATEST(0, 1 - (AVG(total_days) / 30)) * 100))
        ) / 100,
    2) AS eficiencia
FROM
    (
        SELECT
            technician_name,
            CASE
                WHEN onhold_time ~ '\d+hrs \d+min' THEN 
                    CAST(SPLIT_PART(onhold_time, 'hrs ', 1) AS INTEGER) / 24 + 
                    CAST(SPLIT_PART(SPLIT_PART(onhold_time, 'hrs ', 2), 'min', 1) AS INTEGER) / (24 * 60)
                ELSE 0
            END AS total_days,
            COUNT(*) OVER(PARTITION BY technician_name) AS total_tickets
        FROM
            report
        WHERE
            onhold_time ~ '\d+hrs \d+min'
    ) AS subquery
GROUP BY
    technician_name
ORDER BY
    eficacia DESC;
""")


data = get_query("""select * from report r;""")


group_company = get_query("""SELECT 
    site,
    COUNT(*) AS total_tickets
FROM 
    report
GROUP BY 
    site
ORDER BY 
    total_tickets DESC;""")