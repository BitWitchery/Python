# Challenge
# Beginner

# You are given a code which gets as input a number that indicates the wind speed and stores it in a variable named wind.

# Note: we will learn in next lessons how to get input from the user, currently just don't touch the first line.

# Your task is to initialize variable status based on the conditions:

#    - "Calm" if wind is smaller than 8,
#    - "Breeze" if wind is between 8 and 31 (including 8 and 31).
#    - "Gale" if wind is between 32 and 63 (including 32 and 63)
#    - "Storm" otherwise

#     Check the test cases to see all the inputs and the expected outputs

wind = int(input()) # Don't change this line
status = "unset"
# Type your code below
if wind < 8:
    status = "Calm"
elif wind >= 8 and wind <= 31:
    status = "Breeze"
elif wind >= 32 and wind <= 63:
    status = "Gale"
else:
    status = "Storm"

# Don't change the line below
print(f"status = {status}")

###################################################################################################################

# Challenge
# Beginner

# You are given a code which gets as input a number that indicates the temperature in Celsius and stores it in a variable named temperature.

# Note: Don't modify the first line of the code.

 

# Your task is to initialize variable weather based on the following conditions:

#     - "Freezing" if temperature is below 0,
#     - "Cold" if temperature is between 0 and 15 (including 0 and 15).
#     - "Mild" if temperature is between 16 and 25 (including 16 and 25)
#     - "Hot" otherwise

#     Check the test cases to see all the inputs and the expected outputs

temperature = int(input()) # Don't change this line
weather = "unset"
# Type your code below
if temperature < 0:
    weather = "Freezing"
elif temperature >= 0 and temperature <= 15:
    weather = "Cold"
elif temperature >= 16 and temperature <= 25:
    weather = "Mild"
else:
    weather = "Hot"

# Don't change the line below
print(f"weather = {weather}")