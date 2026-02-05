drink_list = ["Espresso", "Americano", "Americano w Milk", "Late", "Cappuchino", "Flat-White"]
userInput = None

def print_Drink_List():
    for id, drink_name in enumerate(drink_list):
        print(f"\n[{int(id) + 1}] - {drink_name}")


def prepare_Drink(drink_id, sugar_amount):
    print(f"\nHere is your {drink_list[int(drink_id)-1]} with {sugar_amount} sugar! Enjoy!\n")


def select_Drink():
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



def add_Sugar():
    while True:
        try:
            sugar_qty = int(input("\nSelect sugar, 0 - 5.\n\n[0] - None, [5] - Hella lot:\n"))
        except ValueError:
            print("\nPlease input a number!")
        else:
            if 5 < sugar_qty or sugar_qty < 0:
                print("\nInvalid number! Please input 0 - 5.")
            else:
                break
    return sugar_qty


def main(userInput):

    while userInput != 0 and userInput != 1:
        try:
            userInput = int(input("\nHello! Would you like a drink?\n\nInput [1] for YES, [0] for NO:\n"))
        except ValueError:
            print("\nPlease input a number!")
        else:
            if userInput != 0 and userInput != 1:
                print("\nInvalid input! Please try again.")

    
    while userInput:
        print_Drink_List()
        selected_drink = select_Drink()
        sugar_amount = add_Sugar()
        prepare_Drink(selected_drink, sugar_amount)
        userInput = int(input("\nWould you like another one?\n\nInput [1] for YES, [0] for NO:\n"))
        if userInput == 0:
            break
        else:
            pass


    return print("\nHave a great day!")


main(userInput)
