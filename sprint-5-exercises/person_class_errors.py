class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.address)

# Understand the errors from running mypy on this code

# Person_class_errors.py:9: error: "Person" has no attribute "address"  [attr-defined]
# Because there is type definiton in the constructor of the Person class, mypy checks whether
# the imran object has an address attribute, and finds that it does not.

# Person_class_errors.py:13: error: "Person" has no attribute "address"  [attr-defined]
# Same with eliza. It is a Person type object, without an address property, code attempts to
# print in line 13.