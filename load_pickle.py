# Load the dictionary back from the pickle file.
import pickle


class Job:
    def __init__(self, title, company, location, date, url):
        self.title = title
        self.company = company
        self.location = location
        self.date = date
        self.url = 'https://www.indeed.com' + url

    def __str__(self):
        return '{:<40} {:<50} {:<40} {}'.format(self.company, self.title, self.location, self.date)


def print_jobs(jobs):
    for k, job in enumerate(jobs):
        print('{}: {}'.format(k, job))
    print()

    for k, job in enumerate(jobs):
        print('{}: {}'.format(k, job.url))

jobs = pickle.load( open( "data_dump/jobs_2017-11-14_1337.p", "rb" ) )
print_jobs(jobs)