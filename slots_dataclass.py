import timeit
from dataclasses import dataclass
from functools import partial


# When set to False, attributes are stored in the __dict__ dunder method
@dataclass(slots=False)
class Person:
    name: str
    address: str
    email: str


# When set to True, it's going to generate a slots variable in which store the attributes
@dataclass(slots=True)
class PersonSlots:
    ame: str
    address: str
    email: str


def get_set_delete(person: Person | PersonSlots):
    person.address = "123 Main St"
    _ = person.address
    del person.address


def main():
    person = Person("John", "123 Main St", "john@doe.com")
    person_slots = PersonSlots("John", "123 Main St", "john@doe.com")
    no_slots = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
    slots = min(timeit.repeat(partial(get_set_delete, person_slots), number=1000000))
    print(f"No slots: {no_slots}")
    print(f"Slots: {slots}")
    print(f"% performance improvement: {(no_slots - slots) / no_slots:.2%}")


if __name__ == "__main__":
    main()