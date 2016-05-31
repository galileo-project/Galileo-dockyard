from datetime import datetime
import time

def datetime_string(dt=None):
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y/%m/%d %H:%M:%S")

def timestamp():
    return time.time()