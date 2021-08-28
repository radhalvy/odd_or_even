positive_answers = ["Y", "YES", "S", "SI"]
negative_answers = ["N", "NO"]


def get_input():
    try:
        user_num = int(input("Enter the number: ")) % 2
    except ValueError:
        print("\nInvalid integer.\n")
        return
    return user_num


def odd_even():
    state = True
    while state:
        user_num = get_input()
        if user_num == 1:
            print("\nThe number is odd.")
        elif user_num == 0:
            print("\nThe number is even.")
        else:
            return
        print("\nDo you want to enter another number?")
        another_num_user = input("\nAnswer: ")
        if another_num_user.upper() in positive_answers:
            state = True
        elif another_num_user.upper() in negative_answers:
            state = False
        else:
            print("\nInvalid answer. Closing the program...")
            return


odd_even()
