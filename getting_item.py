import boto3

# Get the DynamoDB service resource
dynamodb = boto3.resource('dynamodb')

# Define the table you want to work with
table = dynamodb.Table('table1')

response = table.get_item(
    Key={
        'name': 'vijay',
        'ID': '3'
    }
)
item = response['Item']
print(item)