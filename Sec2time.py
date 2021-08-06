from datetime import timedelta

sec = int(input("please write your second: "))
print('Time in Seconds:', sec)

td = timedelta(seconds=sec)
print('Time in hh:mm:ss:', td)