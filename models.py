import json


class HabitManager():
    def __init__(self):
        self.__habit_list = []
        self.__finished_habits = []

    def save(self):
        pass

    def load(self):
        pass

    def add_habit(self, habit_name, habit_count):
        self.__habit_list.append(Habit(habit_name, habit_count, self))

    def check_in_habit(self, habit_name):
        if habit_name in self.get_habit_list_names():
            for habit in self.__habit_list:
                if habit.get_name() == habit_name:
                    habit.check_in()
                    return True
        else:
            return False

    def finish_habit(self, habit):
        self.__finished_habits.append(habit)
        self.__habit_list.remove(habit)

    def remove_habit(self):
        pass

    def get_habit_list(self):
        return self.__habit_list

    def get_habit_list_names(self):
        names = [habit.get_name() for habit in self.__habit_list]
        return ", ".join(names)

    def get_finished_habits_names(self):
        names = [habit.get_name() for habit in self.__finished_habits]
        return ", ".join(names)

    def print_habits(self):
        names = [" ".join((habit.get_name(), f"{habit.get_count_done()}/{habit.get_count()}")) for habit in self.__habit_list]
        return ", ".join(names)

    def print_finished_habits(self):
        names = [" ".join((habit.get_name(), f"{habit.get_count_done()}/{habit.get_count()}")) for habit in self.__finished_habits]
        return ", ".join(names)


class Habit():
    def __init__(self, name, count, habit_manager):
        self.__habit_manager = habit_manager
        self.__name = name
        self.__count = count
        self.__count_done = 0

    def check_in(self):
        self.__count_done += 1

        if self.__count_done >= self.__count:
            self.finish()

    def get_count_done(self):
        return self.__count_done

    def get_count(self):
        return self.__count

    def finish(self):
        self.__habit_manager.finish_habit(self)

    def get_name(self):
        return self.__name

    def setter(self):
        pass



