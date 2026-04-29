from enum import Enum

class MaritalStatus(str,Enum):
    single = "single"
    married = "married"
    separated = "separated"

class EmploymentStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    terminated = "terminated"
    suspended = "suspended"


class EmploymentType(str, Enum):
    permanent = "permanent"
    contract = "contract"
    intern = "intern"