from typing import Any
from datetime import date
from typing_extensions import TypedDict


class SystemStatusGetResult(TypedDict):
    " "
    cpu_n: int
    "Number of CPUs detected by the virtual appliance."
    uptime_sec: int
    "System uptime in seconds."
    hostname: str
    "NETLAB+ domain name"
    sys_lic_exp_date: date
    "License expiration date"
    sys_lic_op_state: bool
    "License operation state"
    sys_logins_enabled: bool
    "User logins status"
    sys_maint_ends: date
    "Mainenance end date"
    sys_mode: Any
    "System mode"
    sys_name: str
    "System name"
    sys_product_id: str
    "Product identifier"
    sys_sdn_release_date: date
    "Software distribution date"
    sys_sdn_release_type: Any
    "Software distribution release type"
    sys_sdn_version: str
    "Software distribution version"
    sys_serial: str
    "System serial number"
