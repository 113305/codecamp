#4.2
from datetime import datetime
now = datetime.now()
print now

#4.3
from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day
print current_year
print current_month
print current_day

#4.4
from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.year, now.month, now.day)

#4.5
from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute, now.second)

#4.6
from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
