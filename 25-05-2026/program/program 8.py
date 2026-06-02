#generate calendar
import calendar
year=int(input("enter the year:"))
month=int(input("enter month:"))
cal=calendar.month(year,month)
print(cal)
