from typing import Any
from flask import Flask, request
from sqlite3 import Error, Connection, connect

app = Flask(__name__)
DATA_FILE_NAME = "data.sql"
DB_NAME = "test.db"


def create_connection(path: str) -> Connection:
    connection = None
    try:
        connection = connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection: Connection, query: str) -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection: Connection, query: str) -> [Any]:
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def load_data(database: str) -> None:
    connection = connect(database)
    cursor = connection.cursor()
    sql_file = open(DATA_FILE_NAME)
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)


def count_clients() -> int:
    conn = create_connection(DB_NAME)
    return execute_read_query(conn, "SELECT count(id) FROM client_rates")[0][0]


@app.route("/")
def default() -> str:
    return "FIRST PROJECT - we have " + str(count_clients()) + " clients in total."


@app.route("/rate/<client_id>")
def get_client_rate(client_id: str) -> str:
    conn = create_connection(DB_NAME)
    res = execute_read_query(conn, f"SELECT rate FROM client_rates WHERE client_id = '{client_id}'")
    if res is None or len(res) == 0:
        return "0"
    return str(res[0][0])


@app.route("/rate", methods=['POST'])
def upsert_client_rate() -> str:
    data = request.get_json()
    update_client_rates(data["client_id"], data["rate"])
    return "UPDATED!"


def update_client_rates(client_id: str, rate: float) -> None:
    conn = create_connection(DB_NAME)
    res = execute_read_query(conn, f"SELECT id FROM client_rates WHERE client_id = '{client_id}'")
    if res is None or len(res) == 0:
        execute_query(conn, f"INSERT INTO client_rates (client_id, rate) VALUES('{client_id}', {rate})")
    else:
        res_id = res[0][0]
        execute_query(conn, f"UPDATE client_rates SET rate = {rate} WHERE id = '{res_id}'")


if __name__ == "__main__":
    load_data(DB_NAME)
    app.run(port=8080)
