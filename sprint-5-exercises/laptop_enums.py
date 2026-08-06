from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


# people = [
#     Person(name="Imran", age=22, preferred_operating_system=OperatingSystem.UBUNTU),
#     Person(name="Eliza", age=34, preferred_operating_system=OperatingSystem.ARCH),
# ]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]


# take input to create a new Person, validate the input to ensure the person data can be used to create a valid person

# loops forever until alphabetic string provided
def person_name_input() -> str:
    name = input("Enter your first name: ")
    while True:
        if (name.isalpha()):
            return name
        name = input("invalid first name, please enter only letters: ")

# loops forever until numeric input is provided
def person_age_input() -> int:
    age = input("Enter your age: ")
    while True:
        if (age.isnumeric()):
            return int(age)
        age = input("Invalid age, please enter only integer value: ")

# loops forever until a valid OS is chosen
def preferred_os_input() -> OperatingSystem:
    os_options = [member.name for member in OperatingSystem]
    os_choice = input(f"Enter your preferred laptop from {os_options}: ").strip().upper()

    while True:
        if (os_choice in os_options):
            return OperatingSystem[os_choice]
        os_choice = input(f"Invalid choice, check spelling and spaces. choices:  {os_options}: ").strip().upper()



        
# run a while loop to act as an interactive menu, in which user input is taken step by step
print(f"Welcome to the CYF library. There are {len(laptops)} laptops available!")
print("Enter your details to begin")
while True:
    name = person_name_input()
    age = person_age_input()
    prefered_os = preferred_os_input()

    person: Person = Person(name, age, prefered_os)
    print(person)
    break