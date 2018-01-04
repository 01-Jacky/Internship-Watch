from __future__ import print_function # Python 2/3 compatibility
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

# DB connection
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")
table = dynamodb.Table('JobInternship')

# Data setup
company = "Google"
title = 'CEO'
DatePosted = '2017-12-31'

# Inserting record
try:
    response = table.get_item(
        Key={
            'Company': company,
            'JobTitle': title
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    if 'Item' in response:
        print('Item already exist')
    else:
        response = table.put_item(
            Item={
                'Company': company,
                'JobTitle': title,
                'DatePosted': DatePosted,
            }
        )
        print("PutItem succeeded:")
        print(json.dumps(response, indent=4, cls=DecimalEncoder))

