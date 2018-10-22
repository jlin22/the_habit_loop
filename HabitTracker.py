from Habit import Habit
from HabitLoop import HabitLoop

class HabitTracker:
    habits = []
    
    def add_habit(self, habit):
        self.habits.append(habit) 
    def __str__(self):
        return '0'
    
if __name__ == '__main__':
    all_habits = HabitTracker()
    #x = input('What would you like to do?\n')
    x = 'add habit to a new category'
    if x == 'add habit to a new category':
        cue = input('What is the cue?\n')
        routine = input('What is the routine?\n')
        reward = input('What is the reward?\n') 
        loop = HabitLoop(cue, routine, reward, 1)        
        habit = Habit()
        habit.add_habit_loop(loop) 
        all_habits.add_habit(habit)
        print(all_habits)
    elif x == 'add habit to an old category':
        pass
    elif x == 'view habit':
        pass
    elif x == 'view all habits':
        pass
    else:
        pass
