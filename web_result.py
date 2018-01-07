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

from dal import db

app = Flask(__name__)

@app.route("/")
def hello(data=None):

    # Load the dictionary back from the pickle file.
    # jobs = pickle.load(open("data_dump/jobs_2017-12-24_0132.p", "rb"))
    # latest_file = ''
    # path = 'data_dump/'
    # for f in listdir(path):
    #     if isfile(join(path, f)) and f > latest_file:
    #         latest_file = path + f
    # jobs = pickle.load(open(latest_file, "rb"))
    # print(latest_file)

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

