import datetime

def convert_date(natural_date):
    # Define a dictionary to map natural language months to their corresponding numbers
    month_mapping = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }
    
    try:
        # Split the natural date into day, month, and year
        day, month, year = natural_date.split()
        
        # Convert the month to its corresponding number
        month_number = month_mapping[month]
        
        # Create a datetime object with the given date
        date_object = datetime.datetime(int(year), month_number, int(day))
        
        # Format the date in a specific format
        formatted_date = date_object.strftime("%Y-%m-%d")
        
        return formatted_date
    except ValueError:
        return "Invalid date format"

# Test the function with a sample natural language date
natural_date = "5th February 2022"
formatted_date = convert_date(natural_date)
print(formatted_date)