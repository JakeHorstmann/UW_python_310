from verify_input import verify_text, verify_boolean, verify_float, verify_date, verify_int
from tabulate import tabulate


class Menu:
    """Menu used to display text and gather input from the user"""
    def ask_for_quote(self):
        """Asks a user for input based on the FIELDS variable"""
        # fields that are used to create a quote
        FIELDS = {"cust_name": {"question": "What is the name of the customer?", "verify_func": verify_text},
                            "desc": {"question":"Please enter a description of the package:", "verify_func": verify_text},
                            "is_dangerous": {"question": "Are the contents dangerous? [Y/N]", "verify_func": verify_boolean},
                            "weight": {"question": "What is the weight of the package in kilograms?", "verify_func": verify_float},
                            "volume": {"question": "What is the volume of the package in cubic meters?", "verify_func": verify_float},
                            "deliver_date": {"question": "When does this need to be delivered by?", "verify_func": verify_date},
                            "is_international": {"question": "Is it going to an international destination? [Y/N]", "verify_func": verify_boolean},
                            }
        # dictionary used to store the user's verified responses
        user_input = {}

        # loops through each question in FIELDS and verifies input
        for field, props in FIELDS.items():
            question = props["question"]
            verify_func = props["verify_func"]
            verified = False
            # loop while the input is not verified from the user
            while not verified:
                # special treatment with the verify function if the input is a date
                if verify_func == verify_date:
                    print(f"{question} ")
                    month, day, year = self.ask_for_date()
                    verified, response = verify_date(month, day, year)
                # otherwise all questions will be mapped through here
                else:
                    response = input(f"{question} ")
                    verified, response = verify_func(response)
                # if the input was verified, the response is added to the user's input
                if verified:
                    user_input[field] = response
                # if not, we must loop again and print our error message
                else:
                    self.print_errors(response)
        
        return user_input

    def ask_for_date(self):
        """ Ask the user for a date"""
        month = input("Please enter a month: ")
        day = input("Please enter a day: ")
        year = input("Please enter a year: ")
        return month, day, year

    def find_error_output_length(self, text):
        """ Find the maximum length for error console output"""
        substrings = text.split("\n")
        max_length = 0
        for string in substrings:
            max_length = max(len(string), max_length)
        return max_length

    def print_errors(self, errors):
        """ Print errors from input verification"""
        header = " ERRORS "
        # get length of table to make it prettier
        table_length = self.find_error_output_length(errors)
        # quick check to see if header is longer than the responses (should never happen)
        table_length = max(table_length, len(header))
        print(header.center(table_length, "*"))

        # check if the ending is a new line from the error responses
        if errors[-1:] == "\n":
            print(errors[:-1])
        else:
            print(errors)
        print("*"*table_length)

    def display_shipment_options(self, options):
        """Display shipment options. Options has format {"shipment_option": (possible?, cost_if_possible, error_msg)}"""
        HEADER = "SHIPMENT OPTIONS:"
        dashes = "-"*self.find_longest_string(HEADER, options, "REASON: ")
        print(HEADER)
        print(dashes)
        for option, (possible, cost, error_msg) in options.items():
            print(f"METHOD: {option.title()}")
            if possible:
                print("POSSIBLE? ✓")
                print(f"COST: ${cost}")
            else:
                print("POSSIBLE? ✕")
                print(f"REASON: {error_msg}")
            print(dashes)

    def get_shipment_options(self, options):
        """Get which shipment option the user wants to use"""
        self.display_shipment_options(options)
        all_methods = list(options.keys())
        method_details = list(options.values())
        methods = self.get_valid_methods(all_methods, [detail[0] for detail in method_details])
        # check if there is no shipping options available
        if len(methods) == 0:
            print("This package cannot be shipped for the reasons listed above")
            return None
        # check if there is only one shipping option available
        elif len(methods) == 1:
            print(f"Package will be shipped by {methods[0]} because it is the only available option")
            index = 0
        # otherwise let the user pick which option they would like to ship by
        else:
            running = True
            while running:
                user_input = input("Please enter a method above: ").lower()
                # check if user chooses a valid method
                try:
                    index = methods.index(user_input)
                    running = False
                except ValueError:
                    print("Please enter a valid ship method from the following methods: ")
                    print(", ".join(methods))
            
        # return {"method": {cost}}
        return {methods[index]: options[methods[index]][1]}
            

    def find_longest_string(self, header, options, error_txt):
        """Find the longest string printed in a display method"""
        longest_length = len(header)
        for _, _, error_msg in options.values():
            if error_msg:
                longest_length = max(longest_length, len(error_msg) + len(error_txt))
        return longest_length
    
    def get_valid_methods(self, all_methods, truth_list):
        """Return a list of valid methods based on a truth array"""
        counter = 0
        methods = []
        for truth in truth_list:
            if truth:
                methods.append(all_methods[counter])
            counter += 1
        return methods
    
    def ask_for_quote_id(self):
        verified = False
        while not verified:
            id = input("Please enter a quote ID: ")
            verified, error = verify_int(id)
            if verified:
                id = int(id)
            else:
                print(error)

        return id
    
    def display_as_table(self, data):
        columns = data["columns"]
        display_data = data["data"]
        table = tabulate(display_data, headers = columns)
        print(table)
    
    def main_menu(self, options):
        print("BOOKING SYSTEM:")
        counter = 0
        for option in options:
            print(f"{counter+1}. {options[counter]}")
            counter += 1
        verified = False
        while not verified:
            response = input("Please enter an option on the menu: ")
            if response in [str(i) for i in range(1, counter+1)]:
                verified = True
                response = int(response)
            else:
                print("Answer is not a valid option")

        return response

            

