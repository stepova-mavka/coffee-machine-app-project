drink_list = ["Espresso", "Americano", "Americano w Milk", "Late", "Cappuchino", "Flat-White"]
userInput = None

def print_Drink_List():
    for id, drink_name in enumerate(drink_list):
        print(f"[{int(id) + 1}] - {drink_name}\n")


def prepare_Drink(drink_id, sugar_amount):
    print(f"Here is your {drink_list[int(drink_id)-1]} with {sugar_amount} sugar! Enjoy!\n\n")


def add_Sugar():
    while True:
        try:
            sugar_qty = int(input("Select sugar, 0 - 5.\n[0] - None, [5] - Hella lot:\n"))
        except ValueError:
            print("Please input a number!\n")
        else:
            if 5 < sugar_qty or sugar_qty < 0:
                print("Invalid number! Please input 0 - 5.\n")
            else:
                break
    return sugar_qty


def main(userInput):

    while userInput != 0 and userInput != 1:
        try:
            userInput = int(input("Hello! Would you like a drink?\nInput [1] for YES, [0] for NO:\n"))
        except ValueError:
            print("Please input a number!\n")
        else:
            if userInput != 0 and userInput != 1:
                print("Invalid input! Please try again.\n")

    
    while userInput:
        print_Drink_List()
        selected_drink = input("Please, select a drink: ")
        sugar_amount = add_Sugar()
        prepare_Drink(selected_drink, sugar_amount)
        userInput = int(input("Would you like another one?\nInput [1] for YES, [0] for NO:\n"))
        if userInput == 0:
            break
        else:
            pass


    return print("Have a great day!")


main(userInput)
