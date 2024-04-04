from data_handler import verify_words, verify_ssn, verify_month, verify_day, verify_year, verify_date


def test_verify_words():
    LENGTH_LIMIT = 50
    test_string_1 = "a"*(LENGTH_LIMIT+1) # test upper limit
    test_string_2 = "a"*LENGTH_LIMIT # test limit
    test_string_3 = "hello i am jake" # test regular set of words
    test_string_4 = "-1" # test integer

    assert verify_words(test_string_1)[0] == False
    assert verify_words(test_string_2)[0] == True
    assert verify_words(test_string_3)[0] == True
    assert verify_words(test_string_4)[0] == False

def test_verify_ssn():
    test_string_1 = "123456789" # test valid ssn with no dashes
    test_string_2 = "123-45-6789" # test valid ssn with dashes
    test_string_3 = "12--45-6789" # test bad with extra dashes
    test_string_4 = "bat-mo-bile" # test words
    test_string_5 = "123-45-67890" # test too long

    assert verify_ssn(test_string_1)[0] == True
    assert verify_ssn(test_string_2)[0] == True
    assert verify_ssn(test_string_3)[0] == False
    assert verify_ssn(test_string_4)[0] == False
    assert verify_ssn(test_string_5)[0] == False

def test_verify_month():
    test_int_1 = "13" # test invalid month upper
    test_int_2 = "0" # test invalid month lower
    test_int_3 = "jake" # test word
    test_int_4 = "12" # test good month

    assert verify_month(test_int_1) == False
    assert verify_month(test_int_2) == False
    assert verify_month(test_int_3) == False
    assert verify_month(test_int_4) == True


def test_verify_day():
    test_month = "1" # test with january
    test_day_1 = "32" # test upper limit
    test_day_2 = "0" # test lower limit
    test_day_3 = "jake" # test word
    test_day_4 = "31" # test valid day

    assert verify_day(test_month, test_day_1, test_month) == False
    assert verify_day(test_month, test_day_2, test_month) == False
    assert verify_day(test_month, test_day_3, test_month) == False
    assert verify_day(test_month, test_day_4, test_month) == True


def test_verify_year():
    test_year_1 = "320103" # test year that is too far out
    test_year_2 = "100" # test year that is too soon
    test_year_3 = "jake" # test word
    test_year_4 = "2012" # test valid year

    assert verify_year(test_year_1) == False
    assert verify_year(test_year_2) == False
    assert verify_year(test_year_3) == False
    assert verify_year(test_year_4) == True