from models import *

def show_menu():
    print("\nMeny")
    print("1. Lägg till vana")
    print("2. Checka in vana")
    print("3. Spara")
    print("4. Avsluta")

    print(f"\nVanor: {habit_manager.get_habit_list_names()}")
    print(f"Avklarade vanor: {habit_manager.get_finished_habits_names()}")


habit_manager = HabitManager()

while True:
    show_menu()
    user_input = input("\nVälj alternativ: ")

    if user_input == "1":
        habit_name = input("Namn på vana: ")
        habit_manager.add_habit(habit_name)

    elif user_input == "2":
        habit_name = input("Namn på vana att checka: ")
        if habit_name in habit_manager.get_habit_list_names():
            index = habit_manager.get_habit_list_names().index(habit_name)
            habit_manager.check_habit(index)
        else:
            print("Vanan finns inte")
            
                
    elif user_input == "3":
        print("Sparar...")
    elif user_input == "4":
        print("Avslutar...")
        break
    else:
        print("Välj mellan 1 och 4")
