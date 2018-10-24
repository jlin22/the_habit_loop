from HabitLoop import HabitLoop

class Habit:
    habit_loops = [] 
    
    def add_habit_loop(self, habit_loop):
        self.habit_loops.append(habit_loop)
    def length(self):
        return len(self.habit_loops)
    def __str__(self):
        s = ''
        for loop in self.habit_loops:
            s += loop.__str__()
            s += '\n'
        return s


            
