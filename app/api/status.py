from enum import Enum 


RemoteStatus = Enum('RemoteStatus', [
    'COMPLETED', 
    'DOWNLOADING',
    'INACTIVE',
])


BetaStatus = Enum('BetaStatus', [
    'ENQUEUED',
    'PROCESSING',
    'NEEDS_INPUT',
    'FAILED',
    'COMPLETED', 
])
