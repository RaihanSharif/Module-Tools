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
        print(today)
        return today >= dt.date(self.birthdate.year +18, self.birthdate.month, self.birthdate.day)

imran = Person("Imran", dt.date(2008,8,6), "Ubuntu")
print(imran.is_adult())