# Internship-Watch

Quickly view, sort, search through list of latest cs related internship postings from indeed.com.  

## Getting Started 

Clone repo, setup virtualenv with prerequisites, and then its ready to start runuing locally ot be deployed to heroku.

### Prerequisites

1. Python 3.6

2. Boto3 for talking with DynamoDB

3. Flask

### Configuration

To talk to your DynamoDB instance, provide your AWS keys in environment variables under:
 
    AWS_ACCESS_KEY_ID 
    
    AWS_SECRET_ACCESS_KEY. 

Boto3 by default looks for those key names.

### Running locally


1. cd to root folder and in shell

    ```
    set FLASK_APP=web_result.py
    flask run
    ```


### Deplying to Heroku

Repo should already everything ready to deploy to heroku. If testing with heroku locally add a .env file with your AWS keys. 
    
    heroku create
    heroku apps:rename proj_name_here
    git push heroku master
 



