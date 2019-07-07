print("How many miles did you travel?")
miles = input()
print(f"You entered {miles} miles. Good job!!")
kilometers = float(miles) * 1.60934
print(f"If you aren't American, then {miles} miles equals {round(kilometers,2)} kilometers!!")