#Import the API key from local
#vibecoding with chatGPT

from pathlib import Path

def import_api_key():
    #Fix the location of the API as two steps higher for now
    key_file = Path(__file__).resolve().parents[2]/ "FRED_API_key.txt"

    #print(f"\n {key_file}")             #Debugging

    if not key_file.exists():
            raise FileNotFoundError(f"API key file not found at {key_file}")

    with key_file.open("r") as f:
        return  f.read().strip()
