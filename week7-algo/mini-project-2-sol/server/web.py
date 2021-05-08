from flask import Flask
from flask import request

app = Flask(__name__)
DATA_FILE_NAME = "client_rate.json"


@app.route("/")
def default() -> str:
    return "FIRST PROJECT - we have " + str(len(get_client_rates())) + " clients in total."


# sample data load function
# This is a temporary data file - when we get to know more about database and cloud storage
# we would not be using this kind of data storage.
def get_client_rates() -> {str: {str: float}}:
    """
    :return: dict {client_id: {'rate': float}}
    """
    import pandas as pd
    df = pd.read_json(DATA_FILE_NAME)
    return df.to_dict()


@app.route("/rate/<client_id>")
def get_client_rate(client_id: str) -> str:
    client_rates = get_client_rates()
    if client_id in client_rates:
        return str(client_rates[client_id]['rate'])
    return "0"


@app.route("/rate", methods=['POST'])
def upsert_client_rate() -> str:
    param = request.get_json()
    client_id = param['client_id']
    rate = param['rate']

    update_client_rates(client_id, rate)
    return "UPDATED"


def update_client_rates(client_id: str, rate: float) -> None:
    client_rates = get_client_rates()
    client_rates[client_id] = {"rate": rate}
    import pandas as pd
    df = pd.DataFrame.from_dict(client_rates)
    df.to_json(DATA_FILE_NAME)


if __name__ == "__main__":
    app.run()
