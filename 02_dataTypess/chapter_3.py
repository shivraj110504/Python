# Intergers

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")    #=>  Total grams of base tea is 17

# Subtraction

remaing_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaing_tea}")   #=> Total grams of remaining tea is 11



# Division# Integer division

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")   #=> Milk per serving is 1.75


total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")   #=> While tea bags per pot: 1


# Modulus


total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover C pods {leftover_pods}")    #=> Leftover C pods 1

# Exponentiation
# Exponentiation is used to calculate powers
# For example, if you want to calculate 2 raised to the power of 3,
# you can use the ** operator.
# This is equivalent to 2 * 2 * 2, which equals 8.
# In Python, you can use the ** operator to perform exponentiation.

base_flavor_strength = 2
scale_factor = 3
powerful_falvour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strenght {powerful_falvour}")   #=> Scaled flavour strenght 8
# 2 * 2 * 2


# Large Integers
# Python can handle very large integers without any issues.
# For example, you can represent a billion as 1_000_000_000.
# This is a convenient way to write large numbers, making them more readable.

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")   #=> tea leaves: 1000000000