from datetime import datetime, timedelta

class DSSInBuild():
    def __init__(self, dss, start_date, build_data, build_stages):
        self.dss = dss
        self.start_date = start_date
        self.build_data = build_data
        self.current_build_stage = max(
                                        [x.build_stage.stage \
                                        for x in self.build_data \
                                        if x.build_item.dss_in_build.title == self.dss]
                                    )
        self.build_stage = build_stages
        
        def time_left_in_build():
            
            time_stage_tup = []
            for stage in self.build_stage:
                time_stage_tup.append((stage.stage, stage.exp_comp_time))

            time_remaining = 0
            for x, y in time_stage_tup:
                if self.current_build_stage < x:
                    time_remaining += y*7
            
            self.time_remaining = datetime.now() + timedelta(days=time_remaining)    

        time_left_in_build()
