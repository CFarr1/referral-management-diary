import datetime as datetime, time

# Function to return a add in minutes onto a date
def AddMinutesToDate(date, minutes):

    # check if date, duration is in correct format if not warn
    if not isinstance(date, datetime.datetime):
        raise TypeError("Date is in a incorrect format, must be in the datetime format!")
    if not isinstance(minutes, (int, float)):
        raise TypeError("Minutes is in a incorrect format, must be int or float!")

    # add date + minutes and return
    return date + datetime.timedelta(minutes=minutes)

# Function to split a float into two ints for hours and minutes
def SplitFloatToTwoInts(value):

    # check if value is in correct format if not warn
    if not isinstance(value, (float, int)):
        raise TypeError("value is in a incorrect format, must be float or int")

    Hours = int(value) # get the hour from float
    Minutes = (abs(int((value - Hours) * 10))*5) # get the minutes from float

    # if minutes overflow just turn it to 0 and add to the hour
    if Minutes > 60:
        Minutes = 0
        Hours += 1

    return Hours, Minutes

# Function to check if a date is between specific hours of the day
def IsBetweenHours(date, start_hour, end_hour):

    # check if date, start_hour and end_hour is in correct format if not warn and also turn the hours into minutes and hour
    if not isinstance(date, datetime.datetime):
        raise TypeError("Date is in a incorrect format, must be in the datetime format!")

    start_hour, start_minutes = SplitFloatToTwoInts(start_hour)
    end_hour, end_minutes = SplitFloatToTwoInts(end_hour)

    if not isinstance(start_hour, int):
        raise TypeError("start_hour is in a incorrect format, must be int!")
    if not isinstance(start_minutes, int):
        raise TypeError("start_minutes is in a incorrect format, must be int!")
    if not isinstance(end_hour, int):
        raise TypeError("end_hour is in a incorrect format, must be int!")
    if not isinstance(end_minutes, int):
        raise TypeError("end_minutes is in a incorrect format, must be int!")

    # get the start and end time
    start_time = datetime.datetime(date.year, date.month, date.day, start_hour, start_minutes, 0)
    end_time = datetime.datetime(date.year, date.month, date.day, end_hour, end_minutes, 0)

    IsValidHours = True

    if date < start_time:
        IsValidHours = False
    if date > end_time:
        IsValidHours = False

    return IsValidHours

# Function to return if a date is valid for calendar
def ValidateDate(date, duration, daystart, dayend):

    # check if date, duration, daystart, dayend is in a correct format if not warn
    if not isinstance(date, datetime.datetime):
        raise TypeError("date is not in a correct format, it must be in datetime!")
    if not isinstance (duration, (int, float)):
        raise TypeError("duration is not in a correct format, it must be int or float!")
    if not isinstance (daystart, (int, float)):
        raise TypeError("daystart is not in a correct format, it must be int or float!")
    if not isinstance (dayend, (int, float)):
        raise TypeError("dayend is not in a correct format, it must be int or float!")

    # get appointment end date
    end_date = AddMinutesToDate(date, duration)

    # check if inbetween correct hours
    IsValid = True

    IsValid_Start = IsBetweenHours(date, 6.00, 22.00)
    IsValid_End = IsBetweenHours(end_date, 6.00, 22.00)

    if IsValid_Start == False:
        IsValid = False
    if IsValid_End == False:
        IsValid = False

    return IsValid

print(ValidateDate(datetime.datetime(2026, 3, 5, 14, 0), 900, 6.00, 22.00))