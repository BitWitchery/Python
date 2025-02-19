# Logical Operators Part 3

# When checking multiple conditions, the computer stops checking as soon as it knows the final answer.

# For example:

x = 0
y = 5
x != 0 and y / x > 2

# Here x equals 0, therefore it will not evaluate y / x > 2. If we were to reverse the order:

y / x > 2 and x != 0

# This will result in an error because y will be divided by 0 which is illegal in math.

# This technique used to optimize the evaluation of logical expressions. For example:

a = 0
b = 2
c = 3
d = 5
(a > 0 and b < 2) or (c < -5 and d < 10)

# In this example b < 2 and d < 10 will not be evaluated because a > 0 and c < -5 are both false.