while True:
    male_age = int(input("Enter male age: "))
    female_age = int(input("Enter female age: "))

    if male_age >= 21 and female_age >= 18:
     print("Marriage allowed for both.")
    else:
        print("marriage not allowed for both")
        if male_age < 21:
         print("Male: Marriage not allowed.")
        else:
         print("Male: Marriage allowed.")

    if female_age < 18:
        print("Female: Marriage not allowed.")
    else:
        print("Female: Marriage allowed.")
