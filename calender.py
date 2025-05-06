import calendar

# Function to display the calendar for a specific month and year
def display_calendar(year, month):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar()
    
    # Format the month and print it
    month_calendar = cal.formatmonth(year, month)
    print(month_calendar)

# Example usage
if __name__ == "__main__":
    year = int(input("Enter year (e.g., 2020): "))
    month = int(input("Enter month (1-12): "))
    
    display_calendar(year, month)