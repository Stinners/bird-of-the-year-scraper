import time 
import scraper 
import config

print("Running Bird of the Year Scraper")

if __name__ == "__main__":
    while True:
        scraper.do_scrape(config.url, config.outfile)
        time.sleep(config.period)

