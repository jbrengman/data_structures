import datetime
import hash_table


class HashMonth(hash_table.HashTable):

    def __init__(self):
        hash_table.HashTable.__init__(self)

    @classmethod
    def make_month(
            cls,
            year=datetime.date.today().year,
            month=datetime.date.today().month):
        month_table = cls()
        d = datetime.date(year, month, 1)
        while (d.month == month):
            month_table.set(str(d.day), d.strftime('%A')[:2])
            d += datetime.timedelta(days=1)
        return month_table

    def day(self, day):
        if type(day) == int:
            day = str(day)
        return self.get(day)
