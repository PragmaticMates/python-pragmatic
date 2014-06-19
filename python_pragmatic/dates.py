def diff_month(date_from, date_to):
    """
    Returns number of months between dates 'date_from' and 'date_to'
    """
    return (date_to.year - date_from.year)*12 + date_to.month - date_from.month
