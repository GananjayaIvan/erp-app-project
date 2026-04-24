from enum import Enum


class EmploymentStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    terminated = "terminated"
    suspended = "suspended"


class EmploymentType(str, Enum):
    permanent = "permanent"
    contract = "contract"
    intern = "intern"