import datetime

def convert_date(natural_date):
    # Define a dictionary to map natural language month names to their corresponding numbers
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
        # Split the natural date into its components
        date_parts = natural_date.split()
        
        # Extract the day, month, and year from the natural date
        day = int(date_parts[1])
        month = month_mapping[date_parts[2]]
        year = int(date_parts[3])
        
        # Create a datetime object with the extracted date
        converted_date = datetime.datetime(year, month, day)
        
        # Format the converted date as 'YYYY-MM-DD'
        formatted_date = converted_date.strftime('%Y-%m-%d')
        
        return formatted_date
    except (ValueError, IndexError):
        return None

# Example usage
natural_date = 'The 5th of April 2022'
converted_date = convert_date(natural_date)
print(converted_date)