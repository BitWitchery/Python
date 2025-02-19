# Challenge
# Beginner

# Create a program that checks if someone can ride a rollercoaster. The requirements are:

#     Must be at least 12 years old
#     Must be taller than or equal 150cm
#     If they meet both requirements but are under 15, they need adult supervision

# Print exactly these messages for each case:

#     If too young: Sorry, you're too young
#     If not tall enough: Sorry, you're not tall enough
#     If under 15 and no adult: Sorry, you need an adult with you
#     If under 15 with adult: You can ride with adult supervision!
#     If 15 or older and tall enough: You can ride by yourself!

age = int(input()) # Don't change this line
height = int(input()) # Don't change this line
has_adult = input() == "True" # Don't change this line

# Write your code below
if age >= 12:
    if height >= 150:
        if age < 15:
            if has_adult:
                print("You can ride with adult supervision!")
            else:
                print("Sorry, you need an adult with you")
        else:
            print("You can ride by yourself!")
    else:
        print("Sorry, you're not tall enough")
else:
    print("Sorry, you're too young")
    
#######################################################################################################################

# Challenge
# Beginner

# Create a program for a game character creation system. The requirements are:

# The character's level determines what weapons they can use:

#     Level 1-5: Can only use Basic weapons
#     Level 6-10: Can use Advanced weapons if they completed training
#     Level 11+: Can use any weapon

# Print these messages based on the conditions:

#     If level 1-5: Basic weapons only
#     If level 6-10 and no training: Need weapon training first
#     If level 6-10 and has training: Access to advanced weapons granted
#     If level 11+: Access to all weapons granted
#     If level is 0 or negative: Invalid level

level = int(input()) # Don't change this line
has_training = input() == "True" # Don't change this line

# Write your code below

if level > 0:  
    if level <= 5:
        print("Basic weapons only")
    else:
        if level <= 10:
            if has_training:
                print("Access to advanced weapons granted")
            else:
                print("Need weapon training first")
        else:
            print("Access to all weapons granted")
else:
    print("Invalid level")