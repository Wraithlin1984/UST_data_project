#Loads data from a local JSON as a 2-dimensional list
#Vibecoding with ChatGPT

import json

def load_data_from_json(filename):
    #Loads dates and data from a JSON into a 2d list

    #Open the passed filename and read it into 'data'
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    observations = data.get("observations", [])

    #Build the 2d list: [date], [data]
    data = []

    for obs in observations:
        date = obs["date"]
        value = obs["value"]

        #Handle missing data (denoted ".")
        if value == ".":
            continue
        data.append([date, float(value)])

    return data