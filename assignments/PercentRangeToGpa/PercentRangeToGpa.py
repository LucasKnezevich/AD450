# Variables for input and input validity
percent_grade = None
valid_input = False

# Get user input
while(valid_input == False):
  percent_grade = float(input('\nEnter grade percentage (must be greater than 0): '))
  valid_input = percent_grade >= 0.0

  if valid_input == False:
    print("\nInvalid input, grade must be greater than 0.0")

# Fucntion for calculating GPA from percentage
def percent_to_gpa(percent_grade):
  if percent_grade >= 95.0:
    return '4.0'
  elif percent_grade < 65.0:
    return '0.0'
  else:
    return str(
      percent_grade / 20 - 1
    )

# Display result
print('\nPercent grade is: ' + str(percent_grade) + '%\nGPA is: ' + percent_to_gpa(percent_grade) + '\n')