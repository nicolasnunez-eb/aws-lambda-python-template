import json
from http import HTTPStatus

from app.shared.aws_lambda_io import api_gateway_response


def test_it_should_return_response_with_api_gateway_format():
    response = api_gateway_response(
        HTTPStatus.OK, body={"data": {"id": "1", "name": "scaloneta"}}
    )

    api_gateway_format = {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": json.dumps({"data": {"id": "1", "name": "scaloneta"}}),
    }
    assert response == api_gateway_format
