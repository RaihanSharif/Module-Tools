
# parent class has two string fields, first_name, last_name
# a method that return a string which joins the two names with a space
class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


# extends parent class
# add ability to change last name, store previous last names in a list
# a method that prints first and last name as well as the original last name of Child
class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names = []

    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"


person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name()) # inherit from Parent class, output = "Elizaveta Alekseeva"
print(person1.get_full_name()) # method of Child class, output = "Elizaveta Alekseeva" no previous surname
person1.change_last_name("Tyurina") # changes last name of person1, adds "Alekseeva" to previous names list
print(person1.get_name()) # last name has changed, output = "Elizaveta Tyurina"
print(person1.get_full_name()) # includes maiden name, output = "Elizaveta Tyurina (née Alekseeva)"

person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name()) # output = "Elizaveta Alekseeva"
print(person2.get_full_name()) # AttrbuteError - the Parent class does not have get_full_name() method
person2.change_last_name("Tyurina") # same again
print(person2.get_name()) # no problems, same as line 40
print(person2.get_full_name()) # again, no get_full_name() method in this Parent class. Same as line 41