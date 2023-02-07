"""
For calculating GPA based on percentage.
"""
import math
import sys

# Variables for input and input validity
PERCENT_GRADE = None
VALID_INPUT = False

# Get user input, repeat until it is valid or user types exit
while VALID_INPUT is False:
    user_input = input('\nEnter grade percentage (must be greater than 0) or \'exit\' to quit: ')

    if user_input.lower() == 'exit':
        sys.exit('Goodbye.')

    PERCENT_GRADE = float(user_input)
    VALID_INPUT = PERCENT_GRADE >= 0.0

    if VALID_INPUT is False:
        print("\nInvalid input, grade must be greater than 0.0")

"""Fucntion for calculating GPA from percentage"""
def percent_to_gpa(grade_percentage):
    if grade_percentage >= 95.0:
        return 4.0
    if grade_percentage < 65.0:
        return 0.0
    else:
        return (grade_percentage - 65) / 10 + 1

"""Function that rounds GPA down to one decimal place, returns a string"""
def get_gpa_string(gpa):
    return str(math.floor(gpa * 10) / 10)

# Display result
print('\nPercent grade is: ' + str(PERCENT_GRADE) + '%\nGPA is: ' + 
    get_gpa_string(percent_to_gpa(PERCENT_GRADE)) + '\n')
