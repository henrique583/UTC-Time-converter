# Compute and print the current day of the week.

# import module to compute the seconds since midnight of 1/1/1970:
from time import time

def utc_day(time_value):
    """Computes the weekday (in Greenwich, England) that corresponds to the provided UTC time value.
    
    This function takes one argument: a UTC time value (float).
    It returns an int representing the day of the week (0=sunday, 1=monday, 
    2=tuesday, 3=wednesday, 4=thursday, 5=friday, 6=saturday) corresponding
    to the specified UTC time value.
    """
    secs = int(time_value)
    #converts time given in seconds to an integer
    mins = secs // 60
    hours = mins // 60
    days_since_epoch = hours // 24
    remaining_days = days_since_epoch % 7
    #Uses remainder of days left in a week to tell you
    #what day of the week it is given a time_value in seconds
    weekday = (remaining_days + 4) % 7
    #Adjusts day 0 to be Sunday instead of Thursday
    return weekday

def local_day(time_value, offset):
    """Computes the weekday (for a location that is offset hours ahead from Greenwich, England).
    
    This function takes two arguments: a UTC time value (float)
    and an offset (float). It calls utc_day to help compute the 
    current day of the week for a timezone that is offset hours 
    ahead of Greenwich, England, then returns that weekday.
    """
    
    #Multiplies numbers of hours offset by number of seconds
    #in a day so it can be added to time_value
    local_day = time_value + (offset * 3600)
    return utc_day(local_day)

def day_of_week(day):
    """Computes the name of a weekday, given its integer (0-6) representation.
    
    This function takes one argument: an int between 0 and 6 (inclusive). 
    It returns the name of that weekday as a string.
    """
    
    if day == 0:
        return "Sunday"
    if day == 1:
        return "Monday"
    if day == 2:
        return "Tuesday"
    if day == 3:
        return "Wednesday"
    if day == 4:
        return "Thursday"
    if day == 5:
        return "Friday"
    if day == 6:
        return "Saturday"

    
if __name__ == "__main__":
    # get UTC time
    now = time()
    # find day of week number for Williamstown
    day_number = local_day(now, -5)
    # get name of day and print it
    day_name = day_of_week(day_number)
    print("It's "+ day_name +"!")
