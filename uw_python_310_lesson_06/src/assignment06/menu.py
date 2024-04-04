import data_handler
from tabulate import tabulate

DASH_MULTIPLIER = 50
# Return the choices so they can be used elsewhere
def return_choices():
    choices = ["1. Load employees in from a CSV",
               "2. Save employees into a CSV",
               "3. Add a new employee",
               "4. Generate a report of current employees",
               "5. Generate a report of employees who have recently left",
               "6. Generate a report of annual reminders",
               "7. Exit"]
    return choices

# Display the main menu to the user
def display_main_menu():
    # print spacing line
    print("")
    # add dashes to look a little nicer
    print("MENU OPTIONS: ")
    print("-"*DASH_MULTIPLIER)
    # display all choices
    choices = return_choices()
    print("\n".join(choices))

# Get input for the menu choices displayed to the user
def get_menu_input():
    menu_choice = input("Please enter one of the choices above: ")
    verified_menu_choice = data_handler.verify_menu_choice(menu_choice)
    # loop while menu choice is not verified
    while not verified_menu_choice:
        menu_choice = input("Please enter a valid choice: ")
        verified_menu_choice = data_handler.verify_menu_choice(menu_choice)
    menu_choice = int(menu_choice)
    return menu_choice

# Get the CSV path for reading from the user
def get_read_csv_path():
    csv_path = input("Please enter the relative path to the csv: ")
    verified_csv_path = data_handler.verify_read_csv_path(csv_path)
    # loop while path is not verified
    while not verified_csv_path:
        csv_path = input("Please enter a valid path (extension included): ")
        verified_csv_path = data_handler.verify_read_csv_path(csv_path)
    
    return csv_path

# Get the CSV path for writing from the user
def get_write_csv_path():
    csv_path = input("Please enter where to save the csv: ")
    verified_csv_path = data_handler.verify_write_csv_path(csv_path)
    # loop while path is not verified
    while not verified_csv_path:
        csv_path = input("Please enter a valid path (extension included): ")
        verified_csv_path = data_handler.verify_write_csv_path(csv_path)
    
    return csv_path

# Get the users inputs to the questions for a new employee
def get_employee_data(question, verify_function):
    verified = False
    error_message = None
    while not verified:
        # print error message if there is one
        if error_message:
            print(error_message)
        # route it differently if the question is a data to ensure better input
        if "date" in question.lower():
            print(f"What is their {question}? ")
            month = input(f"Please enter a month: ")
            day = input(f"Please enter a day: ")
            year = input(f"Please enter a year: ")
            # check to see if no date input is ok for end dates
            if (month == "" and day == "" and year == "") and "end" in question.lower():
                verified = True
                answer = None
            # otherwise check that the inputs are valid
            else:
                verified, error_message = verify_function(month, day, year)
                if verified:
                    answer = f"{int(month)}/{int(day)}/{int(year)}"
        else:
            answer = input(f"What is their {question}? ")
            verified, error_message = verify_function(answer)
    return answer

def display_employees_as_of_date(ids, names, date):
    print("")
    print(f"EMPLOYEES AS OF {date}:")
    print("-"*DASH_MULTIPLIER)
    table = {"ID": ids, "Name": names}
    print_tabular_names(table)

def display_employees_terminated(ids, names, end_dates, date):
    print("")
    print(f"EMPLOYEES TERMINATED SINCE {date}:")
    print("-"*DASH_MULTIPLIER)
    table = {"ID": ids, "Name": names, "End Date": end_dates}
    print_tabular_names(table)

def display_anniversaries(ids, names, start_dates, days_till, days):
    print("")
    print(f"EMPLOYEE ANNIVERSARIES WITHIN {days} DAYS:")
    print("-"*DASH_MULTIPLIER)
    table = {"ID": ids, "Name": names, "Start Date": start_dates, "Days Till": days_till}
    print_tabular_names(table)

def print_tabular_names(table):
    print(tabulate(table, headers="keys", tablefmt="github"))