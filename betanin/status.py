# standard library
from enum import Enum


Status = Enum(
    "Status",
    [
        "COMPLETED",
        "ENQUEUED",
        "FAILED",
        "IGNORED",
        "NEEDS_INPUT",
        "PROCESSING",
    ],
)
