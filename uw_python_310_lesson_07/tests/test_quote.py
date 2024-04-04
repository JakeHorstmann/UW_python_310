from src.assignment07 import quote

test_quote = quote.Quote({"cust_name": "Jake",
                            "desc": "a person",
                            "is_dangerous": "y",
                            "weight": 4.5,
                            "volume": 67.24,
                            "deliver_date": "1/1/2024",
                            "is_international": "n"
                         })

def test_can_be_shipped():
    test = test_quote
    test.weight = 4.5
    test.volume = 67.24
    test = test_quote
    assert test.can_be_shipped() == True
    test.weight = 100
    assert test.can_be_shipped() == False
    test.weight = 4.5
    test.volume = 241
    assert test.can_be_shipped() == False
    test.volume = 125
    assert test.can_be_shipped() == False
    test.weight = 10
    test.volume = 67.24
    assert test.can_be_shipped() == False

def test_can_ship_air():
    test = test_quote
    test.is_dangerous = False
    assert test.can_ship_air()[0] == True
    test.is_dangerous = True
    assert test.can_ship_air()[0] == False

def test_can_ship_ground():
    test = test_quote
    test.is_international = False
    assert test.can_ship_ground()[0] == True
    test.is_international = True
    assert test.can_ship_ground()[0] == False

def test_calculate_air_cost():
    test = test_quote
    test.weight = 3
    test.volume = 10
    assert test.calculate_air_cost() == 200
    test.volume = 1
    assert test.calculate_air_cost() == 30

def test_calculate_ground_cost():
    test = test_quote
    test.is_urgent = False
    assert test.calculate_ground_cost() == 25
    test.is_urgent = True
    assert test.calculate_ground_cost() == 45

