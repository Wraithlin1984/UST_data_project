#Bucket the yields and measure the frequency distribution
#Videcoding with chatGPT

from matplotlib import pyplot as plt
from collections import Counter
import math

def bucket_timeseries(timeseries_data, bucket_size=0.25):
    #Bucket Yield data into fixed intervals, default size is 0.25
    #Yield_data is a list of date:yield pairs
    #Returns: Counter mapping bucket -> count. Sorted on bucket size.

    buckets = []
    for _, value in timeseries_data:
        if value is not None:
            bucket = math.floor(value / bucket_size)*bucket_size
            buckets.append(round(bucket,2))
    unsorted_counter = Counter(buckets)
    #print(sorted(unsorted_counter.items(), key = lambda x:x[0]))                 #Debugging

    return sorted(unsorted_counter.items(), key = lambda x:x[0])

def plot_histogram(data_counts, title = "Frequency Distribution", xlabel = "Value", ylabel = "Count",
                   bar_color = "blue", bar_width = 1):
    #Generic Histograph plotting function
    #data_counts: list of (bucket, count) as pairs OR Counter
    #title, xlabel, ylabel
    #bar_width, bar_colour

    #Handle both counter and list-of-tuples
    if isinstance(data_counts, dict):
        keys = sorted(data_counts.keys())
        values = [data_counts[k] for k in keys]
    else:
        keys, values = zip(*data_counts)

    plt.figure(figsize = (10,5))
    plt.bar(keys, values, width = bar_width, color = bar_color, align = "center")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, axis = "y", linestyle = "--")

    plt.tight_layout()
    plt.show()

