#-------------------------------
# logging functions
# abow-robot studio, 11/10/2019
#-------------------------------
import sys
import time
import logging

from .config import LOG 

def __log(message, level):
    # format the time stamp with millisecond
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y%m%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)

    # write into log file
    message_formated = '%s|%s: %s' % (time_stamp, logging._level_dict.get(level), message)
    with open(LOG['file'], "a") as f:
        f.write(message_formated + "\n")

    # print
    print(message_formated, file=sys.stderr)

def info(message):
    if(LOG['level'] > logging.INFO):
        return
    __log(message, logging.INFO)

def error(message):
    if(LOG['level'] > logging.ERROR):
        return
    __log(message, logging.ERROR)

def debug(message):
    if(LOG['level'] > logging.DEBUG):
        return
    __log(message, logging.DEBUG)

def warning(message):
    if(LOG['level'] > logging.WARNING):
        return
    __log(message, logging.WARNING)
