import json
from http import HTTPStatus
from unittest.mock import Mock, patch

import pytest
from botocore.exceptions import ClientError

from app.entrypoints.example_handler import ExampleModel, handle


class TestLambdaHandler:
    @pytest.fixture(scope="function", autouse=True)
    def mock_dynamodb_client(self):
        """
        Example of how to mock the DynamoDBClient class
        We need to mock the '__getitem__()()' because of the generic
        instantiation of the class
        """
        with patch("app.entrypoints.example_handler.DynamoDBClient") as client:
            yield client.__getitem__()()

    def test_it_should_raise_exception_when_dynamo_fails(self, mock_dynamodb_client):
        mock_dynamodb_client.find_by_id.side_effect = ClientError(
            error_response={}, operation_name="GetItem"
        )

        with pytest.raises(ClientError):
            handle(
                event={},
                context={},
            )

    def test_it_should_return_not_found_when_entity_does_not_exist(
        self,
        mock_dynamodb_client: Mock,
    ):
        mock_dynamodb_client.find_by_id.return_value = None

        response = handle(
            event={},
            context={},
        )

        assert response["statusCode"] == HTTPStatus.NOT_FOUND.value
        assert response["body"] == json.dumps(
            {
                "error": {
                    "code": "NOT_FOUND",
                    "description": "Example entity does not exist",
                }
            }
        )

    def test_it_should_return_ok_with_example_item(
        self,
        mock_dynamodb_client: Mock,
    ):
        mock_dynamodb_client.find_by_id.return_value = ExampleModel(
            {"id": "1", "name": "John"}
        )

        response = handle(
            event={},
            context={},
        )

        assert response["statusCode"] == HTTPStatus.OK.value
        assert response["body"] == json.dumps({"data": {"id": "1", "name": "John"}})
