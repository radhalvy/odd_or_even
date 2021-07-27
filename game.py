positive_answers = ["Y", "YES", "S", "SI"]
negative_answers = ["N", "NO"]
def odd_even():
    loop_state = True
    while loop_state:
        try:
            user_num = int(input("Enter the number: "))
        except ValueError:
            print("\nInvalid number.")
            return
        if user_num % 2 == 0:
            print("\nThe number you entered is even.\n")

        else:
            print("\nThe number you entered is odd.\n")

        print("Do you want to enter another number?")
        another_num_user = input("\nAnswer: ")
        if another_num_user.upper() in positive_answers:
            loop_state = True
        elif another_num_user.upper() in negative_answers:
            print("\nGoodbye.")
            loop_state = False
        else:
            print("\nInvalid answer. Closing the program...")
            loop_state = False


odd_even()
