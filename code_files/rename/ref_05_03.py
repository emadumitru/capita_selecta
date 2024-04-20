import datetime

def convert_natural_date(natural_date):
    today = datetime.date.today()
    words = natural_date.split()
    
    if words[0] == 'today':
        return today.strftime("%Y-%m-%d")
    elif words[0] == 'tomorrow':
        tomorrow = today + datetime.timedelta(days=1)
        return tomorrow.strftime("%Y-%m-%d")
    elif words[0] == 'yesterday':
        yesterday = today - datetime.timedelta(days=1)
        return yesterday.strftime("%Y-%m-%d")
    else:
        try:
            date = datetime.datetime.strptime(natural_date, "%B %d, %Y")
            return date.strftime("%Y-%m-%d")
        except ValueError:
            return "Invalid date format"
        
natural_date = "March 5, 2022"
converted_date = convert_natural_date(natural_date)
print(converted_date)
