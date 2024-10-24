import boto3

# Get the DynamoDB service resource
dynamodb = boto3.resource('dynamodb')

# Define the table you want to work with
table = dynamodb.Table('table1')  # Make sure 'table1' exists in your DynamoDB

# Insert an item into the table
table.put_item(
   Item={
        'name': 'vijay',
        'ID': '3',
        'age': 33,
        'active': True
   }
)
table.put_item(
   Item={
        'name': 'poorvaja',
        'ID': '4',
        'age': 3,
        'active': True
   }
)

print("Items added successfully!")