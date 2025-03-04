import json
import boto3
from moto import mock_dynamodb

@mock_dynamodb
def test_lambda_handler():
    # Create a fake DynamoDB table
    dynamodb = boto3.client('dynamodb', region_name='eu-west-1')
    dynamodb.create_table(
        TableName="VisitorsTable",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}
    )

    # Import your Lambda function
    from lambda_function import lambda_handler

    # Call the Lambda function
    response = lambda_handler({}, {})

    # Assert that it returns the expected value
    assert response["statusCode"] == 200
