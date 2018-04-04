"""
In shell:
set FLASK_APP=app/web_result.py
flask run
"""

from flask import Flask
from flask import render_template
from os import listdir
from os.path import isfile, join
import os
import time

from dal import db      # data access layer

app = Flask(__name__)

@app.route("/")                         # also landing page for now
@app.route("/intern")
def display_jobs(data=None):
    print("Fetching job from db...")
    start = time.time()

    jobs = db.get_jobs()
    end = time.time()
    print('Got result from db in {} seconds'.format(end - start))

    # Post processing
    fresh_jobs = []
    for job in jobs:
        index = job['location'].find('(')       # New York, NY 10005 (Financial District) -> strip part in ()
        if index > -1:
            job['location'] = job['location'][:index]
        fresh_jobs.append(job)

    # Take care of sorting via data table library in the front end
    # fresh_jobs = sorted(fresh_jobs, key=lambda job: job['location'].lower())
    # fresh_jobs = sorted(fresh_jobs, key=lambda job: job['company'].lower())
    # fresh_jobs = sorted(fresh_jobs, key=lambda job: job['date'])
    # for job in fresh_jobs:
    #     print(job['date'])

    return render_template('results.html', jobs_arr=fresh_jobs)

@app.route("/1")
def zzz(data=None):
    return render_template('example.html')


if __name__ == "__main__":
    if __name__ == '__main__':
        # Bind to PORT if defined, otherwise default to 5000.
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)