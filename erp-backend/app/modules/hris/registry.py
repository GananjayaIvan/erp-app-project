from app.modules.hris.models.attendance import Attendance
from app.modules.hris.models.employee import Employee
from app.modules.hris.models.employee_salary import Salary
from app.modules.hris.models.employment_auth import EmployeeAuth
from app.modules.hris.models.employment_model import EmploymentModel
from app.modules.hris.models.employment_position import EmployeePosition
from app.modules.hris.models.leave_balance import LeaveBalance
from app.modules.hris.models.leave_request import LeaveRequest
from app.modules.hris.models.leave_type import LeaveType
from app.modules.hris.models.office import Office
from app.modules.hris.models.office_policy import OfficePolicy
from app.modules.hris.models.shift import Shift

HRIS_MODELS = [
    Attendance,
    Employee,
    EmployeeAuth,
    EmployeePosition,
    EmploymentModel,
    LeaveBalance,
    LeaveRequest,
    LeaveType,
    Office,
    OfficePolicy,
    Salary,
    Shift,
]
