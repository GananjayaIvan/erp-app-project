from app.modules.hris.models.attendance import Attendance
from app.modules.hris.models.audit_logs import AuditLogs
from app.modules.hris.models.employee_organizations import EmployeeOrganizations
from app.modules.hris.models.employees import Employees
from app.modules.hris.models.employees_position import EmployeesPosition
from app.modules.hris.models.employees_sensitive import EmployeeSensitive
from app.modules.hris.models.employment_models import EmploymentModels
from app.modules.hris.models.leave_balance import LeaveBalance
from app.modules.hris.models.leave_requests import LeaveRequests
from app.modules.hris.models.leave_types import LeaveTypes
from app.modules.hris.models.membership import Memberships
from app.modules.hris.models.office_policy import OfficePolicy
from app.modules.hris.models.offices import Offices
from app.modules.hris.models.organization_groups import OrganizationGroup
from app.modules.hris.models.organizations import Organization
from app.modules.hris.models.salaries import Salaries
from app.modules.hris.models.shifts import Shift
from app.modules.hris.models.users import User

HRIS_MODELS = [
    Attendance,
    AuditLogs,
    EmployeeOrganizations,
    EmployeeSensitive,
    Employees,
    EmployeesPosition,
    EmploymentModels,
    LeaveBalance,
    LeaveRequests,
    LeaveTypes,
    Memberships,
    OfficePolicy,
    Offices,
    Organization,
    OrganizationGroup,
    Salaries,
    Shift,
    User,
]
