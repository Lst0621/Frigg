import sys
from datetime import date
from datetime import MINYEAR
from datetime import MAXYEAR
from core.frigg import Frigg


class FriggBuilder(object):
    def __init__(self):
        today = date.today()
        self.year = today.year
        self.month = today.month
        self.lang = 'en_US.utf8'

    def with_year(self, year):
        if type(year) != int:
            raise Exception("Year type must be int")

        if not MINYEAR <= year <= MAXYEAR:
            raise Exception("Year {} not valid".format(year))

        self.year = year
        return self

    def with_month(self, month):
        if type(month) != int:
            raise Exception("Month type must be int")

        if not 1 <= month <= 12:
            raise Exception("Month {} not valid".format(month))

        self.month = month
        return self

    def with_lang(self, lang):
        self.lang = lang
        return self

    def build(self):
        return Frigg(self.year, self.month, self.lang)
