from datetime import date, datetime

class DSSInBuild():
    def time_left_in_build(self, start_date, build_stage):
        pass
    
    def __init__(self, dss, start_date, build_stage):
        self.dss = dss
        self.start_date = start_date
        self.build_stage = build_stage