import menu

# initialize starting log
donor_data = [("Jake Horstmann", 10.0),
              ("Paul Lockaby", 50.0),
              ("Luis Conejo Alpizar", 35.0),
              ("Batman", 1000.0),
              ("Paul Lockaby", 500.0)]


def get_donor_names(data):
    # gets all donor names in the log
    names = []
    for row in data:
        name = row[0]
        names.append(name)
    unique_names = list(set(names))
    return sorted(unique_names)


def display_names(names):
    # displays names if the users types in LIST in send_thank_you
    print("")
    print("NAMES: ")
    for name in names:
        print(name)
    print("")


def send_thank_you():
    # get initial input from user
    response = menu.get_thank_you_input()
    while response == "list":
        # if user says list, get and display all donor names and ask for input again
        all_names = get_donor_names(donor_data)
        display_names(all_names)
        response = menu.get_thank_you_input()
    # if the user puts in anything else use it as a name and store the donation to the log
    name = response.title()
    amount = menu.get_donation_amount()
    add_donation_to_data(name, amount)
    menu.thank_donating_user(name)


def add_donation_to_data(name, amount):
    # adds a donation with a name and an amount
    donor_data.append((name, amount))


def generate_report():
    # creates data to send to the report in the form of {name: [total_donated, times_donated]}
    data = consolidate_donor_data()
    menu.display_report(data)


def consolidate_donor_data():
    data = {}
    # loop through log of donor data
    for line in donor_data:
        name = line[0]
        amount = line[1]
        if name in data.keys():
            # add amount to previous amount
            data[name][0] += amount
            # add 1 to number of donations
            data[name][1] += 1
        else:
            # set up dictionary if not there
            data[name] = [amount, 1]
    return data


def main():
    while True:
        response = menu.get_menu_input()
        if response == "a":
            send_thank_you()
        elif response == "b":
            generate_report()
        else:
            print("Quitting program...")
            break


if __name__ == "__main__":
    main()
