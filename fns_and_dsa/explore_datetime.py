#!/usr/bin/python3

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

def calculate_future_date(current_date):
    # Ask user for number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate future date
    future_date = current_date + timedelta(days=days_to_add)
    # Format as YYYY-MM-DD
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)
    return future_date

if __name__ == "__main__":
    # Part 1
    today = display_current_datetime()
    # Part 2
    calculate_future_date(today)

