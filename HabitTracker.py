from os import mkdir
from Habit import Habit
from HabitLoop import HabitLoop

class HabitTracker:
    habits = {}
    
    def add_new_category(self, category, habit):
        self.habits[category] = habit
    def add_habit_to_existing_category(self, category, loop):
        self.habits[category].add_habit_loop(loop)
    def is_empty(self):
        return len(self.habits) == 0
    def categories(self):
        return self.habits.keys()
    def get_category(self, category):
        return self.habits[category].__str__()
    def get_habit_number(self, category):
        if category not in self.habits.keys():
            return 1
        else:
            return self.habits[category].length()
    
if __name__ == '__main__':
    mkdir('Habits')
    all_habits = HabitTracker()
    while(True):
        x = input('What would you like to do?\n')
        if x == 'add habit to a new category':
            category = input('What is the category?\n')
            cue = input('What is the cue?\n')
            routine = input('What is the routine?\n')
            reward = input('What is the reward?\n') 
            loop = HabitLoop(cue, routine, reward, all_habits.get_habit_number(category))        
            habit = Habit()
            habit.add_habit_loop(loop)
            all_habits.add_new_category(category, habit)
        elif x == 'add habit to an old category':
            if all_habits.is_empty():
                print('No old categories')
                continue
            category = input('Which category?\n')
            if category not in all_habits.categories():
                print('This category does not exist')
                continue
            cue = input('What is the cue?\n')
            routine = input('What is the routine?\n')
            reward = input('What is the reward?\n') 
            loop = HabitLoop(cue, routine, reward, all_habits.get_habit_number(category))        
            all_habits.add_habit_to_existing_category(category, loop)
        elif x == 'view category':
            if all_habits.is_empty():
                print('No category to view')
                continue
            category = input('Which category?\n') 
            if category not in all_habits.categories():
                print('This category does not exist')
                continue
            print(all_habits.get_category(category))
        elif x == 'view all habits':
            for category in all_habits.categories():
                print(all_habits.get_category(category))
        elif x == 'exit':
            break
        else:
            pass
