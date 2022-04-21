#import time
from datetime import date, datetime
#data_time = str(time.ctime(time.time()))
#import datetime as dt
#now = dt.datetime.now(dt.timezone.utc).astimezone()
#data_time_0 = str("%Y-%m-%d %H:%M:%S")
#data_time = f"{now:{data_time_0}}"
#print(data_time)

date_now  = datetime.now()
data_time = date_now.strftime("%Y-%m-%d %H:%M:%S")
print(data_time)
