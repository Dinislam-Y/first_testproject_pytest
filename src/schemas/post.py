# POST_SCHEMA = {
#     "type": "object",
#     "properties": {
#         "id": {"type": "number"},
#         "title": {"type": "string"}
#     },
#     "required": [id]
# }

POST_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name", "age"]
}
