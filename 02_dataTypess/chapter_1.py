
# Immutable types in Python
# Immutable types cannot be changed after they are created.
# only reference to the object can be changed.
# Examples of immutable types: int, float, str, tuple, frozenset


suger_value = 2
print(f"Initial suger value:{suger_value}")

suger_value = 12
print(f"Updated suger value: {suger_value}")

#  The value id's changed from 2 to 12

print(f"Id of 2: {id(2)}")
print(f"Id of  12: {id(12)}")