from flask import Flask
from flask import request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)


# -- DO NOT EDIT
# sample end point for HTTP Get
@app.route("/")
def default():
    """
    default endpoint for this server, just for demo.

    :return: str
    """
    return "FIRST PROJECT - we have " + str(len(get_client_rates())) + " clients in total."


# sample data load function
# This is a temporary data file - when we get to know more about database and cloud storage
# we would not be using this kind of data storage.
def get_client_rates():
    """
    return all the client - rate pairs we have.

    :return: dict {id: {'rate':float}}
    """
    import pandas as pd
    df = pd.read_json("client_rate.json")
    return df.to_dict()


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_write_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# load some existing data in data.sql
def load_data(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    sql_file = open("data.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)


# -- DO NOT EDIT END


# When query http://hostname/rate/client1 it would return the rate number for client1 - 0.2
@app.route("/rate/<client_id>")
def get_client_rate(client_id):
    """
    End point for getting rate for a client_id.

    :param client_id: str
    :return: http response
    """
    # How to get the actual rate from client_id?

    # -- TODO: Part 1, Replace to lookup from database
    con = create_connection("test_senyang.db")
    res = execute_read_query(con, "SELECT rate FROM client_rates WHERE client_id='{}';".format(client_id))
    return str(res[0][0])
    # -- TODO END: Part 1


@app.route("/rate", methods=['POST'])
def upsert_client_rate():
    """
    End point for updating or inserting client rate values in the post param.

    :return: http response.
    """
    # We want to update if the client exist in the client_rate.json data
    # Or insert a new client-rate pair into client_rate.json data
    data = request.get_json()
    update_client_rates(list(data.keys())[0], data[list(data.keys())[0]]["rate"])
    # new def update_client_rates_db()
    # 1. if exist - update
    # 2. not exist - insert - query max - then + 1
    return "SUCCESSFULLY UPDATED!"


def update_client_rates(client_id, rate):
    """
    update or insert a client_id - rate pair.

    :param client_id: string, e.g. 'client1'
    :param rate: float, e.g. 0.1
    :return:
    """

    # -- TODO: Part 2, Replace to write to database
    con = create_connection("test_senyang.db")
    execute_write_query(con, "INSERT INTO client_rates VALUES ({},'{}',{});".format(client_id[-1], client_id, rate))
    # -- TODO END: Part 2


# -- TODO: Part 3, clean up this file, and remove 'client_rate.json', we should not read/write from file.
# -- TODO END: Part 3


if __name__ == "__main__":
    # -- TODO: use 'test_first_name.db' as db file.
    load_data("test_senyang.db")
    app.run()
