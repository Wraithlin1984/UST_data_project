#The Main

from modules.fetch_data import download_us_yields


def main():
    #Download, save as local, and ingest the data
    csv_file = download_us_yields()
    print("File saved successfully", csv_file)

    #newlines will go here

if __name__ == "__main__":
    main()
