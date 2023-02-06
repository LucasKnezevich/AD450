import math

# Variables for input and input validity
percent_grade = None
valid_input = False

# Get user input, repeat until it is valid or user types exit
while(valid_input == False):
  user_input = input('\nEnter grade percentage (must be greater than 0) or \'exit\' to quit: ')

  if user_input.lower() == 'exit':
    exit()

  percent_grade = float(user_input)
  valid_input = percent_grade >= 0.0

  if valid_input == False:
    print("\nInvalid input, grade must be greater than 0.0")

# Fucntion for calculating GPA from percentage
def percent_to_gpa(grade_percentage):
  if grade_percentage >= 95.0:
    return 4.0
  elif grade_percentage < 65.0:
    return 0.0
  else:
    return (grade_percentage - 65) / 10 + 1

# Function that rounds GPA down to one decimal place, returns a string
def get_gpa_string(gpa):
  return str(math.floor(gpa * 10) / 10)

# Display result
print('\nPercent grade is: ' + str(percent_grade) + '%\nGPA is: ' + get_gpa_string(percent_to_gpa(percent_grade)) + '\n')