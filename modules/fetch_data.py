#Fetch data from FRED
#vibecoding with ChatGPT


import os
import requests
from datetime import datetime           #Timestamp for saved files

#Note to self - This could be generalised by having the series ID passed to the function.
def download_us_yields(API_key):
    #Downloads historical 10y UST yields from FRED to local

    #BEFORE doing any of this I should check if the most recent data is already in

    URL_base = "https://api.stlouisfed.org"
    URL_endpoint = "/fred/series/observations"
    #Note to self - I should read the API key from a text file
    API_key = "f889f763982c5a97c15dd61f752b7d15"
    series_id = "DGS10"
    params = {
        "api_key": API_key,
        'series_id': series_id,
        'file_type': 'json'
    }

    #Construct the URL
    URL = f"{URL_base}{URL_endpoint}?series_id={series_id}&api_key={API_key}&file_type=json"
    print(URL)

    #Ensure the target directory exists
    os.makedirs("data", exist_ok=True)

    #Create a file with today's date
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"data/UST_yields_{today}.csv"

    #Request the data
    response = requests.get(URL, params=params)
    response.raise_for_status()      #This creates an error if the download fails

    #Save the file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"JSON data downloaded and saved as {filename}")
    return filename