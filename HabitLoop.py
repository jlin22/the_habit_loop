class HabitLoop:
    
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
