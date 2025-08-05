#The Main

from modules.import_api_key import import_api_key
from modules.fetch_data import download_FRED_data
from modules.ingest_data import load_data_from_json
from modules.plot_data import plot_data_timeseries
from modules.frequency_distribution import bucket_timeseries
from modules.frequency_distribution import plot_histogram
from modules.digit_frequency import analyse_digit_frequency

def main():
    #Grab my FRED API key from local
    API_key = import_api_key()

    #Download, save as local
    series_id = input("Which FRED data would you like to download? (Series ID): ")
    json_file = download_FRED_data(API_key, series_id)
    #Added error handling for bad series_id
    if json_file is None:
        print("Data ingestion failed")
        return()
    print("File saved successfully to: {json_file}")

    #Now ingest the data for manipulation
    dataseries = load_data_from_json(json_file)
    print("Data series loaded successfully.")

    #Plot a graph of the timeseries
    #Note to self: Could we read the series name from the FRED file, and pass that title.
    plot_data_timeseries(dataseries, 10,5)
    input(f"Timeseries {series_id}. Press enter to continue...")

    #Frequency analysis 1: Distribution of yields
    bucket_size = 0.25
    yields_distribution = bucket_timeseries(dataseries, bucket_size)

    #Frequency analysis 2: Distribution of digits
    digit_distribution = analyse_digit_frequency(dataseries)

    #Plot histotgrams
    plot_histogram(yields_distribution, "10y Treasury yields (Frequency)", "Yield", "Count",
                   "green", bucket_size)
    input("Histogram of 10y UST yields. Press enter to continue...")

    #Histogram 2
    plot_histogram(digit_distribution, "Digits within yields (2dp)", "Digit", "Count",
                   "green", 1)
    input("Histogram of digit frequency. Press enter to end.")


if __name__ == "__main__":
    main()
