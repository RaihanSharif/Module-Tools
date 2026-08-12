from dataclasses import dataclass
from enum import Enum
from typing import List
from collections import Counter

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


laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]


# take input (name, age, preferred os), create Person object
# show them how many laptops with their chosen OS are available
# if there is a different os with more laptops, tell user they are more likely to get a laptop
# if they choose that os

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


print(f"Welcome to the CYF library. Enter your details to begin")

name = person_name_input()
age = person_age_input()
prefered_os = preferred_os_input()

person: Person = Person(name, age, prefered_os)

possible_laptops = find_possible_laptops(laptops, person)

print(f"There are {len(possible_laptops)} laptops with your preferred OS.")

# keep only non-preferred OS, and then see if there there is an OS with more laptops available
non_preferred_os = filter(lambda x: x.operating_system != person.preferred_operating_system, laptops)

counter = Counter(laptop.operating_system for laptop in non_preferred_os)
most_common_os, count = counter.most_common(1)[0]

if (count > len(possible_laptops)):
    print(f"there are {count} latops with {most_common_os.name} operating system. You are more likely to get a laptop if you choose {most_common_os.name} ")