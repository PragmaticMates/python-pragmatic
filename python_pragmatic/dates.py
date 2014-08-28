import datetime
from datetime import timedelta


def diff_month(date_from, date_to):
    """
    Returns number of months between dates 'date_from' and 'date_to'
    """
    return (date_to.year - date_from.year)*12 + date_to.month - date_from.month


def diff_days(date_from, date_to):
    """
    Returns number of days between dates 'date_from' and 'date_to'
    """
    return abs((date_to - date_from).days)


def week_range(date):
    """Find the first/last day of the week for the given day.
    Assuming weeks start on Sunday and end on Saturday.

    Returns a tuple of ``(start_date, end_date)``.

    """
    # isocalendar calculates the year, week of the year, and day of the week.
    # dow is Mon = 1, Sat = 6, Sun = 7
    year, week, dow = date.isocalendar()

    # Find the first day of the week.
    if dow == 7:
        # Since we want to start with Sunday, let's test for that condition.
        start_date = date
    else:
        # Otherwise, subtract `dow` number days to get the first day
        start_date = date - timedelta(dow)

    # Now, add 6 for the last day of the week (i.e., count up to Saturday)
    end_date = start_date + timedelta(6)

    #return (start_date, end_date)
    start_datetime = datetime.datetime.combine(start_date, datetime.time.min)
    end_datetime = datetime.datetime.combine(end_date, datetime.time.max)

    return start_datetime, end_datetime
