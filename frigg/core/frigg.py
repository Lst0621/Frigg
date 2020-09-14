from datetime import datetime
import calendar
import locale

from core.frigg_line import FriggLine
from core.const import DaysPerWeek


class Frigg(object):
    def __init__(self, year, month, lang):
        locale.setlocale(locale.LC_ALL, lang)
        self.year = year
        self.month = month
        first_day = datetime(year, month, 1)
        first_week_day = first_day.weekday()
        week_day_idx = [(first_week_day + shift) % DaysPerWeek for shift in range(DaysPerWeek)]
        self.week_days = [calendar.day_name[idx] for idx in week_day_idx]
        last_day = calendar.monthrange(year, month)[1]
        self.frigg_lines = FriggLine.gen_frigg_lines(last_day)

    def to_console(self):
        print("{} {}".format(calendar.month_name[self.month], self.year))

        for week_day, frigg_line in zip(self.week_days, self.frigg_lines):
            print(week_day)
            print(frigg_line)
