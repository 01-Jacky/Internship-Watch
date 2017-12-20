from flask import Flask
from flask import render_template
import pickle

app = Flask(__name__)

@app.route("/")
def hello(data=None):
    # Load the dictionary back from the pickle file.
    jobs = pickle.load(open("data_dump/jobs_2017-12-19_2258.p", "rb"))

    # discard >30 days
    fresh_jobs = [job for job in jobs if job.date != '30+ days ago']

    fresh_jobs = sorted(fresh_jobs, key=lambda job: job.location.lower())
    fresh_jobs = sorted(fresh_jobs, key=lambda job: job.company.lower())
    # jobs = sorted(jobs, key=lambda job : job.date.lower())

    return render_template('results.html', jobs_arr=fresh_jobs)

@app.route("/1")
def zzz(data=None):
    return render_template('example.html')

