"""
In shell:
set FLASK_APP=web_result.py
flask run
"""

from flask import Flask
from flask import render_template
import pickle
from os import listdir
from os.path import isfile, join
import os

from dal import db

app = Flask(__name__)

@app.route("/intern")
def display_jobs(data=None):
    print("Fetching job from db...")
    jobs = db.get_jobs()

    # discard >30 days
    fresh_jobs = [job for job in jobs]

    fresh_jobs = sorted(fresh_jobs, key=lambda job: job['location'].lower())
    fresh_jobs = sorted(fresh_jobs, key=lambda job: job['company'].lower())
    # jobs = sorted(jobs, key=lambda job : job.date.lower())

    return render_template('results.html', jobs_arr=fresh_jobs)

@app.route("/1")
def zzz(data=None):
    return render_template('example.html')


if __name__ == "__main__":
    if __name__ == '__main__':
        # Bind to PORT if defined, otherwise default to 5000.
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)