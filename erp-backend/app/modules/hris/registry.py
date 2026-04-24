from app.modules.hris.models.attendance import Attendance
from app.modules.hris.models.employee import Employees
from app.modules.hris.models.employee_organizations import EmployeeOrganization
from app.modules.hris.models.employee_salary import Salary
from app.modules.hris.models.employees_position import EmployeesPosition
from app.modules.hris.models.employment_model import EmploymentModel
from app.modules.hris.models.leave_balance import LeaveBalance
from app.modules.hris.models.leave_request import LeaveRequest
from app.modules.hris.models.leave_type import LeaveType
from app.modules.hris.models.membership import Membership
from app.modules.hris.models.office import Offices
from app.modules.hris.models.office_policy import OfficePolicy
from app.modules.hris.models.organization_group import OrganizationGroup
from app.modules.hris.models.organizations import Organization
from app.modules.hris.models.shift import Shift
from app.modules.hris.models.users import User

HRIS_MODELS = [
    Attendance,
    EmployeeOrganization,
    Employees,
    EmployeesPosition,
    EmploymentModel,
    LeaveBalance,
    LeaveRequest,
    LeaveType,
    Membership,
    OfficePolicy,
    Offices,
    Organization,
    OrganizationGroup,
    Salary,
    Shift,
    User,
]
