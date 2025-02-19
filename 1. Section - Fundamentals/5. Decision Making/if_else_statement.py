# If - Else

# if allows us to execute particular code if a condition is met, but what if we want to execute something else if the condition is not met?

# For that we have the else statement:

age = 15
status = "None"
if age >= 18:
    status = "Adult"
else:
    status = "Young"

# In the above example, age is smaller than 18 which means it enter the else code and status will hold "Young".

# We can even make it more profound using the elif statement:

age = 68
status = "None"
if age < 18:
    status = "Young"
elif age >= 18 and age <= 65:
    status = "Adult"
else:
    status = "Old"

# Here it checks whether age is smaller than 18, if not it will continue to the next condition and check whether age is between 18 and 65. If that condition is also not met it will set status to "Old".

# We can add as many elif statements as we want:

# if condition1:
#     code
# elif condition2:
#     code
# elif condition3:
#     code
# ...

#     Note that the code inside the if/elif/else must be indented
