import datetime

def getCurrentTime( frm ="%Y-%m-%d %H:%M:%S"):
    dt = datetime.datetime.now()     #当前时间
    return dt.strftime( frm )