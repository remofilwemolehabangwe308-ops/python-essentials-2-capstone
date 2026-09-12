import platform
import os
import datetime
import calendar 

def environment_report():
    os_name = platform.system()
    python_version = platform.python_version()
    current_working_directory = os.getcwd()
    file_exists = os.path.exists("data/students.txt")
    if file_exists is True:
        file_size = os.path.getsize("data/students.txt")
    else:
        file_size = 0
    return f"OS name:{os_name}\nPython version:{python_version}\nCurrent working directory:{current_working_directory}\nFile exists:{file_exists}\nFile size:{file_size}"

def date_report():
    today = datetime.date.today()
    formatted_date = today.strftime("%A, %d %B %Y")
    current_timestamp = datetime.datetime.now()
    future_date = datetime.date(2026,9,30)
    date_difference = future_date - today
    days_until_future_date = date_difference.days
    current_month = calendar.month_name[datetime.date.today().month] 
    is_it_leap_year = calendar.isleap(datetime.date.today().year)
    days_in_current_month = calendar.monthrange(
        datetime.date.today().year,
        datetime.date.today().month 
    )
    days_in_month = days_in_current_month[1]
    return f"Formatted date: {formatted_date}\nCurrent timestamp: {current_timestamp}\nFuture date: {future_date}\nDays until the future date: {days_until_future_date}\nCurrent month: {current_month}\nIs it leap year: {is_it_leap_year}\nDays in month:  {days_in_month}"
