
#* Dates - Python

# In Python, you can work with dates using the `datetime` module. Here is a description
# basic how to work with dates in Python:

#? Obtaining the Current Date and Time:

from datetime import datetime

# Get the current date and time
current_date = datetime.now()
print("Current date and time:", current_date)

#? Date Formatting:

# You can format a date into a text string using the `strftime` method.

# Format the date as a string
formatted_string = current_date.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_string)

#*Here are some common formatting codes:

#* - `%Y`:
# Year with four digits.
#* - `%m`:
# Month as number (01, 02, ..., 12).
#* - `%d`:
# Day of the month (01, 02, ..., 31).
#* - `%H`:
# Time (00, 01, ..., 23).
#* - `%M`:
# Minutes (00, 01, ..., 59).
#* - `%S`:
# Seconds (00, 01, ..., 59).

#? String Parsing to Date:

# You can convert a string to a date using the `strptime` method.

from datetime import datetime

# Parsing a string to date
date_string = "2022-11-15 12:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed date:", parsed_date)

#? Operations with Dates:

# You can perform mathematical operations on dates using the `timedelta` module.

from datetime import datetime, timedelta

# Add a day to the current date
one_day_later = current_date + timedelta(days=1)
print("Current date + one day:", one_day_later)

# Subtract a week from the current date
one_week_before = current_date - timedelta(weeks=1)
print("Current date - one week:", one_week_before)

#? Difference between Dates:

# You can calculate the difference between two dates using the subtraction operator.

from datetime import datetime

# Define two dates
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

# Calculate the difference
difference = end_date - start_date
print("Difference between dates:", difference)
print("Days difference:", difference.days)

#? Time Zones:

# If you need to work with time zones, you can use the `pytz` module.

from datetime import datetime
import pytz

# Get the current date and time in a specific time zone
timezone = pytz.timezone("America/New_York")
current_date_ny = datetime.now(timezone)
print("Current date and time in New York:", current_date_ny)

# Here are some basics on how to work with dates in Python using the module
# `datetime`. You can explore more features and options in the official Python documentation. Practice
# and experiment to strengthen your date handling skills in Python!.