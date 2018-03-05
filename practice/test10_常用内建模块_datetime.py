#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 常用内建模块->datetime
# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    m_dt = re.match(r'\d{4}-\d{1,2}-\d{1,2}\s+\d{1,2}:\d{1,2}:\d{1,2}', dt_str) # 没判断时间超过60的情况，太长了
    if m_dt is None:
        raise AttributeError('bad arg dt_str')
    m_tz = re.match(r'UTC([+-])(\d+):([0-9]{2})', tz_str)
    if m_tz is None:
        raise AttributeError('bad arg tz_str')
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')  # 格式化输入字符串
    symbol = m_tz.group(1)
    hour = int(m_tz.group(2))
    hour_int = int(symbol + str(hour))
    minute = int(m_tz.group(3))
    minute_int = int(symbol + str(minute))
    tz_utc = timezone(timedelta(hours=hour_int, minutes=minute_int)) # 创建时区
    dt_utc = dt.replace(tzinfo=tz_utc)  # 设置为指定UTC时间
    return dt_utc.timestamp()  # 把datetime转换为timestamp

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')