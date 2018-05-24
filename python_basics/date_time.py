from datetime import datetime as dt, timedelta as delta

now = dt.now()
strf = now.strftime

def get_time(hour = strf('%I'),
            minute = now.minute,
            locale = strf('%p')):
    return "It's " + format_time(hour, minute, locale)

def get_date(week = strf('%A'),
            month = strf('%B'),
            day = now.day,
            year = now.year):
    return "It's " + format_date(week, month, day, year)

def format_time(hour, minute, locale):
    return "{}:{} {}".format(hour, minute, locale)

def format_date(week, month, day, year):
    return "{} of {} {}, {}"\
            .format(week, month, day, year)

def past_days(past_days):
    past = now - delta(days=past_days)
    output = "{} days ago was: \n".format(past_days)
    output += format_date(past.strftime('%A'),
                        past.strftime('%B'),
                        past.day,
                        past.year) + ' at '
    output += format_time(past.strftime('%I'),
                        past.minute,
                        past.strftime('%p')) + '\n'
    return output

def past_hours(past_hours):
    past = now - delta(hours=past_hours)
    output = "{} hours ago was: \n".format(past_hours)
    output += format_date(past.strftime('%A'),
                        past.strftime('%B'),
                        past.day,
                        past.year) + ' at '
    output += format_time(past.strftime('%I'),
                        past.minute,
                        past.strftime('%p')) + '\n'
    return output

def past_weeks(past_weeks):
    past = now - delta(weeks=past_weeks)
    output = "{} weeks ago was: \n".format(past_weeks)
    output += format_date(past.strftime('%A'),
                        past.strftime('%B'),
                        past.day,
                        past.year) + ' at '
    output += format_time(past.strftime('%I'),
                        past.minute,
                        past.strftime('%p')) + '\n'
    return output

def future_days(future_days):
    future = now + delta(days=future_days)
    output = "In about {} days, it's gonna be: \n".format(future_days)
    output += format_date(future.strftime('%A'),
                        future.strftime('%B'),
                        future.day,
                        future.year) + ' at '
    output += format_time(future.strftime('%I'),
                        future.minute,
                        future.strftime('%p')) + '\n'
    return output

def future_hours(future_hours):
    future = now + delta(hours=future_hours)
    output = "In about {} hours, it's gonna be: \n".format(future_hours)
    output += format_date(future.strftime('%A'),
                        future.strftime('%B'),
                        future.day,
                        future.year) + ' at '
    output += format_time(future.strftime('%I'),
                        future.minute,
                        future.strftime('%p')) + '\n'
    return output

def future_weeks(future_weeks):
    future = now + delta(weeks=future_weeks)
    output = "In about {} weeks, it's gonna be: \n".format(future_weeks)
    output += format_date(future.strftime('%A'),
                        future.strftime('%B'),
                        future.day,
                        future.year) + ' at '
    output += format_time(future.strftime('%I'),
                        future.minute,
                        future.strftime('%p')) + '\n'
    return output


print(get_time())
print(get_date())
print('\n')
print(past_days(52))
print(past_hours(48))
print(past_weeks(2))
print(future_days(2))
print(future_hours(2))
print(future_weeks(2))
