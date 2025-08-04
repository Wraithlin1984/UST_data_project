#Plot a single-series timeseries from the downloaded FRED data
#Vibecoding with ChatGPT

import matplotlib.pyplot as plt
from datetime import datetime

#Could generalise it but would then need more parameters for axis titles, colour etc.
def plot_data_timeseries(data, figure_width, figure_height):
    #Plots a single data series in a line chart

    #separate the dates and the data from FRED JSON
    dates = [datetime.strptime(row[0], "%Y-%m-%d") for row in data]
    yields = [row[1] for row in data]

    #for i in range(10):                    #Debugging
    #    print(dates[i], yields[i])

    #create the plot
    plt.figure(figsize=(figure_width,figure_height))          #10"x5"
    plt.plot(dates, yields, label="10Y Treasury Yield", color="blue")   #Note: Stupid american spellings
    plt.title("10y UST yields over time")
    plt.xlabel("Date")
    plt.ylabel("Yield (%)")
    plt.grid(True)
    plt.legend()

    #Show the chart
    plt.tight_layout()
    plt.show()