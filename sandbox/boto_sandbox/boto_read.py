from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
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


dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")

table = dynamodb.Table('Music')

Company = "1"
JobTitle = "CEO"

try:
    response = table.get_item(
        Key={
            'Company': Company,
            'JobTitle': JobTitle
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    if 'Item' in response:
        print(len(response))
        print(len(response['Item']))
        item = response['Item']
        print("GetItem succeeded:")
        print(json.dumps(item, indent=4, cls=DecimalEncoder))
    else:
        print('Item not found')

