import time

def seconds_from_start():
    current_time = time.localtime()
    mins_till_next_hour = 60 - (int(time.strftime('%M', current_time)) + 1)
    secs_till_next_hour = (mins_till_next_hour * 60) + (60 - int(time.strftime('%S', current_time)))
    return secs_till_next_hour