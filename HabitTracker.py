import HabitLoop
import Habit
class HabitTracker:
    habits = []
    
    def add_habit(self, habit):
        habits.append(habit) 
    
if __name__ == '__main__':
    all_habits = HabitTracker()
    x = input('What would you like to do?\n')
    if x == 'add habit':
        cue = input('What is the cue?\n')
        routine = input('What is the routine?\n')
        reward = input('What is the reward?\n') 
        habit = Habit(cue, routine, reward)        
        all_habits.add_habit(habit)
    elif x == 'view habit':
        pass
    elif x == 'view all habits':
        pass
    else:
        pass
