import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def get_json(response):
    return json.loads(response)


def validate_json(response, check_list):
    try:
        validate(instance=get_json(response), schema=check_list)
    except ValidationError as err:
        raise AssertionError(f"Invalid json schema! {err.args[0]}")
