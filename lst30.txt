>>> import datetime
>>> ts1 = '2016-04-09 17:36:47'
>>> dt1 = datetime.datetime.strptime(ts1, '%Y-%m-%d %H:%M:%S')
>>> dt1
datetime.datetime(2016, 4, 9, 17, 36, 47)
>>> ts2 = '2016-04-11 09:11:13'
>>> dt2 = datetime.datetime.strptime(ts2, '%Y-%m-%d %H:%M:%S')
>>> dt2
datetime.datetime(2016, 4, 11, 9, 11, 13)
>>> td = dt2-dt1
>>> td
datetime.timedelta(1, 56066)
>>> print td
1 day, 15:34:26