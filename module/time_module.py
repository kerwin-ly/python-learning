
import time
from datetime import datetime

seconds = time.localtime().tm_sec
print(time.localtime(), seconds)


now = datetime.now()
timestamp = now.timestamp() # milliseconds
new_now = datetime.fromtimestamp(timestamp) # yyyy-mm-dd hh:MM:ss
print(now) # yyyy-mm-dd hh:MM:ss
print(now.timestamp())