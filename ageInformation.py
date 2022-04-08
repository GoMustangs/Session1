ageInput = input("Enter your age:")
age = int(ageInput)
if age <= 0:
    print("Invalid Age")
if age < 16:
    print("You're Not Old Enough to Drive")
if age >= 16:
    print("You Can Drive")
if age >= 18:
    print("You Can Vote")
if age >= 21:
    print("You Can Enjoy a Beer")
if age >= 55:
    print("You Can Get a Senior Discount")