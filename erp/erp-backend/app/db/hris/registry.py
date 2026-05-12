from app.db.hris.models.attendance import Attendance
from app.db.hris.models.audit_logs import AuditLogs
from app.db.hris.models.employee_organizations import EmployeeOrganizations
from app.db.hris.models.employees import Employees
from app.db.hris.models.employees_position import EmployeesPosition
from app.db.hris.models.employees_sensitive import EmployeeSensitive
from app.db.hris.models.employment_models import EmploymentModels
from app.db.hris.models.invitations import Invitations
from app.db.hris.models.leave_balance import LeaveBalance
from app.db.hris.models.leave_requests import LeaveRequests
from app.db.hris.models.leave_types import LeaveTypes
from app.db.hris.models.memberships import Membership
from app.db.hris.models.office_policy import OfficePolicy
from app.db.hris.models.offices import Offices
from app.db.hris.models.organization_groups import OrganizationGroup
from app.db.hris.models.organizations import Organization
from app.db.hris.models.salaries import Salaries
from app.db.hris.models.shifts import Shift
from app.db.hris.models.users import User

HRIS_MODELS = [
    Attendance,
    AuditLogs,
    EmployeeOrganizations,
    EmployeeSensitive,
    Employees,
    EmployeesPosition,
    EmploymentModels,
    Invitations,
    LeaveBalance,
    LeaveRequests,
    LeaveTypes,
    Membership,
    OfficePolicy,
    Offices,
    Organization,
    OrganizationGroup,
    Salaries,
    Shift,
    User,
]
