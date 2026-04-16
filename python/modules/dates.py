# Date Module in Python
# The datetime module provides classes for manipulating dates and times.
# Main classes: datetime, date, time, timedelta

from datetime import datetime, date, time, timedelta

# Basic Date Operations
# Get current date
today = date.today()
print(f"Today: {today}")  # Output - Today: 2026-04-15

# Get current date and time
now = datetime.now()
print(f"Now: {now}")  # Output - Now: 2026-04-15 HH:MM:SS.ffffff

# Create a specific date
specific_date = date(2025, 12, 25)
print(f"Christmas 2025: {specific_date}")  # Output - Christmas 2025: 2025-12-25

# Create a specific date and time
specific_datetime = datetime(2025, 12, 25, 15, 30, 45)
print(f"Specific datetime: {specific_datetime}")  # Output - Specific datetime: 2025-12-25 15:30:45

# Create a specific time
specific_time = time(14, 30, 0)
print(f"Time: {specific_time}")  # Output - Time: 14:30:00

# Date Components (Attributes)
date_obj = date(2026, 4, 15)
print(f"Year: {date_obj.year}")  # Output - Year: 2026
print(f"Month: {date_obj.month}")  # Output - Month: 4
print(f"Day: {date_obj.day}")  # Output - Day: 15

# DateTime Components
dt = datetime(2026, 4, 15, 14, 30, 45)
print(f"Hour: {dt.hour}")  # Output - Hour: 14
print(f"Minute: {dt.minute}")  # Output - Minute: 30
print(f"Second: {dt.second}")  # Output - Second: 45
print(f"Microsecond: {dt.microsecond}")  # Output - Microsecond: 0

# Day of Week
date_obj = date(2026, 4, 15)
print(f"Day of week: {date_obj.weekday()}")  # Output - 0 (Monday is 0, Sunday is 6)
print(f"Day name: {['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][date_obj.weekday()]}")  # Output - Wed

# ISO Calendar
print(f"ISO calendar: {date_obj.isocalendar()}")  # Output - (year, week, weekday)

# Date Arithmetic with timedelta
today = date.today()
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
next_month = today + timedelta(days=30)
next_year = today + timedelta(days=365)

print(f"Today: {today}")  # Output - Today: 2026-04-15
print(f"Tomorrow: {tomorrow}")  # Output - Tomorrow: 2026-04-16
print(f"Next week: {next_week}")  # Output - Next week: 2026-04-22
print(f"Next month (approx): {next_month}")  # Output - Next month (approx): 2026-05-15
print(f"Next year: {next_year}")  # Output - Next year: 2027-04-15

# Subtracting Dates
date1 = date(2026, 4, 20)
date2 = date(2026, 4, 15)
difference = date1 - date2
print(f"Days between: {difference.days}")  # Output - Days between: 5

# DateTime Arithmetic
now = datetime.now()
future = now + timedelta(hours=2, minutes=30)
past = now - timedelta(days=1)
print(f"Now: {now}")
print(f"2.5 hours later: {future}")
print(f"1 day earlier: {past}")

# Timedelta Examples
td = timedelta(days=1, hours=2, minutes=30, seconds=15)
print(f"Timedelta: {td}")  # Output - Timedelta: 1 day, 2:30:15
print(f"Total seconds: {td.total_seconds()}")  # Output - Total seconds: 95415.0

# Multiple Timedeltas
td1 = timedelta(days=1)
td2 = timedelta(hours=3)
combined = td1 + td2
print(f"Combined: {combined}")  # Output - Combined: 1 day, 3:00:00

# String Formatting with strftime
date_obj = date(2026, 4, 15)
dt_obj = datetime(2026, 4, 15, 14, 30, 45)

print(dt_obj.strftime("%Y-%m-%d"))  # Output - 2026-04-15
print(dt_obj.strftime("%d/%m/%Y"))  # Output - 15/04/2026
print(dt_obj.strftime("%A, %B %d, %Y"))  # Output - Wednesday, April 15, 2026
print(dt_obj.strftime("%H:%M:%S"))  # Output - 14:30:45
print(dt_obj.strftime("%I:%M %p"))  # Output - 02:30 PM
print(dt_obj.strftime("%Y-%m-%d %H:%M:%S"))  # Output - 2026-04-15 14:30:45
print(dt_obj.strftime("%A"))  # Output - Wednesday
print(dt_obj.strftime("%B"))  # Output - April
print(dt_obj.strftime("%c"))  # Output - Wed Apr 15 14:30:45 2026

# Parse String to Date with strptime
date_string = "2026-04-15"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")  # Output - Parsed date: 2026-04-15 00:00:00
print(f"Type: {type(parsed_date)}")  # Output - Type: <class 'datetime.datetime'>

# Parse Various Date Formats
date_formats = [
    ("15-04-2026", "%d-%m-%Y"),
    ("04/15/2026", "%m/%d/%Y"),
    ("2026.04.15", "%Y.%m.%d"),
    ("April 15, 2026", "%B %d, %Y"),
    ("15 Apr 2026", "%d %b %Y")
]

for date_str, fmt in date_formats:
    parsed = datetime.strptime(date_str, fmt)
    print(f"{date_str:20} -> {parsed.date()}")

# Compare Dates
date1 = date(2026, 4, 15)
date2 = date(2026, 4, 20)
date3 = date(2026, 4, 15)

print(f"date1 == date3: {date1 == date3}")  # Output - True
print(f"date1 < date2: {date1 < date2}")  # Output - True
print(f"date1 > date2: {date1 > date2}")  # Output - False
print(f"date1 <= date2: {date1 <= date2}")  # Output - True
print(f"date1 != date2: {date1 != date2}")  # Output - True

# Get Min and Max Dates
dates = [date(2026, 4, 10), date(2026, 4, 5), date(2026, 4, 20), date(2026, 4, 15)]
print(f"Earliest date: {min(dates)}")  # Output - Earliest date: 2026-04-05
print(f"Latest date: {max(dates)}")  # Output - Latest date: 2026-04-20

# Sort Dates
dates_sorted = sorted(dates)
print(f"Sorted dates: {dates_sorted}")  # Output - Sorted dates: [2026-04-05, 2026-04-10, 2026-04-15, 2026-04-20]

# Case Study: Calculate Age
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birth = date(1995, 5, 15)
age = calculate_age(birth)
print(f"Age: {age}")  # Output - Age: 31 (in 2026)

# Case Study: Days Until Event
def days_until(event_date):
    today = date.today()
    if event_date >= today:
        return (event_date - today).days
    else:
        return None

christmas = date(2026, 12, 25)
days_left = days_until(christmas)
print(f"Days until Christmas: {days_left}")  # Output - Days until Christmas: 254 (approx)

# Case Study: Check if Leap Year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(f"2024 is leap year: {is_leap_year(2024)}")  # Output - True
print(f"2025 is leap year: {is_leap_year(2025)}")  # Output - False
print(f"2000 is leap year: {is_leap_year(2000)}")  # Output - True

# Case Study: Get Day of Month
def get_days_in_month(year, month):
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    last_day = next_month - timedelta(days=1)
    return last_day.day

print(f"Days in Feb 2026: {get_days_in_month(2026, 2)}")  # Output - 28
print(f"Days in Apr 2026: {get_days_in_month(2026, 4)}")  # Output - 30

# Case Study: Business Days Between Dates
def count_business_days(start_date, end_date):
    count = 0
    current = start_date
    while current <= end_date:
        if current.weekday() < 5:  # 0-4 are Monday-Friday
            count += 1
        current += timedelta(days=1)
    return count

start = date(2026, 4, 1)
end = date(2026, 4, 10)
business_days = count_business_days(start, end)
print(f"Business days: {business_days}")  # Output - Business days: 8

# Case Study: Weekend Dates
def get_weekend_dates(start_date, end_date):
    weekends = []
    current = start_date
    while current <= end_date:
        if current.weekday() >= 5:  # Saturday=5, Sunday=6
            weekends.append(current)
        current += timedelta(days=1)
    return weekends

start = date(2026, 4, 1)
end = date(2026, 4, 15)
weekends = get_weekend_dates(start, end)
print(f"Weekend dates in April: {weekends[:3]}")  # Output - First 3 weekend dates

# Case Study: Generate Date Range
def date_range(start_date, end_date):
    current = start_date
    while current <= end_date:
        yield current
        current += timedelta(days=1)

start = date(2026, 4, 1)
end = date(2026, 4, 5)
for d in date_range(start, end):
    print(d, end=" ")  # Output - 2026-04-01 2026-04-02 2026-04-03 2026-04-04 2026-04-05
print()

# Case Study: Recurring Events
def get_monthly_occurrences(start_date, month_count):
    dates = []
    current = start_date
    for _ in range(month_count):
        dates.append(current)
        # Go to next month
        if current.month == 12:
            current = current.replace(year=current.year + 1, month=1)
        else:
            current = current.replace(month=current.month + 1)
    return dates

monthly_dates = get_monthly_occurrences(date(2026, 1, 15), 6)
for d in monthly_dates:
    print(d)
# Output - Monthly dates from Jan to Jun 2026

# Case Study: Check if Date is Within Range
def is_date_in_range(check_date, start_date, end_date):
    return start_date <= check_date <= end_date

date_to_check = date(2026, 4, 15)
range_start = date(2026, 4, 1)
range_end = date(2026, 4, 30)
is_in_range = is_date_in_range(date_to_check, range_start, range_end)
print(f"Date in range: {is_in_range}")  # Output - True

# Case Study: Parse and Format Combined
date_string = "2026-04-15"
parsed = datetime.strptime(date_string, "%Y-%m-%d")
formatted = parsed.strftime("%A, %B %d, %Y")
print(f"Formatted: {formatted}")  # Output - Formatted: Wednesday, April 15, 2026

# Case Study: Time Duration Calculation
def format_duration(td):
    days, remainder = divmod(int(td.total_seconds()), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"

duration = timedelta(days=2, hours=3, minutes=30, seconds=15)
print(f"Duration: {format_duration(duration)}")  # Output - Duration: 2d 3h 30m 15s

# Case Study: Event Schedule
events = {
    "New Year": date(2026, 1, 1),
    "Valentine's Day": date(2026, 2, 14),
    "St. Patrick's Day": date(2026, 3, 17),
    "Independence Day": date(2026, 7, 4),
    "Halloween": date(2026, 10, 31),
    "Christmas": date(2026, 12, 25)
}

today = date.today()
upcoming = {name: (event_date - today).days for name, event_date in events.items() 
            if event_date >= today}

for event, days_left in sorted(upcoming.items(), key=lambda x: x[1]):
    print(f"{event}: {days_left} days away")
# Output - Upcoming events with days remaining

# Case Study: Relative Date Descriptions
def describe_relative_date(target_date):
    today = date.today()
    diff = (target_date - today).days
    
    if diff == 0:
        return "Today"
    elif diff == 1:
        return "Tomorrow"
    elif diff == -1:
        return "Yesterday"
    elif diff > 1:
        return f"In {diff} days"
    elif diff < -1:
        return f"{-diff} days ago"

dates_to_describe = [
    date.today(),
    date.today() + timedelta(days=1),
    date.today() - timedelta(days=1),
    date.today() + timedelta(days=5),
    date.today() - timedelta(days=3)
]

for d in dates_to_describe:
    print(f"{d}: {describe_relative_date(d)}")
# Output - Relative descriptions of dates

# Case Study: Week of the Year
def get_week_of_year(d):
    return d.isocalendar()[1]

test_date = date(2026, 4, 15)
week = get_week_of_year(test_date)
print(f"Week of year: {week}")  # Output - Week of year: 16

# Case Study: First and Last Day of Month
def first_day_of_month(d):
    return d.replace(day=1)

def last_day_of_month(d):
    if d.month == 12:
        next_month = d.replace(year=d.year + 1, month=1, day=1)
    else:
        next_month = d.replace(month=d.month + 1, day=1)
    return next_month - timedelta(days=1)

current = date(2026, 4, 15)
print(f"First day: {first_day_of_month(current)}")  # Output - 2026-04-01
print(f"Last day: {last_day_of_month(current)}")  # Output - 2026-04-30

# Case Study: Datetime with Timezone (aware datetime)
from datetime import timezone

# Create timezone-aware datetime
utc_now = datetime.now(timezone.utc)
print(f"UTC now: {utc_now}")  # Output - UTC now with timezone info

# Case Study: Combining Date and Time
d = date(2026, 4, 15)
t = time(14, 30, 45)
combined = datetime.combine(d, t)
print(f"Combined: {combined}")  # Output - 2026-04-15 14:30:45

# Case Study: Extract Date and Time
dt = datetime(2026, 4, 15, 14, 30, 45)
extracted_date = dt.date()
extracted_time = dt.time()
print(f"Date: {extracted_date}")  # Output - 2026-04-15
print(f"Time: {extracted_time}")  # Output - 14:30:45

# Case Study: Countdown Timer
def days_countdown(target_date):
    today = date.today()
    countdown = (target_date - today).days
    if countdown > 0:
        months = countdown // 30
        remaining_days = countdown % 30
        return f"{months}m {remaining_days}d"
    else:
        return "Date has passed"

target = date(2026, 12, 25)
print(f"Countdown to Christmas: {days_countdown(target)}")

# Case Study: Create Date from Day Number
def day_number_to_date(year, day_number):
    start_date = date(year, 1, 1)
    return start_date + timedelta(days=day_number - 1)

day_100 = day_number_to_date(2026, 100)
print(f"Day 100 of 2026: {day_100}")  # Output - Day 100 of 2026

# Case Study: Get Day Number from Date
def date_to_day_number(d):
    year_start = date(d.year, 1, 1)
    return (d - year_start).days + 1

d = date(2026, 4, 15)
day_num = date_to_day_number(d)
print(f"Date {d} is day {day_num} of the year")

# Case Study: Get Week Start and End Dates
def week_start_end(d):
    start = d - timedelta(days=d.weekday())
    end = start + timedelta(days=6)
    return start, end

d = date(2026, 4, 15)
week_start, week_end = week_start_end(d)
print(f"Week starts: {week_start}, ends: {week_end}")  # Output - Week of 2026-04-13 to 2026-04-19

# Case Study: Next Occurrence of Specific Day
def next_weekday(target_weekday):
    today = date.today()
    days_ahead = target_weekday - today.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return today + timedelta(days=days_ahead)

next_monday = next_weekday(0)  # 0 = Monday
print(f"Next Monday: {next_monday}")

# Case Study: Holidays Finder
holidays_2026 = {
    "New Year": date(2026, 1, 1),
    "Independence Day": date(2026, 7, 4),
    "Thanksgiving": date(2026, 11, 26),
    "Christmas": date(2026, 12, 25)
}

def holidays_this_month(month):
    current_month_holidays = {name: date for name, date in holidays_2026.items() 
                               if date.month == month}
    return current_month_holidays

april_holidays = holidays_this_month(4)
july_holidays = holidays_this_month(7)
print(f"April holidays: {april_holidays}")
print(f"July holidays: {july_holidays}")
