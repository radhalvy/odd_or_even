positive_answers = ["y", "yes", "Y", "Yes", "si", "Si", "s", "S"]
negative_answers = ["n", "N", "no", "No"]
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
            print("The number you entered is even.\n")
            print("Do you want to enter another number?")
            continue_or_not = input("Answer: ")
            if continue_or_not in positive_answers:
                following_loop = True
            elif continue_or_not in negative_answers:
                print("\nGoodbye.")
                following_loop = False
            else:
                print("\nInvalid answer. Closing the program...")
                following_loop = False
        else:
            print("The number you entered is odd.\n")
            print("Do you want to enter another number?")
            continue_or_not = input("Answer: ")
            if continue_or_not in positive_answers:
                following_loop = True
            elif continue_or_not in negative_answers:
                print("\nGoodbye.")
                following_loop = False
            else:
                print("\nInvalid answer. Closing the program...")
                following_loop = False


odd_even()
