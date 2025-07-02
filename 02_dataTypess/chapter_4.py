################### Boolean Data Types ###################

# Boolean data types are used to represent truth values, which can be either True or False.

is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling
print(f"Total actions: {total_actions}")  #=> Total actions: 6


is_milk_present = 0
print(f"Is milk present? {bool(is_milk_present)}")  #=> Is milk present? False

is_milk_present = None
print(f"Is milk present? {bool(is_milk_present)}")  #=> Is milk present? False

is_milk_present = 1
print(f"Is milk present? {bool(is_milk_present)}")  #=> Is milk present? True




################################## Logical Operators ##################################
#and_operator = True and False
#or_operator = True or False
#not_operator = not True

water_is_boiling = True
milk_is_present = False

can_serve_tea = water_is_boiling and milk_is_present   # Both conditions must be True
print(f"Can serve tea? {can_serve_tea}")  #=> Can serve tea? False

can_serve_tea = water_is_boiling or milk_is_present    # At least one condition must be True
print(f"Can serve tea? {can_serve_tea}")  #=> Can serve tea? True

can_serve_tea = not water_is_boiling   
print(f"Can serve tea? {can_serve_tea}")  #=> Can serve tea? False
