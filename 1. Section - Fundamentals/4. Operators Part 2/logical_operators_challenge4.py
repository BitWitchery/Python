# Challenge
# Beginner

# You're helping a pet shop create a system to determine if they can sell a pet to a customer.

# initialize the following variables:

#     has_license with the value True
#     has_space with the value True
#     has_experience with the value False

# Write the following logical expressions to determine if:

#     can_sell_regular_pet: Customer needs EITHER a license OR experience, AND must have space
#     can_sell_exotic_pet: Customer needs BOTH a license AND experience, AND must have space
#     cannot_sell_any_pet: Customer has NO license AND NO experience, OR has NO space

# Initialize variables
has_license = True
has_space = True
has_experience = False

# Calculate conditions
can_sell_regular_pet = has_license or has_experience and has_space
can_sell_exotic_pet = has_license and has_experience and has_space
cannot_sell_any_pet = not has_license and not has_experience and not has_space

# Don't delete the lines below
print("Can sell regular pet:", can_sell_regular_pet)
print("Can sell exotic pet:", can_sell_exotic_pet)
print("Cannot sell any pet:", cannot_sell_any_pet)

#####################################################################################################

# Challenge
# Easy

# You're helping a transportation company create a system to determine if a person can drive certain vehicles.

# Initialize the following variables:

#     has_license with the value True
#     has_experience with the value False
#     has_clean_record with the value True

# Write the following logical expressions to determine if:

#     can_drive_car: Person needs a license AND a clean record
#     can_drive_truck: Person needs a license AND experience AND a clean record
#     cannot_drive_any: Person has NO license OR NO clean record

# Initialize variables
has_license = True
has_experience = False
has_clean_record = True
# Calculate conditions
can_drive_car = has_license and has_clean_record
can_drive_truck = has_license and has_experience and has_clean_record
cannot_drive_any = not has_license or not has_clean_record

# Don't delete the lines below
print("Can drive car:", can_drive_car)
print("Can drive truck:", can_drive_truck)
print("Cannot drive any:", cannot_drive_any)