import boto3
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd

# Get the DynamoDB service resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('table1')
response = table.scan(
    FilterExpression=Attr('age').lt(33)
)
items = response['Items']

# Convert the items to a pandas DataFrame
df = pd.DataFrame(items)

# Save the DataFrame to a CSV file
output_file = 'output.csv'
df.to_csv(output_file, index=False)

print(f"Data successfully saved to {output_file}")