from core.const import DaysPerWeek


class FriggLine(object):

    def __init__(self, start_date, end_date):
        if (end_date - start_date) % DaysPerWeek != 0:
            raise Exception(
                "Invalid week day collection. Start: {} End: {}".format(
                    start_date, end_date))

        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        days = range(self.start_date, self.end_date + DaysPerWeek, DaysPerWeek)
        return '-'.join(str(day).ljust(2, '-') for day in days)

    @staticmethod
    def gen_frigg_lines(days_in_month):
        frigg_lines = []
        for week_day in range(DaysPerWeek):
            start_date = week_day + 1
            end_date = start_date + ((days_in_month - start_date) // DaysPerWeek) * DaysPerWeek
            frigg_lines.append(FriggLine(start_date, end_date))
        return frigg_lines
