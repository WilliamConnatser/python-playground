valid_sting = "double quotes are cool"
print(valid_sting)
valid_sting = 'single quotes are cool as well'
print(valid_sting)
valid_sting = "\t Escape characters \n work similarly \n to other programming languages \" \\ "
print(valid_sting)
valid_sting = "Curly braces must be escaped differently in f strings by using double curly braces: {{ or }}"
print(valid_sting)

f_string = "You can use what's called an f string for implicit string interpolation (put a variable or logic inside a string)"
print(f"Check this out {f_string}")

explicit_interpolation = "You can also explicitly interpolate variables using data-type-specific functions IE. float() str() int() etc..."
print(f"{explicit_interpolation} like this: {str(9999999999)}")

first_string = "String can also "
second_string = "be concatenated using +"
print(first_string + second_string)

print("Unlike Javascript, you can not concatenate non-strings to strings")

strings_are_indexed = "Strings are indexed you can access individual characters via their index"
print(f"{strings_are_indexed} - The first character of the last sentence is {strings_are_indexed[0]}")
print(f"Positive index #s start from the first character of the string. Negative integers start count at the last character of the string: {strings_are_indexed[-1]}")