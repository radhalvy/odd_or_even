def odd_even():
    following_loop = True
    while following_loop == True:
        try:
            user_num = int(input("Enter the number: "))
        except ValueError:
            print("Invalid number.")
            return
        zero_or_one = user_num % 2
        if zero_or_one == 0:
            print("The number you entered is even.")
            print("Do you want to enter another number?")
            continue_or_not = input("Answer: ")
            if continue_or_not != "yes":
                print("Goodbye.")
                following_loop = False
            else:
                following_loop = True
        else:
            print("The number you entered is odd.")
            print("Do you want to enter another number?")
            continue_or_not = input("Answer: ")
            if continue_or_not != "yes":
                print("Goodbye.")
                following_loop = False
            else:
                following_loop = True


odd_even()
