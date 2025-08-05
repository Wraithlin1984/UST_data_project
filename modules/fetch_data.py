#Fetch data from FRED
#vibecoding with ChatGPT

import os
import requests
from datetime import datetime           #Timestamp for saved fi

def download_FRED_data(API_key, series_id):
    #Downloads historical timeseries from FRED to local

    #Note to self: I should check if the most recent data is already in the data storage folder
    URL_base = "https://api.stlouisfed.org"
    URL_endpoint = "/fred/series/observations"
    #series_id = "DGS10"
    params = {
        "api_key": API_key,
        'series_id': series_id,
        'file_type': 'json'
    }

    #Construct the URL
    URL = f"{URL_base}{URL_endpoint}?series_id={series_id}&api_key={API_key}&file_type=json"
    #print(URL)                                 Debugging

    #Ensure the target directory exists
    os.makedirs("data", exist_ok=True)

    #Create a file with today's date
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"data/{series_id}_{today}.json"

    #Request the data
    #Added more error handling
    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        #Write the file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"JSON data downloaded and saved as {filename}")
        return filename
    except requests.exceptions.HTTPError as err:
        if err.response.status_code ==400:
            print(f"Error code 400: Bad request at {URL}")
            print(f"That series ID was not recognised.")
        else:
            print(f"HTTP error occurred at {URL}")
            print(f"{e} - Status code: {e.response.status_code}")
    except requests.exceptions.RequestException as e:
            print(f"Unknown error occurred: {e}")
    return None
