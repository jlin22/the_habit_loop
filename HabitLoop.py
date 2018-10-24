import datetime as dt
import time as tm

class HabitLoop:
    date = dt.datetime.fromtimestamp(tm.time()) 

    def __init__(self, cue, routine, reward, number):
        self.cue = cue
        self.routine = routine
        self.reward = routine
        self.number = number
    def set_cue(self, cue):
        self.cue = cue
    def set_routine(self, routine):
        self.routine = routine
    def set_reward(self, reward):
        self.reward = reward
    def set_date(self, date):
        self.date = date
    def set_number(self, number):
        self.number = number
    def __str__(self):
        return 'Loop {} on {}\nCue: {}\nRoutine: {}\nReward: {}'.format(
            self.number, self.date, self.cue, self.routine, self.reward)
