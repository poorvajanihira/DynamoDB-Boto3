import boto3
from boto3.dynamodb.conditions import Key, Attr

# Get the DynamoDB service resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('table1')
response = table.query(
    KeyConditionExpression=Key('name').eq('chandru')
)
items = response['Items']
print(items)
