# Logical Operators Part 4

# When working with logical expressions, sometimes we need to simplify or rearrange them.

# For example, not in front of two conditions joined by and, can be split into two separate parts. The and becomes or, and each part gets its own not:

# not (A and B) is the same as (not A) or (not B)

# For example:

# Let's check if a number is NOT (between 1 and 10)
number = 15

# These two expressions are equivalent:
result1 = not (number >= 1 and number <= 10)
result2 = (not number >= 1) or (not number <= 10)

print(result1)  # True
print(result2)  # True

# The opposite is also correct: not (A or B) is the same as (not A) and (not B)

# For example:

# Checking if a person is NOT (a student or employed)
is_student = False
is_employed = False

# These two expressions are equivalent:
result1 = not (is_student or is_employed)
result2 = (not is_student) and (not is_employed)

print(result1)  # True
print(result2)  # True