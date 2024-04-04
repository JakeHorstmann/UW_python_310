def display_menu():
    # Display the menu to user
    print("********** MENU **********")
    MENU_OPTIONS = ("A. Send a Thank You",
                    "B. Create a Report",
                    "C. Quit")
    print("\n".join(MENU_OPTIONS))


def get_menu_input():
    # Display the menu to the user and get their reponse
    verified = False
    while not verified:
        display_menu()
        question = "Please enter a valid option: "
        response = input(question).lower()
        verified = verify_menu_input(response)
        print()
    return response


def verify_menu_input(ans):
    # Verify that the menu response is in the list of choices
    MENU_CHOICES = ("a", "b", "c")
    if ans in MENU_CHOICES:
        return True
    return False


def display_thank_you_menu():
    # Display the menu for the thank you option
    print("********** THANK YOU MENU **********")
    MENU_OPTIONS = ("Type LIST to display a list of all donor names",
                    "Type in your name to donate")
    print("\n".join(MENU_OPTIONS))


def get_thank_you_input():
    # Get the input for the thank you option
    display_thank_you_menu()
    question = "Please enter your name or LIST: "
    response = input(question).lower()
    return response


def get_donation_amount():
    # Get donation amount from user and verify it
    verified = False
    while not verified:
        amount = input("Please enter an amount to donate: ")
        verified = verify_amount(amount)
    return round(float(amount), 2)


def verify_amount(str_amount):
    # Verify the donation amount
    try:
        amount = float(str_amount)
        return True
    except ValueError:
        print("Please enter a valid donation amount")
        return False


def thank_donating_user(name):
    # Thank the user for donating
    email = [f"Hi {name},",
             "",
             "Thank you for your generous donation. ",
             "",
             "Have a wonderful day,",
             "Jake Horstmann"]
    print("\n".join(email))


def display_report(data):
    # Displays the report in a nice format
    # set up columns and data values
    columns = ["Donor Name", "Total Given", "Num Gifts", "Average Gifts"]
    names = list(data.keys())
    total_given = [round(amount[0], 2) for amount in data.values()]
    num_gifts = [gifts[1] for gifts in data.values()]
    avg_gift = [round(total_given[col]/num_gifts[col], 2) for col in range(len(names))]
    all_values = [names, total_given, num_gifts, avg_gift]
    # get max width of columns
    col_widths = []
    for col in range(len(columns)):
        column = columns[col]
        values = all_values[col]
        space = get_report_spacing(column, values)
        col_widths.append(space)

    # pad columns with 1 space
    padding = 1
    # fudge factors to account for extra $ signs and extra decimals added from float showing as 1.0 and not 1.00
    columns_with_sign = 2
    extra_float_zero = 2
    # print heading out
    print_report_row(columns, col_widths, padding)
    print("-"*(padding*len(columns)+sum(col_widths)+columns_with_sign+extra_float_zero))
    # print all row values
    for row in range(len(names)):
        name = names[row]
        given = total_given[row]
        gifts = num_gifts[row]
        avg = avg_gift[row]
        row_data = [name, given, gifts, avg]
        print_report_row(row_data, col_widths, padding)
    # print extra line spacing
    print()


def get_report_spacing(column_name, values):
    # finds the max length of a column
    max_length = len(column_name)
    for value in values:
        max_length = max(max_length, len(str(value)))
    return max_length


def print_report_row(values, col_widths, padding=1):
    row = ""
    for col in range(len(values)):
        # get value and max width for the column
        value = values[col]
        width = col_widths[col]
        try:
            # check if the column is a number. right align if it is
            int(value)
            # if it is a float and ends in .0, add another 0 to make it look better
            if (str(value)[-2:] == ".0") and (type(value) == type(1.0)):
                value = str(value) + "0"
                pad = " "*(padding + width - len(value) - 1)
                row += f"${pad}{value}"
            # if it is just a float and a normal decimal, pad it this way
            elif type(value) == type(1.0):
                value = str(value)
                pad = " "*(padding + width - len(value) - 1)
                row += f"${pad}{value}"
            # if it is a normal number with 2 decimals pad it this way
            else:
                value = str(value)
                pad = " "*(padding + width - len(value))
                row += f"{pad}{value}"
        # catches all strings to left align
        except ValueError:
            value = str(value)
            pad = " "*(padding + width - len(value))
            row += f"{value}{pad}"
        # add bars between columns
        row += "|"
    print(row)
