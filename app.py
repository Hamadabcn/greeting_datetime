import datetime

def greet_and_get_time():
    # Get current date and time
    now = datetime.datetime.now()

    # Format the date and time
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")

    # Greet the user
    print(f"\nHello how are you! The current date is {current_date} and the current time is {current_time}. Do you still have any things to do today\n")

# Call the function
greet_and_get_time()