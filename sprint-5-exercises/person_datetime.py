# modify to use datetime.date to take in a date of birth
# store in a field instead of age
import datetime as dt

class Person:
    def __init__(self, name: str, birthdate: dt.date, preferred_operating_system: str):
        self.name = name
        self.birthdate = birthdate
        self.preferred_operating_system = preferred_operating_system
        self.birthdate = birthdate

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


        return today >= dt.date(self.birthdate.year +18, self.birthdate.month, self.birthdate.day)

imran = Person("Imran", dt.date(2008,8,6), "Ubuntu")
print(imran.is_adult())