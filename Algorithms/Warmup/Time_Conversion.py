import re

# time = input().strip()
time = '12:00:00AM'
m = re.match(r'(\d{2}):(\d{2}):(\d{2})(\w{2})', time)
hh = int(m.group(1))
mm = m.group(2)
ss = m.group(3)
apm = m.group(4)

if apm == 'PM' and hh != 12:
    hh += 12
if apm == 'AM' and hh == 12:
    hh = 0

print("%02d" % hh + ':' + mm + ':' + ss)
