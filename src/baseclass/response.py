from jsonschema import validate

from src.emuns.global_emuns import GlobalErrorMessage


class Response:
    def __init__(self, response):
        self.response = response,
        self.response_json = response.json(),
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)

    def assert_status_code(self, statuscode):
        if isinstance(statuscode, list):
            assert self.response_status in statuscode, GlobalErrorMessage.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == statuscode, GlobalErrorMessage.WRONG_STATUS_CODE.value
        return self