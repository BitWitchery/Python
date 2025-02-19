# Challenge
# Beginner

# Write a program that get input from the user (their name), and then outputs Hello, 
# followed by a space and the user's inputted name.

# For example, if the user inputs Bob, the expected output is Hello, Bob.

# You will need to:

#     1. Use input() to get input from the user.
#     2. Store the input in a variable.
#     3. Print Hello, and the stored variable in the end (add a space after the comma).

# Write code here
name = input()
print(f"Hello, {name}")

################################################################################################

# Challenge
# Beginner

# Create a program that receives that user name and age, then calculates and prints how old they will be in 10 years.

# The output should be in the format: "In 10 years, [name] will be [age] years old."

# You will need to:

#     1. Use input() to get the user's name and age.
#     2. Store the inputs in variables.
#     3. Convert the age to an integer and add 10 to it.
#     4. Print the result using an f-string.

name = input()
age = int(input())
# Write code here

new_age = int(age)
new_age += 10

print(f"In 10 years, {name} will be {new_age} years old.")