# convert person class to a dataclass
import datetime as dt
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    birthdate: dt.date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = dt.date.today()
        years = today.year - self.birthdate.year
        # python does a lexicographical comparison of the elements in the tuples
        # only checks the days if the months are equal

        had_birthday_this_year = (today.month, today.day) >= (self.birthdate.month, self.birthdate.day)
        age = years if had_birthday_this_year else years - 1
        return age >= 18

        # note: the above is necessary because with my old version, if the original birthday is on feb 29
        # then it would try to create a new date of feb 29 on a non-leap year and crash

imran = Person("Imran", dt.date(2009,8,6), "Ubuntu")
print(imran.is_adult())