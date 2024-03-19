# import Library
import datetime

# current Date and Time
x = datetime.datetime.now()
print(x)

# year, month, day, hour, minute, second, and microsecond.

print("Year : ",x.year)
print("Month : ",x.month)
print("Day : ",x.day)


# Create a Date and Time
# For Creating Date Objects
x = datetime.datetime(2020, 5, 17) # time is optional parameter
print(x)


# strftime() Method
x = datetime.datetime.now()

print(x.strftime("%A")) # Full weekday name: Monday, Tuesday

print(x.strftime("%c")) # Local version of Date and Time
print(x.strftime("%x")) # Local version of Date
print(x.strftime("%X")) # local version of Time
# The `datetime` module in Python provides the `strftime()` method, which is used to format a datetime
# object into a string representation based on a specified format.


# For Day
print(x.strftime("%d")) # Date
print(x.strftime("%j")) # Day number in year


# For Week
print(x.strftime("%A")) # Week day name
print(x.strftime("%a")) # Short week day name
print(x.strftime("%w")) # Week day in number
print(x.strftime("%U")) # Week number in year
print(x.strftime("%W")) # Week number in year


# For Months
print(x.strftime("%b")) # Month short word 
print(x.strftime("%B")) # Month in words
print(x.strftime("%m")) # Month in number

# For Year
print(x.strftime("%y")) # Short Year
print(x.strftime("%Y")) # Year

# For Hours
print(x.strftime("%H")) # 24
print(x.strftime("%I")) # 12
print(x.strftime("%p")) # AM / PM


# For Minute
print(x.strftime("%M")) #Minute

# For Second
print(x.strftime("%S")) # Second
print(x.strftime("%f")) # Microsecond

# Time Zone
print(x.strftime("%z")) # UTC offset
print(x.strftime("%Z")) # Timezone
