while True:
    age = int(input("What's your age?"))

    if age >= 55:
        if age < 75:
            print("Hello Boomer!")
        else:
            print("Hello wise one!")  
    else:
        print("Hello young one!")
    print("")
    print("-"*15)
