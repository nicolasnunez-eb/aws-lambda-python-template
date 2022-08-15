from http import HTTPStatus
from typing import TypedDict

from app.shared.aws_dynamodb import DynamoDBClient, dynamodb_resource

from ..shared.aws_lambda_io import ApiGatewayResponse, LambdaEvent, api_gateway_response


class ExampleModel(TypedDict):
    id: str
    name: str


def handle(event: LambdaEvent, context: dict) -> ApiGatewayResponse:
    client = DynamoDBClient[ExampleModel](dynamodb_resource, "Example")
    entity = client.find_by_id("id", "1")
    if not entity:
        return api_gateway_response(
            HTTPStatus.NOT_FOUND,
            {
                "error": {
                    "code": "NOT_FOUND",
                    "description": "Example entity does not exist",
                }
            },
        )
    return api_gateway_response(HTTPStatus.OK, {"data": entity})
