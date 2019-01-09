# python
from enum import Enum

# betanin
from betanin.extensions import db


Status = Enum('Status', [
    'COMPLETED',
    'ENQUEUED',
    'FAILED',
    'IGNORED',
    'NEEDS_INPUT',
    'PROCESSING',
])
