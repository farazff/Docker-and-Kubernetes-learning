import os

from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    url = data['host']
    resp = requests.get(url)
    out = {'hostname': 'Faraz_ASUS', 'time': str(resp.content)}
    json_dump = json.dumps(out)
    return json_dump


if __name__ == '__main__':

    if os.path.exists('config.json'):
        with open("config.json") as json_config_file:
            data = json.load(json_config_file)
            if 'host' not in data.keys() or 'port' not in data.keys():
                f = open('Localconfig.json')
                data = json.load(f)
    else:
        with open("Localconfig.json") as json_config_file:
            data = json.load(json_config_file)

    app.run(host="0.0.0.0", debug=True, port=data['port'])
