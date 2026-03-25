class Logging :
    def __init__(self,log , message, module, timespent) :
        self.log = log
        self.message = message
        self.module = module
        self.timespent = timespent


    def to_tuple(self):
        return self.log, self.message, self.module, self.timespent

    @classmethod
    def from_list_to_tuple(cls, logs) :
        return [log.to_tuple() for log in logs]

    @classmethod
    def total_time(cls,logs):
        total = 0

        if not logs :
            return total, 0

        for log in logs :
            total += log.timespent

        hours = total / 60

        return total , hours

    @classmethod
    def total_per_module(cls,logs):
        time_module = {}

        if not logs:
            return time_module

        for log in logs :
            if log.module not in time_module :
                time_module[log.module] = {"total" :log.timespent, "sessions" : 1}
            else:
                time_module[log.module]["total"] += log.timespent
                time_module[log.module]["sessions"] += 1

        return time_module
