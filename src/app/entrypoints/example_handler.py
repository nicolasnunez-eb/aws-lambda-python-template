from typing import TypedDict

from app.shared.aws_dynamodb import DynamoDBClient, dynamodb_resource


class ExampleModel(TypedDict):
    id: str
    name: str


def handle(event: dict, context: dict) -> dict:
    client = DynamoDBClient[ExampleModel](dynamodb_resource, "Example")
    client.find_by_id("id", "1")
    return {}
