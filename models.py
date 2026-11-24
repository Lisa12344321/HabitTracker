import json


class HabitManager():
    def __init__(self):
        self.__habit_list = []
        self.__finished_habits = []

    def save(self):
        pass

    def load(self):
        pass

    def add_habit(self, habit_name):
        self.__habit_list.append(Habit(habit_name))

    def check_habit(self, habit_index):
            habit = self.__habit_list[habit_index]
            habit.check()
            self.__habit_list.remove(habit)
            self.__finished_habits.append(habit)


    def remove_habit(self):
        pass

    def get_habit_list_names(self):
        names = [habit.get_name() for habit in self.__habit_list]
        return ", ".join(names)

    def get_finished_habits_names(self):
        names = [habit.get_name() for habit in self.__finished_habits]
        return ", ".join(names)



class Habit():
    def __init__(self, name):
        self.__name = name
        self.__state = "0/1"

    def check(self):
        self.__state = "1/1"

    def get_name(self):
        return self.__name

    def setter(self):
        pass



