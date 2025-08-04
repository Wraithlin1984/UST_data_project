#This measures the frequency of each digit in the yield data to check for randomness (or not)
#vibecoding with chatGPT

from collections import Counter
from operator import index


def analyse_digit_frequency(dataseries):
    #Counts the frequency of each digit (0-9) across the dataseries
    #data: list of date:yield pairs
    #Returns: Counter mapping digit -> count

    digits = []
    for _, value in dataseries:
        if value is not None:
            value_str = f"{value:.2f}"      #Value as a string with two "decimal points"

            for char in value_str:
                if char.isdigit():
                    digits.append(int(char))    #Add one to the counter
    unsorted_data = Counter(digits)

    print(sorted(unsorted_data.items(), key=lambda x:x[0]))         #DEBUGGING

    return Counter(digits)
