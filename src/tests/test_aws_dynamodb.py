from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
from app.entrypoints.example_handler import ExampleModel

from app.shared.aws_dynamodb import DynamoDBClient


class TestDynamoDBClient:
    def test_it_should_store_item(
        self, stub_dynamodb_resource: DynamoDBServiceResource
    ):
        client = DynamoDBClient[ExampleModel](stub_dynamodb_resource, "Example")
        entity = {"id": "1", "name": "john"}

        client.store(entity)

        assert client.find_by_id("id", "1") == entity

    def test_it_should_return_none_if_item_does_not_exist(
        self, stub_dynamodb_resource: DynamoDBServiceResource
    ):
        client = DynamoDBClient[ExampleModel](stub_dynamodb_resource, "Example")

        assert client.find_by_id("id", "-1") is None
