# Cast

# To convert the input to a different type, we need to cast.

# To cast a string to an int (a whole number), we will write:

var = input()
var = int(var)

# Or in one line,

var = int(input())

# If the input is a number, i.e. 5, 4, 54 then var will hold a number. If the input contains an invalid number: 5ab, bb, akt, etc. then the program will fail.

# Here is a table that shows how to cast to different types:
# Cast	    -> Explanation
# int()	    -> Convert to a whole number
# float()	-> Convert to a real number
# bool()	-> Convert to a boolean
# str()	    -> Convert to a string

#     It is important to use the right type because it can affect the output.

#    Adding two strings will result in:

#     "5" + "5" = "55"

#    Adding two numbers will result in:

#     5 + 5 = 10
