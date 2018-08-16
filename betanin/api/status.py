from enum import Enum 


RemoteStatus = Enum('RemoteStatus', [
    'COMPLETED', 
    'DOWNLOADING',
    'INACTIVE',
    'UNKNOWN',
])


BetaStatus = Enum('BetaStatus', [
    'COMPLETED', 
    'ENQUEUED',
    'FAILED',
    'IGNORED',
    'NEEDS_INPUT',
    'PROCESSING',
    'UNKNOWN',
    'WAITING',
])
