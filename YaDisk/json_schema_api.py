class YadiskSchemas:
    CREATE_FOLDER = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "href": {
                "type": "string"
            },
            "method": {
                "type": "string"
            },
            "templated": {
                "type": "boolean",
                "enum": [True, False]
            }
        },
        "required": [
            "href",
            "method",
            "templated"
        ]
    }

    GET_DOWNLOAD_LINK = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "operation_id": {
                "type": "string"
            },
            "href": {
                "type": "string"
            },
            "method": {
                "type": "string"
            },
            "templated": {
                "type": "boolean",
                "enum": [True, False]
            }
        },
        "required": [
            "operation_id",
            "href",
            "method",
            "templated"
        ]
    }

    RENAME_RESOURCE = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "href": {
                "type": "string"
            },
            "method": {
                "type": "string"
            },
            "templated": {
                "type": "boolean",
                "enum": [True, False]
            }
        },
        "required": [
            "href",
            "method",
            "templated"
        ]
    }
