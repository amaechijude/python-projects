from datetime import datetime
def datetime_func(param):
    t = datetime.fromtimestamp(int(param)).strftime('%I:%M:%S %p %b. %d, %Y')
    return t