from bs4 import BeautifulSoup
import logging
from lib.job import Job


def _get_job(node):
    """
    Returns a Job object given the html node representing the record
    """
    job_title = node.find('a', {'class': 'turnstileLink'}).text
    job_title = ' '.join(job_title.split())

    url = node.find('a', {'class': 'turnstileLink'})['href']

    company = node.find('span', {'class': 'company'}).text
    company = ' '.join(company.split())

    location = node.find('span', {'class': 'location'}).text
    location = ' '.join(location.split())

    date = node.find('span', {'class': 'date'}).text
    date = ' '.join(date.split())

    return Job(job_title, company, location, date, url)


def parse_non_sponsored_jobs(html):
    """ Return a list of Job object ecluding sponsored jobs """
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()

    non_sponsored_result = []
    for r in soup.find_all('div', {'class': ['row', 'result']}):
        if r.find('span', {'class': 'sponsoredGray'}) is None:
            non_sponsored_result.append(r)

    jobs = []
    keywords = set(['software','developer','engineer','engineering'])
    for result in non_sponsored_result:
        try:
            job = _get_job(result)
        except Exception as e:
            logging.exception(e)
            continue

        found = False
        for keyword in keywords:
            if not found and 'intern' in job.title.lower() and keyword in job.title.lower():
                jobs.append(job)
                found = True
    return jobs