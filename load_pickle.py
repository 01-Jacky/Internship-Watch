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
        google_link = 'https://www.google.com/search?q={}'.format('+'.join(self.company.split() + ["intern", "salary"]))
        return '{:<35} {:<50} {:<35} {:<15} {:<70} {}'.format(
            self.company, self.title[:45], self.location[:30], self.date, google_link, self.url)


def print_jobs(jobs):
    jobs = sorted(jobs, key=lambda job : job.company.lower())
    jobs = sorted(jobs, key=lambda job : job.location.lower())
    # jobs = sorted(jobs, key=lambda job : job.date.lower())

    for k, job in enumerate(jobs):
        print('{:<2}: {}'.format(k, job))
    print()



jobs = pickle.load( open( "data_dump/jobs_2017-12-17_2139.p", "rb" ) )
print_jobs(jobs)