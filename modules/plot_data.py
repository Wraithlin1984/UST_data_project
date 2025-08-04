#Plot a single-series timeseries from the downloaded FRED data
#Vibecoding with ChatGPT

import matplotlib.pyplot as plt
from datetime import datetime

#Could generalise it but would then need more parameters for axis titles, colour etc.
def plot_data_timeseries(data):
    #Plots a single data series in a line chart

    #separate the dates and the data from FRED JSON
    dates = datetime.strptime(row[0], "%Y-%m-%d")

    for row in data:
        yields = [row[1] for row in data]

    #create the plot
    plt.figure(figsize=(10,5))          #10"x5"
    plt.plot(dates, yields, label="10Y Treasury Yield", colour="blue")
    plot.title("10y UST yields over time")
    plt.xlabel("Date")
    plt.ylabel("Yield (%)")
    plt.grid(True)
    plt.legend()

    #Show the chart
    plt.tight_layout()
    plt.show()