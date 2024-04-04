from menu import Menu
from quote import Quote
import csv

class Application(Menu):
    """Runs the main application"""
    def __init__(self):
        """Begins loop for running the application"""
        self.csv_columns = ["id",
                            "cust_name",
                            "ship_method",
                            "cost",
                            "deliver_date",
                            "desc",
                            "weight",
                            "volume",
                            "is_dangerous",
                            "is_international"]
        self.quotes_in_system = self.quotes_in_system()
        self.run_app()

    def run_app(self):
        """Main application running loops"""
        OPTIONS = ["Enter a quote in the system",
                   "Find how many quotes in the system",
                   "Look up a quote by its ID",
                   "See last 5 quotes entered in the system",
                   "Exit"]
        option_len = len(OPTIONS)
        running = True
        while running:
            # get a menu option from the user
            menu_option = self.main_menu(OPTIONS)
            match menu_option:
                # collect a quote from the user and save it to csv
                case 1:
                    quote = self.collect_quote()
                    if quote:
                        id = self.generate_quote_id()
                        data = quote.prepare_for_csv(id)
                        self.save_data(data)
                        print(f"Quote succesfully saved with id {id}")

                # display number of quotes in the system
                case 2:
                    print(f"Total number of quotes in the system: {self.quotes_in_system}")
                # look up a quote by an ID
                case 3:
                    id = self.ask_for_quote_id()
                    quote_data = self.find_quote_by_id(id)
                    if quote_data:
                        data = {"columns": self.csv_columns,
                                "data": [quote_data]}
                        self.display_as_table(data)
                    else:
                        print(f"ID {id} not found")
                # find last 5 quotes in system
                case 4:
                    ids = self.last_quotes(5)
                    data = []
                    for id in ids:
                        data.append(self.find_quote_by_id(id))

                    all_data = {"columns": self.csv_columns,
                                "data": data}
                    self.display_as_table(all_data)
                # exit application
                case option_len:
                    print("Exiting...")
                    return
            print("")
                
    def collect_quote(self):
        """Collects a quote from the user"""
        response = self.ask_for_quote()
        quote = Quote(response)
        shipment_options = quote.return_shipment_options()
        shipment = self.get_shipment_options(shipment_options)
        
        if shipment:
            quote.set_shipment(shipment)
            return quote
        return None
    
    def generate_quote_id(self):
        """Generates a unique quote ID"""
        self.quotes_in_system += 1
        return self.quotes_in_system

    def quotes_in_system(self, csv_path = "booking_quotes.csv"):
        """Returns the total number of quotes in the system"""
        csv_length = 0
        with open(csv_path, "r", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                csv_length += 1
        return csv_length - 1
    
    def find_quote_by_id(self, id, csv_path = "booking_quotes.csv"):
        """Returns details for a quote in the system"""
        counter = 1
        with open(csv_path, "r", newline="") as csvfile:
            next(csvfile)
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                csv_id = int(row[0])
                if csv_id == id:
                    return row
                counter += 1
        return None
    
    def last_quotes(self, num_of_quotes, csv_path = "booking_quotes.csv"):
        """Returns num_of_quotes worth of the last quotes in the system"""
        ids = []
        counter = 1
        with open(csv_path, "r", newline="") as csvfile:
            next(csvfile)
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                csv_id = int(row[0])
                ids.append(csv_id)
                if len(ids) > num_of_quotes:
                    ids.pop(0)
                counter += 1
        return ids
    
    def save_data(self, data, csv_path = "booking_quotes.csv"):
        with open(csv_path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow(data)
        
