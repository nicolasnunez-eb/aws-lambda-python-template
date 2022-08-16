from typing import Generic, Literal, Mapping, Optional, TypeVar, Union, cast

import boto3
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource

session = boto3.Session()
dynamodb_resource = session.resource("dynamodb")


# You can statically type your tables
Table = Literal["Example"]

T = TypeVar("T", bound=Mapping)


class DynamoDBClient(Generic[T]):
    dynamo_resource: DynamoDBServiceResource

    def __init__(self, dynamo_resource: DynamoDBServiceResource, table_name: Table):
        self.dynamo_resource = dynamo_resource
        self.table = dynamo_resource.Table(table_name)

    def store(self, entity: T) -> None:
        """
        raises : botocore.exceptions.ClientError
        """
        self.table.put_item(Item=entity)

    def find_by_id(self, id_name: str, id: Union[str, int]) -> Optional[T]:
        try:
            item = self.table.get_item(Key={id_name: id})
            return cast(T, item["Item"])
        except KeyError:
            return None
