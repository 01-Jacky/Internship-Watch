from datetime import datetime, timedelta

def _convert_to_date(date_string):
    """
    Returns the date based on today and the 'x days ago' string
    e.g. if today is 2017-12-20, then _convert_to_date('1 days ago') returns the datetime 12-15-2017
    """

    DATE_FORMAT = '%Y-%m-%d'

    if date_string.lower() in ['just posted', 'today']:
        return datetime.today().strftime(DATE_FORMAT)
    elif date_string.lower() == '30+ days ago':
        return date_string.lower()
    else:
        # else we need to convert 'x days ago' ago into a date
        days_ago = date_string.split(" ")[0]
        d = datetime.today() - timedelta(days=int(days_ago))
        return d.strftime(DATE_FORMAT)

def subtract_days(date_string):
    DATE_FORMAT = '%Y-%m-%d'

    base_date = datetime.strptime(date_string, DATE_FORMAT)
    date_1_before = base_date - timedelta(days=int(1))
    ans = date_1_before.strftime(DATE_FORMAT)
    return ans


string = '2017-12-20'
DATE_FORMAT = '%Y-%m-%d'

print(subtract_days(string))

DATE_FORMAT = '%Y-%m-%d'

base_date = datetime.strptime(string, DATE_FORMAT)
date_1_before = base_date - timedelta(days=int(1))
ans = date_1_before.strftime(DATE_FORMAT)

print(ans)