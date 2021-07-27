positive_answers = ["Y", "YES", "S", "SI"]
negative_answers = ["N", "NO"]
user_num = ""

def get_input():
    try:
        user_num = int(input("Enter the number: ")) % 2
    except ValueError:
        print("Invalid integer.")
        return
    return user_num


def odd_even(user_input_function):
    state = True
    while state:
        user_input_function = get_input()
        if user_input_function == 1:
            print("\nThe number is odd.")
        else:
            print("\nThe number is even.")
        print("\nDo you want to enter another number?")
        another_num_user = input("\nAnswer: ")
        if another_num_user.upper() in positive_answers:
            state = True
        elif another_num_user.upper() in negative_answers:
            state = False
        else:
            print("\nInvalid answer. Closing the program...")


odd_even(user_num)
