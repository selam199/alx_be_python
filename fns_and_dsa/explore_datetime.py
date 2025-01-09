from datetime import datetime, timedelta


def display_current_datetime():
    """Displays the current date and time in a readable format."""
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")


def calculate_future_date():
    """Prompts the user to enter a number of days, calculates the future date,
       and displays it in the same format as the current date."""
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")


def main():
    """Main function to execute the script.
       Calls the display_current_datetime and calculate_future_date functions."""
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()
