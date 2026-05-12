def is_active(self) -> bool:
    return self.status == EmploymentStatus.active

def is_terminated(self) -> bool:
    return self.status == EmploymentStatus.terminated

def is_inactive(self) -> bool:
    return self.status == EmploymentStatus.inactive

def is_suspended(self) -> bool:
    return self.status == EmploymentStatus.suspended