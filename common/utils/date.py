# -*- coding: utf-8 -*-

import time
import datetime


def timestamp(date_str, format_str="%Y-%m-%d"):
    time_array = time.strptime(date_str, format_str)
    time_stamp = int(time.mktime(time_array))

    return time_stamp


def date(time_stamp=0, date_format='%Y-%m-%d %H:%M:%S'):
    time_stamp = int(time_stamp)
    time_array = time.localtime(time_stamp)

    return time.strftime(date_format, time_array)

