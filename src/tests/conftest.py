import os

import boto3
import moto
import pytest
from moto.core import patch_resource

from app.shared.aws_dynamodb import dynamodb_resource

# Moto config documentation
# http://docs.getmoto.org/en/latest/docs/getting_started.html#recommended-usage


@pytest.fixture(scope="session", autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"


@pytest.fixture(scope="session", autouse=True)
def stub_dynamodb_resource(aws_credentials):
    with moto.mock_dynamodb():
        patch_resource(dynamodb_resource)
        dynamodb_stub = boto3.resource("dynamodb")
        yield dynamodb_stub


@pytest.fixture(scope="session", autouse=True)
def tables_setup(stub_dynamodb_resource):
    """Create your dynamodb tables here"""
    stub_dynamodb_resource.create_table(
        AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": "S"},
        ],
        TableName="Example",
        KeySchema=[
            {"AttributeName": "id", "KeyType": "HASH"},
        ],
        BillingMode="PAY_PER_REQUEST",
    )
