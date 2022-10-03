from enum import Enum
from dataclasses import dataclass


class OrgRole(Enum):
    MANAGER = "manager"
    CEO = "ceo"
    ANALYST = "analyst"


@dataclass
class Employee(object):
    age: int
    role: OrgRole


def main() -> None:
    nicholas = Employee(age=27, role=OrgRole.ANALYST)
    juan = Employee(age=35, role=OrgRole.MANAGER)
    print(nicholas)
    print(juan)
    # Next class will not work because role attrs its tide to the defined OrgRole
    louis = Employee(age=35, role="CTO")


if __name__ == "__main__":
    main()
