# Should You Go for a Walk?
# You’re deciding whether to go for a walk based on two real-life conditions:

# is_sunny = True

# have_umbrella = False



# Print the result of the following:

# Should you go for a walk if it’s sunny and you don’t need an umbrella?

# Should you go for a walk if it’s sunny or if you have an umbrella?

# Is it not sunny today?

# Do you not have an umbrella?




is_sunny = True
have_umbrella = False

# Should you go for a walk if it’s sunny and you don’t need an umbrella?
can_go_for_walk = is_sunny and not have_umbrella
print(f"Can go for a walk if it's sunny and no umbrella: {can_go_for_walk}")  #=> Can go for a walk if it's sunny and no umbrella: True
# Should you go for a walk if it’s sunny or if you have an umbrella?
can_go_for_walk = is_sunny or have_umbrella
print(f"Can go for a walk if it's sunny or have umbrella: {can_go_for_walk}")  #=> Can go for a walk if it's sunny or have umbrella: True
# Is it not sunny today?
is_not_sunny = not is_sunny
print(f"Is it not sunny today? {is_not_sunny}")  #=> Is it not sunny today? False
# Do you not have an umbrella?
do_not_have_umbrella = not have_umbrella
print(f"Do you not have an umbrella? {do_not_have_umbrella}")  #=> Do you not have an umbrella? True