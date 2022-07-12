import os


class CommonConsts:
    ROOT_FOLDER = os.path.abspath(os.path.join(os.path.abspath(__file__), 3 * "../"))
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class MessageConsts:
    SUCCESS = "Success"
    VALIDATION_FAILED = "Validation failed"
    UNAUTHORIZED = "Unauthorized"
    BAD_REQUEST = "Bad request"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "Not found"
    CONFLICT = "Conflict"
    INVALID_OBJECT_ID = "Invalid object id"
    INTERNAL_SERVER_ERROR = "Unknown internal server error"
