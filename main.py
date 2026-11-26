from models import *

def show_menu():
    print("\nMeny")
    print("1. Lägg till vana")
    print("2. Checka in vana")
    print("3. Avsluta")

    print(f"\nVanor: {habit_manager.print_habits()}")
    print(f"Avklarade vanor: {habit_manager.print_finished_habits()}")


habit_manager = HabitManager()

while True:
    show_menu()
    user_input = input("\nVälj alternativ: ")

    if user_input == "1":
        habit_name = input("Namn på vana (T.ex. Dricka 2L vatten): ")
        habit_count = input("Hur många gånger det ska gå att checka in vanan (T.ex. 2): ")
        habit_manager.add_habit(habit_name, int(habit_count))

    elif user_input == "2":
        habit_name = input("Namn på vana att checka in: ")
        if habit_manager.check_in_habit(habit_name):
            print("\nDu har checkat in vanan")
        else:
            print("\nVanan finns inte")
            
                
    elif user_input == "3":
        print("Avslutar...")
        break
    else:
        print("Välj mellan 1 och 3")
