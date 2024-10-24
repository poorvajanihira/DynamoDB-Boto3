import boto3

# Get the DynamoDB service resource
dynamodb = boto3.resource('dynamodb')

# Define the table you want to work with
table = dynamodb.Table('table1')
table.update_item(
    Key={
        'name': 'sekar',
        'ID': '2'
    },
    UpdateExpression='SET active = :val1',
    ExpressionAttributeValues={
        ':val1': False
    }
)
print('Updated successfully!')