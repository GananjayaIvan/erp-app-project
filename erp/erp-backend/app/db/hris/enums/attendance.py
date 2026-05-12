from enum import Enum

class CheckInStatus(str, Enum):
    on_time = "on_time"
    late = "late"
    too_late = "too_late"
    early = "early"

class ShiftTypeEnum(str, Enum):
    fixed = "fixed"
    flexible = "flexible"
    split = "split"
    night = "night"