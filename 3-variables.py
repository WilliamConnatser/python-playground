reassigned = "Variables"
reassigned = "Variables can be reassigned"
total_message = reassigned + " and used as a value while declaring new variables"
print(total_message)

_valid_variable_name = "variables must start with an underscore or a letter"
valid_variable_name2 = "numbers are cool, but not for the start of the variable name"

print(_valid_variable_name)
print(valid_variable_name2)

different_variable = True
DIFFERENT_VARIABLE = False

print(different_variable == DIFFERENT_VARIABLE)

print("Most variables should be snake cased and lowercase")
print("Constants are uppercase")
print("Camel case is used for classes")
print("Double underscore are supposed to be private or left alone")
print("Python is dynamically typed language.. variables can change types!!")

print("Stay away from reserved key words for variables. It will work, but it reassigns them to variable's value, and if you try to access the reserved function later it will break.")
print("IE. don't use print int float bool input round etc")