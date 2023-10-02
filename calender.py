# import calender module
import calendar
  
text_cal = calendar.TextCalendar(firstweekday = 0)
  
year = int(input("Enter the year : "))
month = int(input("Enter the month : "))
width = 6
length = 2
  
# printing formatyear
print(text_cal.formatmonth(year,month, width, length))