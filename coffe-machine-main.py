drink_list = ["Espresso", "Americano", "Americano w Milk",
               "Latte", "Cappuccino", "Flat-White"]

user_input = None

def input_message(run_flag):
    str_greeting = "\nHello! Would you like a drink?\n"
    str_another_drink = "\nWould you like another one?\n"
    str_input_guidelines = "\nInput [1] for YES, [0] for NO:\n"
    if run_flag:
        input_message = int(input(f"{str_greeting} {str_input_guidelines}"))
    else:
        input_message = int(input(f"{str_another_drink} {str_input_guidelines}"))
    return input_message


def print_drink_list() -> None:
    for id, drink_name in enumerate(drink_list):
        print(f"\n[{int(id) + 1}] - {drink_name}")


def prepare_drink(drink_id, sugar_amount):
    print(f"\nHere is your {drink_list[int(drink_id)-1]} " \
          f"with {sugar_amount} sugar! Enjoy!\n")


def select_drink():
    while True:
        try:
           drink_value = int(input("\nPlease, select a drink:\n"))
        except ValueError:
            print("\nPlease input a number!")
        else:
            if 1 <= drink_value <= len(drink_list):
                break  
            else:
                print("\nSelect a valid drink number!")
    return drink_value



def add_sugar():
    while True:
        try:
            sugar_qty = int(input("\nSelect sugar, 0 - 5.\n\n" \
                                  "[0] - None, [5] - Hella lot:\n"))
        except ValueError:
            print("\nPlease input a number!")
        else:
            if 5 < sugar_qty or sugar_qty < 0:
                print("\nInvalid number! Please input 0 - 5.")
            else:
                break
    return sugar_qty


def main():
    first_run = True

    while True:
        try:
            user_input = input_message(first_run)
        except ValueError:
            print("\nPlease input a number!")
        else:
            if user_input != 0 and user_input != 1:
                print("\nInvalid input! Please try again.")
            else:
                first_run = False
                break

    
    while user_input:
        print_drink_list()
        selected_drink = select_drink()
        sugar_amount = add_sugar()
        prepare_drink(selected_drink, sugar_amount)
        user_input = input_message(first_run)
        if user_input == 0:
            break


    return print("\nHave a great day!")


main()
