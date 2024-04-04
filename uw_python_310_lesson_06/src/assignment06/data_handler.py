import menu
import pandas as pd
import os
from datetime import datetime, timedelta
pd.options.mode.chained_assignment = None  # default='warn'

# Verify that the menu input is within the range of choices
def verify_menu_choice(menu_choice):
    # make sure that the choice can be an integer
    try:
        menu_choice = int(menu_choice)
        menu_choice_range = range(1, len(menu.return_choices()) + 1)
        if menu_choice in menu_choice_range:
            return True
        else:
            return False
    # return not verified if it is not an int
    except ValueError:
        return False
    
# Route the user's menu choice to the correct function
def route_menu_input(menu_choice, csv):
    match menu_choice:
        case 1:
            response = load_employee_csv()
        case 2:
            response = save_employee_csv(csv)
        case 3:
            response = add_new_employee(csv)
        case 4:
            response = report_current_employees(csv)
        case 5:
            response = report_recent_terminated(csv)
        case 6:
            response = report_upcoming_anniversaries(csv)

    return response

# Load a CSV from the user that has employee data
def load_employee_csv():
    csv_path = menu.get_read_csv_path()
    csv = pd.read_csv(csv_path)
    # return a loaded csv as pandas dataframe
    return csv

# Verify that the csv path is valid
def verify_read_csv_path(path):
    # check to make sure the file actually exists
    try:
        csv = pd.read_csv(path)
        return True
    except FileNotFoundError:
        return False
    
def save_employee_csv(csv):
    # verify csv_path
    csv_path = menu.get_write_csv_path()
    # save csv to valid path
    if type(csv) == type(None):
        print("")
        print("No CSV to save. Please load a CSV first")
    else:
        csv.to_csv(csv_path, index = False)
    
    return csv
    
def verify_write_csv_path(path):
    # check if path already exists so we don't overwrite if it does and csv is empty
    if os.path.exists(path):
        return True
    else:
        # check that file has .csv at the end
        if path[-4:].lower() == ".csv":
            # check if the full path is valid by opening a file. delete it after it creates
            try:
                with open(path,"w") as f:
                    pass
                os.remove(path)
                return True
            except FileNotFoundError:
                pass
    return False

# Adds a new user to the CSV data
def add_new_employee(csv):
    # check if csv is empty
    if type(csv) == type(None):
        print("")
        print("Please load a CSV before adding a new employee")
    else:
        # set up questions to ask user. this also uses a verify function to verify input
        questions = [("NAME", verify_words),
                    ("ADDRESS", verify_words),
                    ("SOCIAL SECURITY NUMBER", verify_ssn),
                    ("DATE OF BIRTH", verify_date),
                    ("JOB TITLE", verify_words),
                    ("START DATE", verify_date),
                    ("ENDING DATE", verify_date)]
        # create a list that can append to the csv. start it with a unique id
        responses = [create_unique_id(csv)]

        # get input for questions and verify all responses
        for question, verify_func in questions:
            question = question.lower()
            response = menu.get_employee_data(question, verify_func)
            # special treatment to remove dashes for ssn
            if question == "social security number":
                responses.append("".join(response.split("-")))
            else:
                responses.append(response)

        # add the row to the csv
        csv.loc[len(csv)] = responses
    return csv
    

# Create a unique ID for a new employee
def create_unique_id(csv):
    max_id = csv.employee_id.max()
    return max_id + 1

# Verify input that is a set of words
def verify_words(words):
    LENGTH_LIMIT = 50
    # check if all the words together are over 50 characters
    if len(words) > LENGTH_LIMIT:
        error_message = f"Input is over {LENGTH_LIMIT} characters"
        return False, error_message
    # try to turn it into an int. if that's possible, it's not a word
    try:
        int(words)
        error_message = "Input cannot be a number"
        return False, error_message
    except ValueError:
        # check if empty
        if words == "":
            error_message = "Input cannot be empty"
            return False, error_message
    return True, None

# Verify input for SSN
def verify_ssn(ssn):
    # remove dashes if they exist
    ssn = "".join(ssn.split("-"))
    # check if the ssn can be an integer
    try:
        int(ssn)
        # check if it is 9 digits long
        if len(str(ssn)) != 9:
            error_message = "SSN can only contain 9 digits"
            return False, error_message
    except ValueError:
        error_message = "SSN must be composed of numbers, not text"
        return False, error_message
    return True, None

# Verify input for a date
def verify_date(month, day, year):
    month_verified = verify_month(month)
    day_verified = verify_day(month, day, month_verified)
    year_verified = verify_year(year)
    verified = month_verified and day_verified and year_verified

    return verified, None

# Verify input for a month prompt
def verify_month(month):
    try:
        month = int(month)
        if month > 0 and month <= 12:
            return True
        else:
            print("The month must be an integer 1-12")
    except ValueError:
        print("The month must be an integer 1-12")
    return False

# Verify input for a day prompt
def verify_day(month, day, month_verified):
    # create a list with days of each month as the index. index 0 should be avoided
    days_in_month = ["DO NOT USE",31,28,31,30,31,30,31,31,30,31,30,31]
    if month_verified:
        try:
            day = int(day)
            month = int(month)
            if day > 0 and day <= days_in_month[month]:
                return True
            else:
                print("Day is not valid for the month given")
        except ValueError:
            print("Day must be an integer")
    else:
        print("Month must be verified before verifying the day")
    return False

# Verify input for a year prompt
def verify_year(year):
    # make sure it's 4 digits long
    try:
        int(year)
        if len(year) == 4:
            return True
        else:
            print("The year must be 4 digits long")
    except ValueError:
        print("The year must be an integer")
    return False

# Runs a report to display all current employees
def report_current_employees(csv):
    if type(csv) == type(None):
        print("")
        print("Please load a CSV before trying to report on current employees")
    else:
        current_date = datetime.now()
        current_employee_ids = employees_as_of_date(csv, current_date)
        current_employees = match_ids_to_names(csv, current_employee_ids)
        ids = current_employees["employee_id"].to_list()
        names = current_employees["name"].to_list()
        menu.display_employees_as_of_date(ids, names, current_date.strftime("%m/%d/%Y"))

    return csv

# Returns all employees as of a certain date
def employees_as_of_date(csv, date):
    employees = csv[["employee_id", "end_date"]]
    # replace empty dates with the date so they do not get ignored
    employees["end_date"] = employees["end_date"].fillna(date)
    # convert end date column for easy compairing
    employees["end_date"] = pd.to_datetime(employees["end_date"])
    # create dummy date column to calculate the difference
    employees["compare_date"] = pd.to_datetime(date)
    # find all employees with an end date later than the date given
    employees = employees[(employees["end_date"] - employees["compare_date"]).dt.days >= 0]
    return employees["employee_id"]

# Matches employee IDs to names
def match_ids_to_names(csv, ids):
    employees = csv[["employee_id", "name"]]
    # inner join each frame on ID column
    filtered_employees = employees.merge(ids, on = "employee_id", how = "inner").sort_values(by = ["employee_id"])
    return filtered_employees

# Reports on recently terminated employees. Default is 31 days
def report_recent_terminated(csv, days = 31):
    if type(csv) == type(None):
        print("")
        print("Please load a CSV before trying to report on recently terminated employees")
    else:
        cutoff_date = datetime.now() - timedelta(days=days)
        terminated = employees_terminated_since_date(csv, cutoff_date)
        terminated = match_ids_to_names(csv, terminated)
        # pull in end dates
        terminated = terminated.merge(csv[["employee_id", "end_date"]], on = "employee_id", how = "inner")
        ids = terminated["employee_id"].to_list()
        names = terminated["name"].to_list()
        end_dates = terminated["end_date"].to_list()
        menu.display_employees_terminated(ids, names, end_dates, cutoff_date.strftime("%m/%d/%Y"))

    return csv

# Returns all employees terminated since a date
def employees_terminated_since_date(csv, date):
    current_date = datetime.now()
    # get employees today and as of the date given to see which employees are no longer here
    employees_now = employees_as_of_date(csv, current_date)
    employees_then = employees_as_of_date(csv, date)
    # left join the current employees to the old employee list. indicator shows "left_only" for employees that did not match (were terminated)
    terminated = employees_then.to_frame().merge(employees_now, on = "employee_id", how = "left", indicator = True)
    # select only terminated employees
    terminated = terminated[terminated["_merge"] == "left_only"]
    return terminated["employee_id"]

# Reports on anniversaries within a number of days. Default is 90 days
def report_upcoming_anniversaries(csv, days = 90):
    if type(csv) == type(None):
        print("")
        print("Please load a CSV before trying to report on upcoming anniversaries")
    else:
        employees = upcoming_anniversaries(csv, days)
        employees = match_ids_to_names(csv, employees)
        ids = employees["employee_id"].to_list()
        names = employees["name"].to_list()
        start_dates = employees["start_date"].to_list()
        days_till = employees["days_till_anni"].to_list()
        menu.display_anniversaries(ids, names, start_dates, days_till, days)

    return csv


# Returns employee IDs for upcoming anniversaries based on days
def upcoming_anniversaries(csv, days):
    employees = csv[["employee_id", "start_date"]]
    employees["start_date"] = pd.to_datetime(employees["start_date"])
    employees["compare_date"] = pd.to_datetime(datetime.now())
    employees["days_till_anni"] = (employees["start_date"] - employees["compare_date"]).apply(
        lambda x: (x.days % 365) + 1
    )
    anniversary_ids = employees[employees["days_till_anni"] <= days]
    anniversary_ids["start_date"] = anniversary_ids["start_date"].dt.date
    return anniversary_ids[["employee_id", "start_date", "days_till_anni"]]
