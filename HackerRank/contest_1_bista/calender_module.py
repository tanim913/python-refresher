import calendar

weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
mm, dd, yy = map(int, input().split(' '))

print(weekdays[calendar.weekday(yy, mm, dd)].upper())
