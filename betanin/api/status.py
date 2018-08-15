from enum import Enum 


RemoteStatus = Enum('RemoteStatus', [
    'COMPLETED', 
    'DOWNLOADING',
    'INACTIVE',
    'UNKNOWN',
])


BetaStatus = Enum('BetaStatus', [
    'ENQUEUED',
    'PROCESSING',
    'NEEDS_INPUT',
    'FAILED',
    'COMPLETED', 
    'UNKNOWN',
])
