# Logical Operators Part 1

# Logical operators are used to check combinations of comparisons that return True or False.

# For example the following statement contains two comparisons: 

# Is 5 greater than 3 and less than 6?
# Operator	Meaning	                                Example
# and	    And - True if all operands are True	    a and b
# or	    Or - True if any operand is True	    a or b
# not	    Not - True if the operand is False	    #not a

###############################################################################################

# Let's look at some examples:

# 5 is greater than 3 and 1 equal to 1:

b1 = (5 > 3) and (1 == 1) # evaluates to true

# Explanation: All of the operands are True, so b1 will 
# hold True (and operation is True if both operands are True) .

###############################################################################################

# 5 is not equal to 4 or 5 is equal to 2:

b2 = not 5 == 4 or 5 == 2 # evaluates to true

# Explanation: The first operand (not 5 == 4) is True so 
# b2 is also True because or operation is True if either one of the operands is True.

###############################################################################################

# 1 is not equal to 1 or false:

b3 = not 1 == 1 or False # evaluates to false

# Explanation: All of the operands are False, so b3 will hold False (or operation).

###############################################################################################

# not (3 greater than 4):

b4 = not (3 > 4) # evaluates to true

# Explanation: The operand is False, so b4 will hold True (not operation).

###############################################################################################

# not (5 greater than 10 or 5 greater than 1):

b5 = not (5 > 10 or 5 > 1) # evaluates to false

# Explanation: 5 > 10 or 5 > 1 is True (one of the operands is True), 
# so in total b5 is False (not operation).