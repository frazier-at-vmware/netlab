from typing import Any
import json
from datetime import date, datetime, timedelta
from decimal import Decimal
from enum import Enum
from uuid import UUID

from . import enums
from .errors import ResponseFormatError

ENUMS = {
    'cls_email_logs': enums.ClassEmailLogs,
    'cls_lab_limit': enums.ClassLabLimit,
    'acc_type': enums.AccountType,
    'pod_cat': enums.PodCategory,
    'pod_admin_state': enums.PodAdminState,
    'pod_current_state': enums.PodCurrentState,
    'pc_icon': enums.PCIcon,
    'pc_type': enums.PCType,
    'pl_icon': enums.PLIcon,
    'vh_com_path': enums.VirtualHostComPath,
    'vm_role': enums.VirtualMachineRole,
    'res_type': enums.ReservationType,
    'date_format': enums.DateFormat,
    'time_format': enums.TimeFormat,
    'cls_ext_slots_per_res': (enums.ClassExtensionSlots, int),
    'com_ext_slots_per_res': (enums.CommunityExtensionSlots, int),
    'con_access': enums.ContentAccessiblity,
}

ENUM_CSV = {
    'acc_privs': enums.AccountPrivileges,

    # Pod
    'pod_cat_values': enums.PodCategory,
}

STR_CSV = {
    'con_pt_ids',
}

DATE_FIELDS = {
    # Class
    'cls_end_date', 'cls_start_date',

    # System
    'sys_lic_exp_date', 'sys_maint_ends', 'sys_sdn_release_date',

    # Reservation
    'local_ymd',

    # History
    'crs_release_date',
}

DATETIME_FIELDS = {
    # HDR
    'time', 'hdr_time',

    # User
    'acc_last_login', 'acc_session_time_started', 'acc_time_created', 'acc_time_last_access',

    # Pod
    'time', 'vh_bios_date', 'vh_date_modified', 'vh_date_tested', 'vm_date_added', 'vh_date_added',
    'vm_date_added',

    # Reservation
    'res_active_time', 'res_attend_time', 'res_end', 'res_post_time', 'res_preload_time',
    'res_start', 'utc', 'local', 'time_in_local', 'time_in_utc', 'time_out_local', 'time_out_utc',
    'res_end_utc', 'res_start_utc', 'start_time', 'end_time',

    # History
    'lh_active_time', 'lh_attend_time', 'lh_end_time', 'lh_start_time', 'res_active_time', 'res_attend_time',
    'res_end_actual', 'res_end_sched',
    'res_load_time', 'res_post_time', 'res_save_time', 'res_start', 'res_term_time', 'rh_report_time'

    # VM
    'vdc_date_added', 'vdc_date_tested', 'vh_bios_date', 'vh_date_added', 'vh_date_modified', 'vh_date_tested',
    'vm_date_added', 'vhp_time',

    # System
    'sp_time',
}

TIMEDELTA_FIELDS = {
    # Reservation
    'res_remaining_dhms',
}

BOOLEAN_FIELDS = {
    # Class
    'cls_change_ex', 'cls_no_delete', 'cls_retain_ilt', 'cls_retain_st', 'cls_self_sched', 'cls_team_sched', 'lead',
    'con_managed', 'con_global', 'registered', 'auth_all_communities',

    # System
    'sys_logins_enabled',

    # User
    'acc_can_login', 'acc_pw_change', 'acc_sys', 'test_taken', 'com_enabled',
    'enabled', 'logout', 'changed',
    'acc_nlx_terms', 'acc_npd_terms',

    # Pod
    'pod_acl_enabled', 'pod_auto_net_enabled', 'pod_auto_net_host_setup', 'pod_auto_net_host_teardown',
    'pod_managed', 'pt_removable', 'pc_online', 'pc_revert_to_scrub', 'pc_vnc_use_copy_rect',
    'vh_online', 'vh_pra_enabled', 'vm_auto_display', 'vm_auto_network', 'vm_auto_settings', 'vm_sanity_checks',
    'pc_revert_to_scrub', 'pc_vnc_use_copy_rect', 'vh_pra_enabled', 'vm_auto_display', 'vm_auto_network',
    'vm_auto_settings', 'vm_sanity_checks', 'pt_removable', 'pod_managed', 'pod_dyn_vlan'

    # Reservation
    'res_done', 'res_is_active', 'tz_is_dst',

    # History
    'res_done', 'rh_reported'

    # VM
    'notify_progress', 'notify_complete', 'vh_online', 'vh_pra_enabled', 'data_available'

    # Paging
    'out_of_bounds',
}

DECIMAL_FIELDS = {
    # System
    'gnice_pct', 'guest_pct', 'idle_pct', 'iowait_pct', 'irq_pct', 'nice_pct', 'soft_pct',
    'steal_pct', 'sys_pct', 'usr_pct', 'uptime_sec', 'used_pct', 'sp_value',
}

INT_FIELDS = {
    # Class
    'cls_max_slots_per_res', 'cls_min_hours_btw_res', 'cls_retain_period', 'com_id' 'cls_id', 'acc_id',
    'con_trustee',

    # Lab
    'con_build', 'con_fs_id', 'con_trustee', 'ex_index', 'ex_minutes', 'ex_fs_id',

    # Pod
    'acc_id', 'pod_id', 'pod_csw_base_port', 'pod_csw_base_vlan', 'pod_csw_id', 'pod_id', 'pod_id_avail_count',
    'pod_id_base', 'pod_id_range_min', 'pod_id_range_max', 'pod_osm_enabled', 'non_osm_pod_count', 'pod_vlan_pool_size',
    'sys_total_pod_count', 'clone_vh_id', 'pl_index', 'dev_id', 'line', 'pc_id', 'pev_id', 'pod_id', 'res_id',
    'severity', 'device_count', 'pt_apc_port_count', 'pt_as_port_count', 'pt_build', 'pt_csw_port_count', 'pt_pod_max',
    'pt_vlan_pool', 'remote_pc_count', 'pod_res_id', 'pc_pod_id', 'pc_pod_index', 'pc_vnc_port', 'pl_index', 'vdc_id',
    'vh_cpu_cores', 'vh_cpu_mhz', 'vh_cpu_threads', 'vh_cpu_threads', 'vh_id', 'vh_memory_mb', 'vh_pra_max_cpu',
    'vh_pra_max_mem_mb', 'vh_pra_max_vm', 'vhg_id', 'vm_alloc_cpu_n', 'vm_alloc_mem_mb', 'vm_child_count', 'vm_id',
    'vm_parent_id', 'vm_runtime_vh_id', 'pt_apc_port_count', 'pt_as_port_count', 'pt_build', 'pt_csw_port_count',
    'pt_index', 'pt_pod_max', 'pt_vlan_pool', 'remote_pc_count', 'pt_apc_port_count', 'pt_as_port_count',
    'pt_csw_port_count', 'pt_index', 'pt_pod_max', 'pt_vlan_pool', 'remote_pc_count',

    # Reservation
    'acc_com_id', 'acc_id', 'cls_div_id', 'cls_id', 'pod_id', 'res_acc_id', 'res_cls_id', 'res_com_id', 'res_flags',
    'res_id', 'res_init_fail', 'res_minutes', 'res_pod_id', 'res_remaining_sec', 'res_id', 'res_minutes', 'serial',
    'slot_minutes', 'acc_com_id', 'cls_div_id', 'cls_id', 'pod_id', 'res_acc_id', 'res_cls_id', 'res_com_id',
    'res_flags', 'res_init_fail', 'res_minutes', 'res_pod_id', 'active_reservations', 'completed_reservations',
    'future_reservations', 'pods_in_use', 'total_reservations', 'days', 'hours', 'minutes', 'months', 'local_day',
    'local_day_of_week', 'local_hour_12', 'local_hour_24', 'local_minute', 'local_second', 'local_year', 'tz_id',
    'tz_id_in', 'tz_id_out',

    # History
    'acc_id', 'cli_bytes_in', 'cli_bytes_out', 'cli_connects', 'cli_seconds', 'cls_id', 'com_id', 'lh_attend_min',
    'lh_n_users', 'vnc_bytes_in', 'vnc_bytes_out', 'vnc_connects', 'vnc_seconds', 'pod_id', 'res_extensions', 'res_id',
    'rh_attend_min', 'rh_init_fail_total', 'rh_n_lab_devices', 'rh_n_users', 'rh_n_vcpu', 'rh_n_vm', 'rh_n_vm_hosts',
    'rh_resume_total', 'rh_suspend_total'

    # System
    'cpu_n', 'free_b', 'avail_b', 'total_b', 'used_b',

    # User
    'acc_id', 'acc_fs_id', 'acc_logins', 'com_id', 'tz_id', 'com_alt_banner_height', 'com_alt_banner_width',
    'com_max_slots_per_res', 'com_min_hours_btw_res', 'active', 'logouts', 'acc_fs_id', 'acc_maint_notify',
    'acc_session_tx_number', 'acc_sys', 'acc_session_tx_number', 'accman_list_com_id', 'first_weekday',

    # VM
    'progress', 'vdc_id', 'vh_id', 'vh_cpu_cores', 'vh_cpu_count', 'vh_cpu_mhz', 'vh_cpu_threads', 'vh_memory_mb',
    'vh_pra_max_cpu', 'vh_pra_max_mem_mb', 'vh_pra_max_vm', 'vm_id', 'pc_id', 'pc_pod_id', 'pc_vm_id', 'vdc_id',
    'vh_id', 'vhg_id', 'vm_alloc_cpu_n', 'vm_alloc_mem_mb', 'vm_child_count', 'vm_parent_id', 'age_sec',

    # Paging
    'page_length', 'total_records', 'total_pages', 'page_limit', 'current_page', 'page_offset', 'page_total',
}

UUID_FIELDS = {
    # History
    'acc_uuid', 'cls_uuid', 'com_uuid', 'crs_uuid', 'lh_uuid', 'rh_uuid', 'lh_uuid_current', 'pod_uuid', 'res_uuid',
    'rh_uuid'
}

BLANK_IS_NONE_FIELDS = {
    # class
    'ros_team',
}


def deserialize(data):
    return json.loads(data, object_hook=process)


def resolve_enum(enum, value):
    if not isinstance(enum, tuple):
        enum = (enum,)
    for e in enum:
        try:
            return e(value)
        except:  # noqa
            pass
    raise ResponseFormatError("The value {} could not resolve to one of '{}'.".format(
        value, enum))


def process(obj):
    for field, value in obj.items():
        if field in DATE_FIELDS:
            obj[field] = to_date(value)
        if field in DATETIME_FIELDS:
            obj[field] = to_datetime(value)
        if field in TIMEDELTA_FIELDS:
            obj[field] = to_timedelta(value)
        if field in BOOLEAN_FIELDS:
            obj[field] = to_bool(value)
        if field in DECIMAL_FIELDS:
            obj[field] = to_decimal(value)
        if field in INT_FIELDS:
            obj[field] = to_int(value)
        if field in UUID_FIELDS:
            obj[field] = to_uuid(value)
        if field in ENUMS and value is not None:
            obj[field] = resolve_enum(ENUMS[field], value)
        if field in ENUM_CSV and value is not None:
            enum = ENUM_CSV[field]
            obj[field] = list(map(lambda v: enum[v], value.split(',')))
        if field in STR_CSV:
            obj[field] = value.split(',')
        if field in BLANK_IS_NONE_FIELDS and value == '':
            obj[field] = None
    return obj


def to_date(value):
    if value:
        return datetime.strptime(value, '%Y-%m-%d').date()
    else:
        return None


def to_datetime(value):
    if value:
        try:
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            # rarely timestamps include microseconds. catch and process those
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
    else:
        return None


def to_timedelta(value):
    if value:
        days, hours, minutes, seconds = [int(i) for i in value.split(',')]
        return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    else:
        return None


def to_bool(value):
    truth_values = ('1', 'true', 'yes')
    normalized_value = str(value).lower()
    return normalized_value in truth_values


def to_decimal(value):
    if value:
        return Decimal(value)
    else:
        return None


def to_int(value):
    if value:
        return int(value)
    else:
        return 0


def to_uuid(value):
    if value:
        return UUID(value)
    else:
        return None


def serialize(data, pretty=False):
    extra_args: Any = {}
    if pretty:
        extra_args['indent'] = 2
        extra_args['sort_keys'] = True
    return json.dumps(data, default=default, **extra_args)


def default(obj):
    if isinstance(obj, Enum):
        return obj.value
    if isinstance(obj, datetime):
        return from_datetime(obj)
    if isinstance(obj, date):
        return from_date(obj)
    if isinstance(obj, timedelta):
        return from_timedelta(obj)
    if isinstance(obj, UUID):
        return from_uuid(obj)
    if isinstance(obj, Decimal):
        return from_decimal(obj)
    return obj


def from_date(value):
    return value.strftime("%Y-%m-%d")


def from_datetime(value):
    return value.strftime("%Y-%m-%d %H:%M:%S")


def from_timedelta(value):
    days, secs = value.days, value.seconds
    hours = secs // 3600
    minutes = (secs % 3600) // 60
    seconds = secs % 60
    return ','.join([str(days), str(hours), str(minutes), str(seconds)])


def from_uuid(value):
    return str(value)


def from_decimal(value):
    return str(value)
