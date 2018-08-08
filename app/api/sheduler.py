import threading


def _worker():
    while True:
        transmission.find_jobs()
        time.sleep(5)


def start_worker():
    thread = threading.Thread(target=_worker)
    thread.start()
