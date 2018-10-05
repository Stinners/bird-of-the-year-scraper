import matplotlib.pyplot as plt
from datetime import datetime

from config import outfile, date_format

# Read the data from the csv file
def get_data(filename):
    times = []
    birds = []
    with open(filename, "r") as f:

        # Get the names from the first line 
        birds = f.readline().strip(",\n").split(",")[1:]
        birds = [[name] for name in birds]

        # Now iterate through the other lines 
        for line in f.readlines():
            elems = line.strip(",\n").split(",")
            times.append(elems[0])
            [bird.append(float(vote)) for bird, vote in zip(birds, elems[1:])]

    return times, birds

# Calculates the difference between two times in hours 
# Times should be in YYYY-MM-DD HH-MM format
def time_diff(start, stop):
    start = datetime.strptime(start, date_format)
    stop = datetime.strptime(stop, date_format)
    diff = stop - start
    # This will cause problems if the difference is greater than a day
    hours = diff.seconds / 60 / 61
    hours += diff.days * 24
    return hours

def get_top(data, num):
    # Sort the birds by their most recent vote
    data.sort(key=lambda bird: bird[-1], reverse=True)
    return data[:num]

def make_plot(birds, times):
    names = [bird[0] for bird in birds]
    votes = [bird[1:] for bird in birds]
    time_diffs = [time_diff(times[0], time) for time in times]
    print(time_diffs)
    for name, bird_votes in zip(names, votes):
        plt.plot(time_diffs, bird_votes, label=name)
    plt.legend(loc="best")
    plt.show()

def plot(filename, num):
    times, data = get_data(filename)
    top_birds = get_top(data, num)
    make_plot(top_birds, times)

if __name__ == "__main__":
    plot(outfile, 10)
