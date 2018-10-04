import matplotlib.pyplot as plt

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

def get_top(data, num):
    # Sort the birds by their most recent vote
    data.sort(key=lambda bird: bird[-1], reverse=True)
    return data[:num]

def make_plot(birds):
    names = [bird[0] for bird in birds]
    votes = [bird[1:] for bird in birds]
    xs = range(len(votes[0]))
    for name, bird_votes in zip(names, votes):
        plt.plot(xs, bird_votes, label=name)
    plt.legend(loc="best")
    plt.show()

def plot(filename, num):
    times, data = get_data(filename)
    top_birds = get_top(data, num)
    make_plot(top_birds)

