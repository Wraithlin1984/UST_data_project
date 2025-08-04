#The Main

from modules.fetch_data import download_us_yields
from modules.ingest_data import load_data_from_json
from modules.plot_data import plot_data_timeseries
from modules.frequency_distribution import bucket_timeseries
from modules.frequency_distribution import plot_histogram
from modules.digit_frequency import analyse_digit_frequency

def main():
    #Download, save as local, and ingest the data
    json_file = download_us_yields("f889f763982c5a97c15dd61f752b7d15")
    print("File saved successfully to: {json_file}")

    dataseries = load_data_from_json(json_file)
    print("Data series loaded successfully.")

    #Plot a graph of the timeseries
    plot_data_timeseries(dataseries, 10,5)
    input("Timeseries of 10y UST yields. Press enter to continue...")

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
