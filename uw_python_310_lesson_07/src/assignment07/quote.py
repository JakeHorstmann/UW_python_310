from datetime import datetime

class Quote:
    """Used to create a quote in the system"""

    def __init__(self, input_dictionary):
        """Initialize a quote based on the input from menu.ask_for_input"""
        self.cust_name = input_dictionary["cust_name"]
        self.desc = input_dictionary["desc"]
        self.is_dangerous = self.convert_yes_or_no(input_dictionary["is_dangerous"])
        self.weight = input_dictionary["weight"]
        self.volume = input_dictionary["volume"]
        self.deliver_date = input_dictionary["deliver_date"]
        self.is_international = self.convert_yes_or_no(input_dictionary["is_international"])
        self.can_ship = self.can_be_shipped()
        # only calculate shipment routes if it can be shipped
        if self.can_ship:
            self.is_urgent = self.urgent()
            self.air = self.can_ship_air()
            # check if the package is urgent and can ship by air
            if self.is_urgent and self.air[0]:
                # only allow air if urgent and possible
                self.ground = (False, None, "Shipment is urgent and can ship by air")
                self.overseas = (False, None, "Shipment is urgent and can ship by air")
            else:
                self.ground = self.can_ship_ground()
                self.overseas = self.can_ship_overseas()
        else:
            # if can't ship, set error messages as so
            self.ground = (False, None, "Shipment is over weight or volume limit")
            self.air = (False, None, "Shipment is over weight or volume limit")
            self.overseas = (False, None, "Shipment is over weight or volume limit")
        

    def urgent(self):
        """Determine is a package is urgent based on delivery date"""
        URGENT_LIMIT = 3
        deliver_date = self.deliver_date
        # get current date, but leave out clock time
        current_date = datetime.now()
        current_date = f"{current_date.month}/{current_date.day}/{current_date.year}"

        # find difference between 2 dates in days
        delta = (datetime.strptime(deliver_date, "%m/%d/%Y") - datetime.strptime(current_date, "%m/%d/%Y")).days
        
        # return y if urgent, n if not urgent
        if delta <= URGENT_LIMIT:
            return True
        return False

    def can_be_shipped(self):
        """Determine if the package can be shipped based on weight and volume"""
        WEIGHT_LIMIT = 10
        VOLUME_LIMIT = 125
        weight = self.weight
        volume = self.volume
        # check if weight is above weight limit or volume is above volume limit
        if (weight >= WEIGHT_LIMIT) or (volume >= VOLUME_LIMIT):
            return False
        return True
    
    def can_ship_air(self):
        """Determines if a package can be shipped by air"""
        # if shipment is dangerous, you cannot ship by air
        if self.is_dangerous:
            return (False, None, "Cannot ship dangerous packages by air")
        
        # return shipment cost if it can
        cost = self.calculate_air_cost()
        return (True, round(cost,2), None)
        

    def can_ship_ground(self):
        """Determines if a package can be shipped by ground"""
        if self.is_international:
            return (False, None, "Cannot ship ground internationally")

        cost = self.calculate_ground_cost()
        return (True, round(cost,2), None)

    def can_ship_overseas(self):
        """Determines if a package can be shipped overseas"""
        cost = self.calculate_overseas_cost()
        return (True, round(cost,2), None)

    def calculate_air_cost(self):
        """Calculate cost to ship by air based on weight and volume and return the most expensive"""
        COST_PER_KG = 10.0
        COST_PER_M3 = 20.0
        weight_cost = self.weight * COST_PER_KG
        volume_cost = self.volume * COST_PER_M3
        return max(weight_cost, volume_cost)
    
    def calculate_ground_cost(self):
        """Calculate cost to ship by ground"""
        URGENT_COST = 45.0
        REGULAR_COST = 25.0

        # use urgent cost if urgent
        if self.is_urgent:
            return URGENT_COST
        return REGULAR_COST
    
    def calculate_overseas_cost(self):
        """Calculate cost to ship overseas"""
        REGULAR_COST = 30.0

        return REGULAR_COST
    
    def convert_yes_or_no(self, variable):
        """Convert a y/n answer to True/False"""
        if variable == "y":
            return True
        return False
    
    def return_shipment_options(self):
        """Return shipment details for ground, air, and overseas"""
        options = {"ground": self.ground,
                   "air": self.air,
                   "overseas": self.overseas}
        return options
    
    def set_shipment(self, shipment):
        """Set the shipment in the form of {method: cost}"""
        self.shipment = shipment

    
    def prepare_for_csv(self, id):
        """
        Prepare the quote to be saved to a CSV in the form of:
        id, cust_name, ship_method, cost, deliver_date, desc, weight, volume, is dangerous?, is international?
        """
        save_data = [
            id,
            self.cust_name,
            list(self.shipment.keys())[0],
            list(self.shipment.values())[0],
            self.deliver_date,
            self.desc,
            round(self.weight,3),
            round(self.volume,3),
            self.is_dangerous,
            self.is_international
        ]
        return save_data
