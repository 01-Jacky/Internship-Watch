import time
import pickle
import datetime
import random
import os
from bs4 import BeautifulSoup


from lib.job import Job
import lib.downloader
import lib.parser


def print_jobs(jobs):
    jobs = sorted(jobs, key=lambda job : job.company.lower())
    jobs = sorted(jobs, key=lambda job : job.date.lower())
    jobs = sorted(jobs, key=lambda job : job.location.lower())

    for k, job in enumerate(jobs):
        print('{:<2}: {}'.format(k, job))
    print()

map = {}
# Parse the soup
if __name__ == '__main__':
    jobs = []
    for k, i in enumerate(range(0,1000, 10)):
        # url = 'https://www.indeed.com/jobs?q=software+intern&l=United+States&sort=date&start=' + str(i)
        # url = 'https://www.indeed.com/jobs?q=computer+science+intern&l=United+States&sort=date&start=' + str(i)
        url = 'https://www.indeed.com/jobs?q=computer+science+intern&l=United+States&start=' + str(i)
        # url = 'https://www.indeed.com/jobs?q=computer+science+intern&l=San+Francisco%2C+CA&radius=100&sort=date&start=' + str(i)

        print('Scraping page ' + str(k + 1))
        html = lib.downloader.get_html(url)
        jobs.extend(lib.parser.parse_non_sponsored_jobs(html))
        time.sleep(random.uniform(0.5,1.5))

    # Save jobs to disc
    if not os.path.exists('data_dump'):
        os.makedirs('data_dump')

    picke_name = "data_dump/jobs_{}.p".format(datetime.datetime.today().strftime('%Y-%m-%d_%H%M'))
    pickle.dump(jobs, open(picke_name, "wb" ))
    print_jobs(jobs)

