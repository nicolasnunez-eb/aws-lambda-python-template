import json
from http import HTTPStatus
from typing import Dict, Mapping, TypedDict, Union


class LambdaEvent(TypedDict):
    pathParameters: Dict[str, str]
    body: str


class EntityBody(TypedDict):
    data: Union[dict, list, Mapping]


class Error(TypedDict):
    code: str
    description: str


class ErrorBody(TypedDict):
    error: Error


class ApiGatewayResponse(TypedDict):
    headers: dict
    statusCode: int
    body: str


def api_gateway_response(
    status: HTTPStatus, body: Union[EntityBody, ErrorBody]
) -> ApiGatewayResponse:
    response: ApiGatewayResponse = {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": status.value,
        "body": json.dumps(body),
    }

    return response
