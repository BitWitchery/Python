# Challenge
# Beginner

# Write a program that determines if it is a good day for solar panel energy production

# Initialize these variables:

#     is_sunny with the value True
#     wind_speed with the value 5.4
#     temperature with the value 23
#     solar_panel_output with the value 9
#     is_cloudy with the value False

# Write a single logical expression to check all of the following conditions:

#     It's sunny
#     The wind speed is less than 10
#     The solar panel output is less than 15
#     The temperature is above 20 OR there are no clouds

# Initialize variables
is_sunny = True
wind_speed = 5
solar_panel_output = 10
temperature = 25
is_cloudy = True

# The complete logical expression
result = True

# Don't delete the lines below
print("Checking conditions for solar energy production...")
print("1. Is it sunny?", is_sunny)
print("2. Is wind speed safe?", wind_speed < 10)
print("3. Can panels produce more?", solar_panel_output < 15)
print("4. Is temperature good OR no clouds?", (temperature > 20 or not is_cloudy))
print("\nFinal result - Good day for solar energy production:", result)

#################################################################################################

# Challenge
# Easy

# You're helping a weather app determine suitable outdoor activities based on weather conditions. Create a program that uses logical operations to determine if certain activities are possible.

# Initialize the following variables:

#     is_sunny with the value True
#     temperature with the value 25
#     wind_speed with the value 10
#     water_temperature with the value 22

# Write the following logical expressions to determine if:

#     can_go_hiking: It's sunny AND temperature is above 15°C AND wind speed is below 20 km/h
#     can_go_swimming: It's sunny AND temperature is above 20°C AND water temperature is above 18°C
#     cannot_go_outside: It's NOT sunny OR temperature is below 10°C OR wind speed is above 30 km/h

# Initialize variables
is_sunny = True
temperature = 25
wind_speed = 10
water_temperature = 22
# Calculate conditions
can_go_hiking = is_sunny and temperature > 15 and wind_speed < 20
can_go_swimming = is_sunny and temperature > 20 and water_temperature > 18
cannot_go_outside = not is_sunny or temperature < 10 or wind_speed > 30

# Don't delete the lines below
print("Can go hiking:", can_go_hiking)
print("Can go swimming:", can_go_swimming)
print("Cannot go outside:", cannot_go_outside)