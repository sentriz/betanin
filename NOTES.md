## line model


# rest
```
{
    index: <index>
    data: <data>
}
```

# socket
```
{
    torrentID: <torrent_id>
    line: {
		index: <index>
	    data: <data>
	}
}
```


# importing logic
| remote      | beta    | action                            |
|-------------|---------|-----------------------------------|
| downloading | unknown | beta = waiting                    |
| complete    | waiting | beta = enqueed; beta = processing |
