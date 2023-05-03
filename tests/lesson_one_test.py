import requests

from config import SERVICE_URL
from src.baseclass.response import Response
from src.schemas.post import POST_SCHEMA

url = requests.get(url=SERVICE_URL)
response = Response(url)


def test_status_code():
    response.assert_status_code(200).validate(POST_SCHEMA)

