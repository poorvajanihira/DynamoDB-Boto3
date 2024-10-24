import boto3

# Get the DynamoDB service resource
dynamodb = boto3.resource('dynamodb')

# Define the table you want to work with
table = dynamodb.Table('mytable')
table.delete()

print('Table deleted!')