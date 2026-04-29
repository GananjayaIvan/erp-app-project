# BUSINESS LOGIC

def calculate_worked_time(self):
    """
    Calculate worked minutes (call in service layer ideally)
    """
    if self.checkin and self.checkout:
        delta = self.checkout - self.checkin
        self.worked_minutes = int(delta.total_seconds() / 60)
    else:
        self.worked_minutes = None