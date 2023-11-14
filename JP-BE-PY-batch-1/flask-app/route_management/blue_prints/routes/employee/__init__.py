from .add_employee import employee_bp as add_employee_bp
from .list_employee import employee_bp as list_employee_bp
from .profile_employee import employee_bp as profile_employee_bp


router_list = []
router_list.append(add_employee_bp)
router_list.append(list_employee_bp)
router_list.append(profile_employee_bp)