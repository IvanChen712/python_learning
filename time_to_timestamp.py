import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz = re.match(r'^UTC([+-]\d{1,2}):(\d{2})$', tz_str)
    tz_hour = int(tz.group(1))
    tz_minute = int(tz.group(2))
    dt = dt.replace(tzinfo=timezone(timedelta(hours=tz_hour, minutes=tz_minute)))
    return dt.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
