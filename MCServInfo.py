import requests 
from flask import Flask, request, render_template
import json

def json_formatter(json_data):
    data = json.loads(json_data)
    formatted_json = json.dumps(data, indent=4)
    return formatted_json

def get_mc_server_info(name):
    server_info = requests.get("https://api.mcsrvstat.us/3/{0}".format(name)).content
    if not server_info is None:        
        return json_formatter(server_info)
    return "None"

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method=="POST":
        data = request.form["server-name-input"]
        answer = get_mc_server_info(data)
        return render_template('index.html', answer_data=answer)
    return render_template('index.html')

app.run(debug=True)