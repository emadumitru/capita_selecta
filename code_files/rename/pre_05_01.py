import datetime

def convert_date(natural_date):
    # Define a dictionary to map month names to their corresponding numbers
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

    # Split the natural language date into its components
    parts = natural_date.split()
    month = month_mapping[parts[0]]
    day = int(parts[1].rstrip(','))
    year = int(parts[2])

    # Create a datetime object with the parsed components
    date_obj = datetime.datetime(year, month, day)

    # Format the date in a standardized format
    formatted_date = date_obj.strftime('%Y-%m-%d')

    return formatted_date

# Example usage
natural_date = 'January 1, 2022'
formatted_date = convert_date(natural_date)
print(formatted_date)