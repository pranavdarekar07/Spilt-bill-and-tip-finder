print("Spilt bills and tip finder ")

total = float(input("Enter the total bill : $"))
spilt = int(input("Bill split in how many members : "))
tip = float(input("How much percent tip you want to give : "))

final = (total+(total*(tip/100)))/spilt

print(f"Each person have to pay ${final}.")