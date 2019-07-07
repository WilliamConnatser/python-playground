print("Python is dynamically typed language.. variables can change types!!")
print("Booleans have uppercase first letters like True and False");

print(f"True = {type(True)}")

print(f"1 = {type(1)}")

print(f"2.0 = {type(2.0)}")

string = "string"
print(f"\"string\" = {type(string)}")
    
print(f"[1,2,3] = {type([1,2,3])}")

dictt = {"key": "value"}
print(f"{{\"key\": \"value\"}} = {type(dictt)}")

print(f"None = {type(None)} (Python's version of null)")

print("You can convert data types using the applicable functions IE. float() str() int() etc")
print("f strings abstract away the conversion of non-string data types into strings implicitly")
print("But you can also do it manually when reassigning variables or in logic like this: str(1) = " + str(1))