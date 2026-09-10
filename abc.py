gender = input("Enter your gender (male/female): ").lower()
age = int(input("Enter your age: "))

# Check eligibility using nested if-else blocks
if gender == "male":
    if age >= 21:
       print("Marriage allowed.")
    else:
        print("Marriage not allowed.")

elif gender == "female":
    if age >= 18:
        print("Marriage allowed.")
    else:
        print("Marriage not allowed.")

else:
     print("Invalid input. Please enter male or female.")