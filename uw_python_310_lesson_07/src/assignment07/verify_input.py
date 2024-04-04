
def verify_text(text, limit=50):
    """Verify input for text"""
    # verifies if the input is less than the character limit
    if len(text) >= limit:
        return False, f"Input is longer than the {limit} character limit"
    # verifies if the input is not a number
    try:
        float(text)
        return False, f"Input cannot be a number"
    except ValueError:
        return True, text


def verify_boolean(boolean):
    """Verify input for a boolean"""
    # verify if the input is either Y or N"""
    boolean = boolean.lower()
    if boolean not in ["y", "n"]:
        return False, "Input must be Y or N"
    return True, boolean


def verify_float(double):
    """Verify input for a float"""
    try:
        double = float(double)
        return True, double
    except ValueError:
        return False, "Input must be a number"


def verify_date(month, day, year):
    """Verify input for a date"""
    month_verified, month_feedback = verify_month(month)
    day_verified, day_feedback = verify_day(month, day, month_verified)
    year_verified, year_feedback = verify_year(year)
    verified = month_verified and day_verified and year_verified
    feedback = f"{month_feedback}{day_feedback}{year_feedback}"

    if verified:
        month = int(month)
        day = int(day)
        year = int(year)
        date = f"{month}/{day}/{year}"
        return verified, date
    return verified, feedback


def verify_month(month):
    """Verify input for a month prompt"""
    feedback = ""
    try:
        month = int(month)
        if month > 0 and month <= 12:
            return True, feedback
        else:
            feedback += "The month must be between 1 and 12\n"
    except ValueError:
        feedback += "The month must be an integer 1-12\n"
    return False, feedback


def verify_day(month, day, month_verified):
    """Verify input for a day prompt"""
    # create a list with days of each month as the index. index 0 should be avoided
    days_in_month = ["DO NOT USE", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    feedback = ""
    if month_verified:
        try:
            day = int(day)
            month = int(month)
            if day > 0 and day <= days_in_month[month]:
                return True, feedback
            else:
                feedback += "Day is not valid for the month given\n"
        except ValueError:
            feedback += "Day must be an integer\n"
    else:
        feedback += "Month must be verified before verifying the day\n"
    return False, feedback


def verify_year(year):
    """Verify input for a year prompt"""
    feedback = ""
    try:
        # make sure it's 4 digits long and an integer
        int(year)
        if len(year) == 4:
            return True, feedback
        else:
            feedback += "The year must be 4 digits long\n"
    except ValueError:
        feedback += "The year must be an integer\n"
    return False, feedback

def verify_int(num):
    """Verify input for an integer"""
    feedback = ""
    try:
        # try to make it an integer
        int(num)
        return True, feedback
    except ValueError:
        feedback += "Input must be an integer"
    
    return False, feedback
    