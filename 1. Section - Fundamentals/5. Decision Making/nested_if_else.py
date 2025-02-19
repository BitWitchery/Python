# Nested If - Else

# We can nest if-elif-else statements within each other. This allows us to create hierarchical decision-making structures.

# For example:

if age > 18:
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
else:
    print("Too young to drive")

# It can be infinite nested:

if condition1:
    # if condition1 is True
    if condition2:
        # if condition1 and condition2 are True
        if condition3:
            # if condition1, condition2 and condition3 are True
            ...