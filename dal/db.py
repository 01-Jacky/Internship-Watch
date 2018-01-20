import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def get_jobs():
    jobs = []

    # Boto3 by default also looks in env variables for AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID
    dynamodb = boto3.resource(
        'dynamodb',
        region_name='us-west-2',
        endpoint_url="https://dynamodb.us-west-2.amazonaws.com"
    )

    table = dynamodb.Table('JobInternships')


    fe = Key('date').gte('2018-01-01')
    # pe = "#yr, title, info.rating"
    # Expression Attribute Names for Projection Expression only.
    # ean = { "#yr": "year", }
    esk = None

    response = table.scan(
        FilterExpression=fe,
        # ProjectionExpression=pe,
        # ExpressionAttributeNames=ean
        )

    for i in response['Items']:
        jobs.append(i)

    while 'LastEvaluatedKey' in response:
        response = table.scan(
            FilterExpression=fe,
            # ProjectionExpression=pe,
            # ExpressionAttributeNames= ean,
            ExclusiveStartKey=response['LastEvaluatedKey']
            )

        for i in response['Items']:
            jobs.append(i)

    return jobs


if __name__ == '__main__':
    jobs = get_jobs()
    for job in jobs:
        print(json.dumps(job, cls=DecimalEncoder))
        print(job['date'])
