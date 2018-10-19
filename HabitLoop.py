import datetime as dt
import time as tm

class HabitLoop:
    date = dt.datetime.fromtimestamp(tm.time()) 

    def __init__(self, cue, routine, reward):
        self.cue = cue
        self.routine = routine
        self.reward = routine
    def set_cue(self, cue):
        self.cue = cue
    def set_routine(self, routine):
        self.routine = routine
    def set_reward(self, reward):
        self.reward = reward
    def set_date(self, date):
        self.date = date
    def __str__(self):
        return 'HabitLoop on {}\nCue: {}\nRoutine: {}\nReward: {}'.format(
            self.date, self.cue, self.routine, self.reward)

