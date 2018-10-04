import bs4 
import urllib.request 
import os 
import datetime

# Returns a tuple in the form (name, votes)
def process_bird(bird_node):
    name = bird_node.find("h3").text 

    votes = bird_node.find("div", {"class": "voting-result"}).text
    votes = votes.strip().split()[0]

    return name, votes

def write_series(data, file):
    for elem in data:
        file.write(elem)
        file.write(",")
    file.write("\n")

def write_to_csv(bird_data, filename):
    
    # Check if the file exists 
    # And if it doesn't write the name headers
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            names = [bird[0] for bird in bird_data]
            names = ["Times"] + names
            write_series(names, f)

    #Write the voting data
    with open(filename, "a") as f:
        # Get current time in format YYYY-MM-DD HH-MM
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        votes = [bird[1] for bird in bird_data]
        votes = [timestamp] + votes
        write_series(votes, f)

def fetch_data(url):
    html = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # Get a lost of soups each corresponding to the part of the 
    # page displaying a single bird
    bird_nodes = soup.findAll("div", {"class": "node-bird"})
    
    return [process_bird(bird) for bird in bird_nodes]

def do_scrape(url, filename):
    data = fetch_data(url)
    write_to_csv(data, filename)
    return(data)

if __name__ == "__main__":
    do_scrape(outfile)
