### Questions

## Question 1

my_string = "Jake"
my_integer = 6
my_float = 6.0

## Question 2

int1 = 7
int2 = 9
result = int1 + int2
# The result should be 16 below
print(result)

## Question 3

float1 = 3.3
float2 = 4.7
result = float1 + float2
# The result should be 8.0
print(result)

## Question 4

string1 = "Jake"
string2 = " Horstmann"
result = string1 + string2
# The result should be Jake Horstmann
print(result)

## Question 5

num1 = 8
num2 = 5.2
result = num1 + num2
# The result should be 13.2
print(result)

## Question 6

num1 = 4
string1 = "4"
# result = num1 + string1
# print(result)
# The output was an error because strings and numbers are not naturally concatenated

### Try now tasks

## Task 1

print("my_string =", type(my_string), "my_integer =",type(my_integer), "my_float =", type(my_float))

## Task 2

fake_num = "4"
print("fake_num type is", type(fake_num))
fake_num = int(fake_num)
print("fake_num type is now",type(fake_num))

## Task 3

num1 = 5
num2 = 7.654321
result = num1 * num2
print(round(result,3))

## Task 4

my_name = input("Please enter your name ")
print("Your name is", my_name)

## Task 5

favorite_number = input("Please enter your favorite number ")
print("Your favorite number is", favorite_number)
# I expect this to be a string since input returns a string
print("favorite_number is a",type(favorite_number))
# Input returns a string

## Task 5

int1 = input("Please enter an integer ")
int2 = input("Please enter another integer ")
result = int1 + int2
# Since those are strings this should be a concatenation of the two
print(result)
# It was the concatenation of the two of them because input returns strings
int1 = int(int1)
int2 = int(int2)
result2 = int1 + int2
print(result2)
