import datetime
from datetime import timedelta
import time


datetimeFormat = '%b %d,%Y %H:%M:%S'
date1 = 'Oct 7,2017 16:09:50'
date2 = 'Sep 23,2016 13:54:40'
diff = datetime.datetime.strptime(date1, datetimeFormat) \
       - datetime.datetime.strptime(date2, datetimeFormat)

print("Difference:", diff)
print("Days:", diff.days)

print("Seconds:", diff.seconds)
