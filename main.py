import time 
import scraper 

period = 60 * 60 * 2
outfile = "bird_votes.csv"
url = "http://birdoftheyear.org.nz/"

print("Running Bird of the Year Scraper")

while True:
    scraper.do_scrape(url, outfile)
    time.sleep(period)

