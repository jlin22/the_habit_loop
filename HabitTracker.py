class HabitTracker:
    habits = []
    
    def add_habit(self, habit):
        habits.append(habit) 
    
if __name__ == '__main__':
    all_habits = HabitTracker()
    x = input('What would you like to do?\n')
    if x == 'add habit':
        pass
    elif x == 'view habit':
        pass
    elif x == 'view all habits':
        pass
    else:
        x = input("That's not a valid input. What would you like to do?\n") 
