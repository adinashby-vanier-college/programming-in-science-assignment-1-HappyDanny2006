# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3): 
    maximum = max(num1, num2, num3)
    return(maximum)

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    return(min(num1, num2, num3))

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    result = ""
    if (number < 0):
        result += ("Negative")
    elif (number == 0):
        result += ("Zero")
    else:
        result += ("Positive")
    return(result)
# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.

def star_shape(rows):
    result = ""
    count = 1
    for i in range(1, rows+1):
        result += "*" * (count) + "\n"
        count += 1
    return(result[0:-1])
    

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    number = 1

    while number <= limit:
        if number % 3 == 0:
            print("remainder of 3")
        else:
            print(number)
    number += 1

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(result, limit):
    result = 0
    for i in range (result, limit + 1):
        if i % 2 == 0:
            result += i
    return(result)
