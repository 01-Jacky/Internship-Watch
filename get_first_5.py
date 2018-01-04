import time
import pickle
import datetime
import random
import os
from bs4 import BeautifulSoup


from lib.job import Job
import lib.downloader
import lib.parser

# boto3
import boto3
import json
import decimal
from botocore.exceptions import ClientError


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def print_jobs(jobs):
    jobs = sorted(jobs, key=lambda job : job.company.lower())
    jobs = sorted(jobs, key=lambda job : job.date.lower())
    jobs = sorted(jobs, key=lambda job : job.location.lower())

    for k, job in enumerate(jobs):
        print('{:<2}: {}'.format(k, job))
    print()


# Parse the soup
if __name__ == '__main__':
    jobs = []
    for k, i in enumerate(range(0,20, 10)):
        # url = 'https://www.indeed.com/jobs?q=software+intern&l=United+States&sort=date&start=' + str(i)
        # url = 'https://www.indeed.com/jobs?q=computer+science+intern&l=United+States&sort=date&start=' + str(i)
        url = 'https://www.indeed.com/jobs?q=software+intern&l=United+States&start=' + str(i)
        # url = 'https://www.indeed.com/jobs?q=computer+science+intern&l=United+States&start=' + str(i)
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

    # Save job to db
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")
    table = dynamodb.Table('JobInternships')

    for job in jobs:
        jobid = job.company.replace(' ', '') + '_' + job.title.replace(' ','')

        try:
            response = table.get_item(
                Key={
                    'date': job.date,
                    'jobID': jobid,
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            if 'Item' in response:                      # If item exist
                print('Item already exist')
            else:                                       # If not insert it
                print('Inserting...')
                response = table.put_item(
                    Item={
                        'date': job.date,
                        'jobID': jobid,
                        'company': job.company,
                        'title': job.title,
                        'location': job.location,
                        'url': job.url,
                    }
                )
                # print("PutItem succeeded:")
                # print(json.dumps(response, indent=4, cls=DecimalEncoder))



