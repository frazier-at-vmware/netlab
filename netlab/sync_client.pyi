
# GENERATED

from typing import Union, Optional, Dict, Any, List, Generator
from typing_extensions import Literal
import netlab.enums
import netlab.datatypes.pod
import netlab.api.system_results
import netlab.config
import datetime
import uuid

NoneType = type(None)

class SyncClient(object):




    def alive(self) -> bool:
        ...

    def call(self, method: str, **kwargs: Any) -> Any:
        r"""

        :param method: The NETLAB+ method name.
        :param kwargs: The arguments to pass to netlab.

        .. warning::

            In most cases, it is better to use the higher level methods, rather than this
            low level method.
        """

    def class_add(self, *, cls_name: str, com_id: int, cls_change_ex: bool = True, cls_def_pw_account: Optional[str] = None, cls_def_pw_console: Optional[str] = None, cls_def_pw_enable: Optional[str] = None, cls_email_logs: netlab.enums.klass.ClassEmailLogs = netlab.enums.ClassEmailLogs.NO, cls_end_date: Optional[datetime.date] = None, cls_lab_limit: netlab.enums.klass.ClassLabLimit = netlab.enums.ClassLabLimit.ENFORCE, cls_max_slots_per_res: Optional[int] = None, cls_min_hours_btw_res: Optional[int] = None, cls_no_delete: bool = False, cls_retain_ilt: bool = False, cls_retain_period: Optional[datetime.date] = None, cls_retain_st: bool = True, cls_self_sched: bool = True, cls_start_date: Optional[datetime.date] = None, cls_team_sched: bool = False, **kwargs) -> int:
        r"""
        This method allows you to add a class to the NETLAB+ system.

        :param cls_name: Class name.
        :param com_id: Community ID.

        :param cls_change_ex: Allow student to change exercise.
        :param cls_def_pw_account: Class default account password.
        :param cls_def_pw_console: Class default console password.
        :param cls_def_pw_enable: Class default enable password.
        :param cls_email_logs: Email reservation logs for real equipment pods.
        :param cls_end_date: Class end date.
        :param cls_lab_limit: Class lab time limit.
        :param cls_max_slots_per_res: Maximum number of slots per reservation.
        :param cls_min_hours_btw_res: Minimum hours between reservations.
        :param cls_no_delete: Prevent from deletion.
        :param cls_retain_ilt: Retain instructor led logs.
        :param cls_retain_period: The number of days to retain logs for.
        :param cls_retain_st: Retain student logs.
        :param cls_self_sched: Allow students to self schedule.
        :param cls_start_date: Class start date.
        :param cls_team_sched: Allow teams to schedule.

        :return: On success, returns the **cls_id** of the newly created class.
        """

    def class_content_add(self, *, cls_id: int, con_id: str, **kwargs) -> None:
        r"""
        This method allows you to add content to a class.

        :param cls_id: Class identifier.
        :param con_id: Content identifier.
        """

    def class_content_availability(self, *, cls_id: int, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method provides a list of available class content.

        :param cls_id: Unnique class identifier.

        :return: On success, returns a list of objects with the requested properties:

        **Properties**

        con_access
            Content is Globally accessible or Private.
        con_aid
            Content author ID.
        con_author
            Content author name.
        con_build
            Build number.
        con_copyright
            Content copyright.
        con_desc
            Content description.
        con_gid
            Unique content identifier.
        con_global
            Is content globally accessible or not.
        con_id
            Unique content identifier.
        con_managed
            Is the content managed or not.
        con_name
            Name of content.
        con_notes
            Content notes.
        con_org
            Content organization.
        con_origin
            Source of the content.
        con_pt_ids
            Comma separated list of required Pod Types.
        con_url
            Content URL.
        """

    def class_content_list(self, *, cls_id: int, properties: Union[Literal['all'], List[str]] = 'all', **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method provides a list of content associated with a class.

        :param cls_id: Unique class identifier.
        :param properties: Array of properties to retrieve.

        :return: On success, returns a list of objects with the requested properties:

        **Properties**

        con_access
            Content is Globally accessible or Private.
        con_aid
            Content author ID.
        con_author
            Content author name.
        con_build
            Build number.
        con_copyright
            Content copyright.
        con_desc
            Content description.
        con_gid
            Unique content identifier.
        con_global
            Is content globally accessible or not.
        con_id
            Unique content identifier.
        con_managed
            Is the content managed or not.
        con_name
            Name of content.
        con_notes
            Content notes.
        con_org
            Content organization.
        con_origin
            Source of the content.
        con_pt_ids
            Comma separated list of required Pod Types.
        con_url
            Content URL.
        """

    def class_content_remove(self, *, cls_id: int, con_id: str, **kwargs) -> None:
        r"""
        This method removes content from a class.

        :param cls_id: Class identifier.
        :param con_id: Content identifier.
        """

    def class_get(self, *, cls_id: int, properties: Union[List[str], Literal['default', 'all']] = 'default', **kwargs) -> Dict[str, Any]:
        r"""
        This method allows you to retrieve a single class and properties.

        :param int cls_id: Class ID.
        :param properties: List of properties to retrieve. Defaults to "all".
        :return: On success, returns an object with the requested properties:

        **Properties**

        cls_change_ex
            Allow student to change exercise.
        cls_def_pw_account
            Class default account password.
        cls_def_pw_console
            Class default console password.
        cls_def_pw_enable
            Class default enable password.
        cls_email_logs
            Email reservation logs for real equipment pods. :py:class:`netlab.enums.ClassEmailLogs`
        cls_end_date
            Class end date.
        cls_id
            Unique class identifier.
        cls_lab_limit
            Lab limit settings. :py:class:`netlab.enums.ClassLabLimit`
        cls_max_slots_per_res
            Maximum number of slots per reservation.
        cls_min_hours_btw_res
            Minimum number of hours between reservations.
        cls_name
            Unique class name per community.
        cls_no_delete
            Prevent from deletion.
        cls_retain_ilt
            Retain instructor led logs.
        cls_retain_period
            Number of days to retain class logs.
        cls_retain_st
            Retain student logs.
        cls_self_sched
            Allow students to self schedule.
        cls_start_date
            Class start date.
        cls_team_sched
            Allow teams to schedule.
        cls_uuid
            Class UUID.
        com_id
            Unique community identifier.
        enrollment
            Count of those enrolled.
        leads
            List of leads and properties sorted by acc_sort_name.
        """

    def class_list(self, *, com_id: Optional[int] = None, member: bool = False, properties: Union[List[str], Literal['default', 'all']] = 'default', **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method allows you to retrieve a list of classes and their properties.

        :param com_id: Community ID.
        :param member: If true, get list of classes the caller is in.
        :param properties: List of properties to retrieve. See Properties section for list of available properties.

        :return: On success, returns an object with the requested properties:

        **Properties**

        cls_change_ex
            Allow student to change exercise.
        cls_def_pw_account
            Class default account password.
        cls_def_pw_console
            Class default console password.
        cls_def_pw_enable
            Class default enable password.
        cls_email_logs
            Email reservation logs for real equipment pods. :py:class:`netlab.enums.ClassEmailLogs`
        cls_end_date
            Class end date.
        cls_id
            Unique class identifier.
        cls_lab_limit
            Lab limit settings. :py:class:`netlab.enums.ClassLabLimit`
        cls_max_slots_per_res
            Maximum number of slots per reservation.
        cls_min_hours_btw_res
            Minimum number of hours between reservations.
        cls_name
            Unique class name per community.
        cls_no_delete
            Prevent from deletion.
        cls_retain_ilt
            Retain instructor led logs.
        cls_retain_period
            Number of days to retain class logs.
        cls_retain_st
            Retain student logs.
        cls_self_sched
            Allow students to self schedule.
        cls_start_date
            Class start date.
        cls_team_sched
            Allow teams to schedule.
        cls_uuid
            Class UUID.
        com_id
            Unique community identifier.
        enrollment
            Count of those enrolled.
        leads
            List of leads and properties sorted by acc_sort_name.
        """

    def class_remove(self, *, cls_id: int, delete_students: bool = False, **kwargs) -> None:
        r"""
        This method removes a class from the NETLAB+ system.

        :param cls_id: Local system class.
        :param delete_students: `False` Do not delete student accounts. `True` Delete student accounts
            that are exclusively in this class. Student accounts that are members of multiple classes are not deleted.
        """

    def class_roster_add(self, *, acc_id: str, cls_id: str, lead: bool = False, ros_team: Optional[str] = None, **kwargs) -> Literal['OK']:
        r"""
        This method allows you to add a member to a class roster.

        :param acc_id: Unique account identifier.
        :param cls_id: Unique class identifier.
        :param lead: Add as lead.
        :param ros_team: Assign user to a team. Single character, A-Z.
        """

    def class_roster_get(self, *, cls_id: int, acc_id: Optional[int], **kwargs) -> Dict[str, Any]:
        r"""
        This method returns class roster information for a single user.

        :param cls_id: Local system class identifier.
        :param acc_id: Returns roster information for the user specified by acount ID acc_id.
            If acc_id is not provided, roster information related to the requester is returned.
        :return: On success, returns an object with the requested properties:

        **Properties**

        acc_display_name
            Account name people will see this name in discussions, messages and comments.
        acc_email
            Account email.
        acc_id
            Local system account identifier.
        acc_full_name
            Account full name.
        acc_last_login
            Timestamp of last account login.
        acc_logins
            Number of times a user has logged in.
        acc_sort_name
            Account name as it appears in sorted lists.
        acc_time_last_access
            Timestamp of last access.
        acc_type
            Account type.
        acc_user_id
            Account user identifier.
        cls_id
            Unique class identifier.
        lead
            User is a lead instructor.
        ros_team
            Team identifier [A-Z] or `None` if user is not assigned to a team.
        """

    def class_roster_list(self, *, cls_id: int, leads: bool = False, **kwargs):
        r"""
        This method lists users in the class roster.

        :param cls_id: Local system class.
        :param leads: `None` Return all users in the roster (leads and learners).
            `True` Return lead instructors only. `False` Return learners only.

        :return: On success, returns an object with the requested properties:

        **Properties**

        acc_display_name
            Account name people will see this name in discussions, messages and comments.
        acc_email
            Account email.
        acc_id
            Local system account identifier.
        acc_full_name
            Account full name.
        acc_last_login
            Timestamp of last account login. Possibly `None`.
        acc_logins
            Number of times a user has logged in.
        acc_sort_name
            Account name as it appears in sorted lists.
        acc_time_last_access
            Timestamp of last access. Possibly `None`.
        acc_type
            Account type. :py:class:`netlab.enums.AccountType`
        acc_user_id
            Account user identifier.
        cls_id
            Unique class identifier.
        lead
            If user is a lead instructor.
        ros_team
            Assignment of user to a team (designated by team letter). `None` if user is not assigned to a team.
        """

    def class_roster_remove(self, *, acc_id: int, cls_id: str, **kwargs) -> None:
        r"""
        This method removes a user from the class roster.

        :param acc_id: Account identifier of user to be removed.
        :param cls_id: Unique class identifier.
        """

    def class_roster_team_update(self, *, cls_id: int, ros_team: Optional[str] = None, roster_acc_id: List[int], **kwargs) -> str:
        r"""
        This method will create and update teams (groups of students) for a given class roster.

        :param cls_id: Local system class identifier.
        :param ros_team: A single uppercase letter [A,Z] as the designation of the team to add
            the student(s) to. If this value is `None`, the student(s) are assigned to no team
            (unassigned).
        :param roster_acc_id: A list of account IDs to assign to the specified team.
        """

    def class_update(self, *, cls_id: int, cls_change_ex: Optional[bool] = None, cls_def_pw_account: Optional[str] = None, cls_def_pw_console: Optional[str] = None, cls_def_pw_enable: Optional[str] = None, cls_email_logs: Optional[netlab.enums.klass.ClassEmailLogs] = None, cls_end_date: Optional[datetime.date] = None, cls_lab_limit: Optional[netlab.enums.klass.ClassLabLimit] = None, cls_max_slots_per_res: Optional[int] = None, cls_min_hours_btw_res: Optional[int] = None, cls_name: Optional[str] = None, cls_no_delete: Optional[bool] = None, cls_retain_ilt: Optional[bool] = None, cls_retain_period: Optional[int] = None, cls_retain_st: Optional[bool] = None, cls_self_sched: Optional[bool] = None, cls_start_date: Optional[datetime.date] = None, cls_team_sched: Optional[bool] = None, cls_ext_slots_per_res: Union[int, netlab.enums.klass.ClassExtensionSlots, NoneType] = None, **kwargs) -> Literal['OK']:
        r"""
        This method allows you to update a class and its properties.

        :param cls_id: Unique class identifier.
        :param cls_change_ex: Allow student to change exercise.
        :param cls_def_pw_account: Class default account password.
        :param cls_def_pw_console: Class default console password.
        :param cls_def_pw_enable: Class default enable password.
        :param cls_email_logs: Email reservation logs for real equipment pods.
        :param cls_end_date: Class end date.
        :param cls_lab_limit: Class lab time limit.
        :param cls_max_slots_per_res: Maximum number of slots per reservation.
        :param cls_min_hours_btw_res: Minimum hours between reservations.
        :param cls_name: Class name.
        :param cls_no_delete: Prevent from deletion.
        :param cls_retain_ilt: Retain instructor led logs.
        :param cls_retain_period: The number of days to retain logs for.
        :param cls_retain_st: Retain student logs.
        :param cls_self_sched: Allow students to self schedule.
        :param cls_start_date: Class start date.
        :param cls_team_sched: Allow teams to schedule.
        :param cls_ext_slots_per_res: Allow extensions to reservations for students and teams.
            Instructors are not restricted to this limit.
        """

    def history_reservation_get(self, *, res_id, **kwargs) -> Dict[str, Any]:
        ...

    def lab_exercise_list(self, *, properties: Optional[List[str]] = None, sort_property: Literal['ex_id', 'ex_index', 'ex_name', 'ex_con_id'] = 'ex_id', con_id: Optional[str] = None, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method allows you to retrieve a list of lab exercises installed on the system.

        :param con_id: If specified, only return exercises within for the lab designed with identifier of con_id.
        :param sort_property: Property to sort results by.
        :param properties: List of properties to retrieve. See Properties section for list of available properties.

        :return: On success, returns an object with the requested properties:

        **Properties**

        ex_id
            Lab exercise identifier.
        ex_con_id
            Lab design identifier.
        ex_index
            Exercise index number in lab design.
        ex_name
            Exercise name.
        ex_content_url
            Lab document relative URL.
        ex_minutes
            Exercise minimum time in minutes.
        ex_topology_image
            Lab topology image relative URL.
        ex_im_id
            Internal image map identifier for clickable hotspots.
        ex_vlan_map
            Alternate VLAN map for real equipment pods, overrides pod design.
        ex_pt_id
            Exercise pod type identifier.
        ex_tabs
            Exercise tabs enabled.
        ex_actions
            Exercise actions enabled.
        ex_fs_id
            Root node of folder containing configuration files for this exercise.
        ex_content_no_preview
            If true, user cannot preview this exercise.
        ex_ilt_no_select
            If true, exercise is disabled in ILT.
        cls_ids
            Array of class identifiers using this content.
        hotspots
            Array of image_map objects (for clickable hotspots).
        """

    def pod_acl_add(self, *, com_id: int, pod_id: int, acc_id: Optional[int] = None, cls_id: Optional[int] = None, team: Optional[str] = None, **kwargs) -> uuid.UUID:
        r"""
        This method allows you to add access controls to a pod on the NETLAB+ system.

        :param com_id: Community identifier.
        :param pod_id: Pod identifier.
        :param acc_id: Account identifier.
        :param cls_id: Class identifier.
        :param team: Team assignment.
        :return: Pod access control list UUID.
        """

    def pod_acl_admin_add(self, *, acc_id: int, pod_id: int, **kwargs) -> None:
        r"""
        This method allows you add additional pod access control administrators.

        :param int acc_id: Account identifier.
        :param int pod_id: Pod identifier.
        """

    def pod_acl_admin_auth(self, *, acc_id: int, pod_id: int, **kwargs) -> bool:
        r"""
        This method returns true if a specified instructor account is authorized to manage POD
        ACLs on a specified pod.

        :param acc_id: Account identifier.
        :param pod_id: Pod identifier.

        :return: acc_id is authorized for pod_id.
        """

    def pod_acl_admin_list(self, *, pod_id: int, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method allows you to retrieve a list of pod access controls per pod.

        :param pod_id: Pod identifier.
        :return: Pod access control list.
        """

    def pod_acl_admin_pods(self, *, acc_id: int, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method allows you to retrieve a list of pods a user has access to.

        :param int acc_id: Account identifier.
        """

    def pod_acl_admin_remove(self, *, acc_id: int, pod_id: int, **kwargs) -> None:
        r"""
        This method allows you to remove authorization for an account.

        :param acc_id: Account identifier.
        :param pod_id: Pod identifier.
        """

    def pod_acl_challenge(self, *, com_id: int, pod_id: int, acc_id: Optional[int] = None, cls_id: Optional[int] = None, team: Optional[str] = None, **kwargs) -> uuid.UUID:
        r"""
        This method allows you to test against a pod access control list.

        :param int com_id: Community identifier.
        :param int pod_id: Pod identifier.
        :param int acc_id: Account identifier.
        :param int cls_id: Class identifier.
        :param str team: Team assignment.
        :return: If matching rule found, pod access control list UUID.
        """

    def pod_acl_get(self, *, pacl_uuid: uuid.UUID, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method allows you to retrieve a pod access control list.

        :param pacl_uuid: Pod access control list UUID.
        :return: Pod access control list.
        """

    def pod_acl_list(self, *, pod_id: int, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method allows you to retrieve a list of pod access controls per pod.

        :param pod_id: Pod identifier.
        :return: Pod access control list.
        """

    def pod_acl_remove(self, *, pacl_uuid: uuid.UUID, **kwargs) -> None:
        r"""
        This method allows you to remove a pod access control list.

        :param pacl_uuid: Pod access control list UUID.
        """

    def pod_add(self, *, pod_id: int, pt_id: str, devices: Optional[List[Dict[str, Any]]] = None, pod_acl_enabled: bool = False, pod_adv_settings: Optional[str] = None, pod_auto_net_enabled: bool = True, pod_auto_net_host_setup: bool = True, pod_auto_net_host_teardown: bool = True, pod_cat: netlab.enums.pod.PodCategory = netlab.enums.PodCategory.PERSISTENT_VM, pod_desc: Optional[str] = None, pod_name: Optional[str] = None, **kwargs) -> Literal['OK']:
        r"""
        This method allows you to add a pod to the NETLAB+ system. Pods created will be OFFLINE after added.

        :param pod_id: Unique pod identifier.
        :param pt_id: Pod type identifier.
        :param devices: Array of devices associated with this pod. This is for real equipment pods only.
        :param pod_acl_enabled: Pod access control list enabled.
        :param pod_adv_settings: Advanced settings for pod configuration.
        :param pod_auto_net_enabled: Auto-networking enabled.
        :param pod_auto_net_host_setup: Auto-networking host setup enabled.
        :param pod_auto_net_host_teardown: Auto-networking host teardown enabled.
        :param pod_cat: Pod category type.
        :param pod_desc: Pod description.
        :param pod_name: Pod name.
        """

    def pod_clone_task(self, *, source_pod_id: int, clone_pod_id: int, clone_pod_name: str, pc_clone_specs: Union[List[netlab.datatypes.pod.PCCloneSpec], netlab.datatypes.pod.PCCloneSpec, NoneType] = None, severity_level: netlab.enums.common.HDRSeverity = netlab.enums.HDRSeverity.WARN, **kwargs) -> netlab.datatypes.common.HDRResult:
        r"""
        Clone a pod.

        :param source_pod_id: Source pod unique identifier.
        :param clone_pod_id: Cloned pod unique identifier
        :param clone_pod_name: Cloned unique pod name.
        :param pc_clone_specs: Array of PC clone specifications. Any unpassed params will be taken from the existing
            pods. If a dict is passed, the params will be used on every pod.
        :param severity_level: Display detailed events for the task only at this severity level or
            higher.
        :return: HDR result

        **pc_clone_specs**

        The format requires a list of dictionaries.
        One dictionary per each PC in the pod, e.g. `[{pc.clone.spec.1}, {pc.clone.spec.2}]`.
        See ``PCCloneSpec`` the expected value type and a key description.

        **Example:**

        ::

            pc_clone_specs = [{
                    "clone_role":"NORMAL",
                    "clone_type":"LINKED",
                    "source_snapshot":"GOLDEN_MASTER",
                    "pc_type":"AVMI",
                    "clone_vh_id":1,
                    "clone_name":"Test_Linux_Install_pod04_CentOS Server",
                    "clone_storage_alloc":"ONDEMAND",
                    "clone_datastore":"local",
                    "clone_snapshot":"GOLDEN_MASTER"
                }, {
                    "clone_role":"NORMAL",
                    "clone_type":"LINKED",
                    "source_snapshot":"GOLDEN_MASTER",
                    "pc_type":"AVMI",
                    "clone_vh_id":1,
                    "clone_name":"Test_Linux_Install_pod04_Ubuntu Workstation",
                    "clone_storage_alloc":"ONDEMAND",
                    "clone_datastore":"local",
                    "clone_snapshot":"GOLDEN_MASTER"
                }]

        """

    def pod_get(self, *, pod_id: int, properties: Union[List[str], Literal['default', 'all']] = 'default', **kwargs) -> Dict[str, Any]:
        r"""

        :param pod_id: Unique pod identifier.
        :param properties: Properties consist of any combination of properties listed below under Properties.
                           You may also use **"all"** to include all properties, or **"default"** for a smaller subset
                           of properties.

        :return: Returns a dictionary object containing the following properties:

        **Properties**

        def_im_name
            Default image name.
        def_topology_image
            Default topology image URL.
        def_vlan_map
            Default VLAN mapping.
        device_count
            Count of devices in pod type.
        devices
            List of devices in pod type.
        pod_acl_enabled
            Pod access control list enabled.
        pod_admin_state
            Administrative pod states.
        pod_adv_settings
            A list of all advanced settings.
        pod_auto_net_enabled
            Automatic VM networking enabled.
        pod_auto_net_host_setup
            Automatic Host networking setup enabled.
        pod_auto_net_host_teardown
            Automatic Host networking teardown enabled.
        pod_cat
            Pod category type. :py:class:`netlab.enums.PodCategory`
        pod_csw_base_vlan
            Pod control switch base VLAN.
        pod_csw_id
            Pod control switch id.
        pod_current_state
            Pod current state status.
        pod_desc
            Pod description.
        pod_id
            Unique pod identifier.
        pod_managed
            Pod is managed.
        pod_name
            Pod name.
        pod_origin
            Pod origin.
        pod_res_id
            Current pod reservation identifier.
        pod_task_id
            Current pod task identifier.
        pod_task_info
            Current pod task information.
        pod_task_type
            Current pod task type.
        pod_uuid
            Globally unique pod identifier.
        pt_actions
            Pod type actions enabled.
        pt_adv_settings
            Long string of advanced settings.
        pt_apc_port_count
            Switched outlet port count requirement.
        pt_apdid
            Author identifier for pod design.
        pt_as_port_count
            Access server port count requirement.
        pt_author
            Pod design author.
        pt_build
            Pod build number.
        pt_copyright
            Pod design copyright.
        pt_csw_port_count
            Control switch port count requirement.
        pt_desc
            Pod type description.
        pt_gpdid
            Global unique identifier.
        pt_id
            Pod type identifier.
        pt_name
            Pod type name.
        pt_notes
            Pod type notes.
        pt_org
            Pod design organization.
        pt_origin
            Pod type origin.
        pt_pod_max
            Max pod count of this type.
        pt_removable
            Pod type is removable.
        pt_tabs
            Pod type tabs enabled.
        pt_url
            Pod design support URL.
        pt_vlan_pool
            Pod type vlan pool.
        remote_pc
            List of remote PCs in pod type with their expanded properties. See Remote PC table below.
        remote_pc_count
            Count of remote PCs in pod type.
        reservations
            The number of reservations scheduled or in progress for this pod.
        sched_image
            Scheduler image URL.
        vm_alloc
            VM resource allocation properties. `netlab.datatypes.VMAlloc` Added in 18.5.0.
        """

    def pod_list(self, *, pod_cat: Optional[netlab.enums.pod.PodCategory] = None, **kwargs) -> List[Dict[str, Any]]:
        r"""
        List pods on the system.

        :param pod_cat: Pod category type.
        :return: Returns a list of dictionary objects containing the following properties:

        **Properties**

        def_topology_image
            Default topology image URL.
        pod_acl_enabled
            Pod access control lists enabled for this pod.
        pod_admin_state
            Pod administrative state. :py:class:`netlab.enums.PodAdminState`
        pod_cat
            Pod category. :py:class:`netlab.enums.PodCategory`
        pod_current_state
            Pod current state. :py:class:`netlab.enums.PodCurrentState`
        pod_desc
            Pod description.
        pod_dyn_vlan
            Pod is using dynamic vlans.
        pod_id
            Unique pod identifier.
        pod_managed
            Pod is managed (currently always True).
        pod_name
            Pod name.
        pod_uuid
            Pod name.
        pod_res_id
            Current pod reservation identifier.
        pt_apdid
            Author identifier for pod design.
        pt_desc
            Pod type description.
        pt_gpdid
            Global unique identifier.
        pt_id
            Pod type identifier.
        pt_name
            Pod type name.
        sched_image
            Scheduler image URL.
        """

    def pod_list_used_ids(self, **kwargs) -> List[int]:
        r"""
        List the used pod_id's on the system.

        :return: Returns a list of pod_ids
        """

    def pod_pc_get(self, *, pod_id: Optional[int] = None, pl_index: Optional[int] = None, pc_id: Optional[int] = None, **kwargs) -> Dict[str, Any]:
        r"""
        Get information regarding a pod pc.

        :param pod_id: Pod ID
        :param pl_index: PC Pod index
        :param pc_id: unique pc identifier

        :return: On success, returns the following properties:

        **Properties**

        pc_icon
            Icon identifier. :py:class:`netlab.enums.PCIcon`
        pc_id
            Unique pc identifier.
        pc_label
            PC label.
        pc_online
            PC online.
        pc_origin
            PC origin.
        pc_os_id
            PC operating system identifier.
        pc_os_name
            NETLAB+ operating system name.
        pc_pod_id
            pod_id pc is associated to.
        pc_pod_index
            Index of pods.
        pc_revert_to_scrub
            Revert pc during scrub.
        pc_type
            PC type. :py:class:`netlab.enums.PCType`
        pc_vnc_ip_addr
            IP Address of vnc (ESXi host) server.
        pc_vnc_port
            Port number VNC is running on.
        pc_vnc_use_copy_rect
            Always Allow VNC to use copy rect encoding.
        pl_icon
            Pod design PC icon identifier. :py:class:`netlab.enums.PLIcon`
        pl_index
            PC pod index.
        pl_label
            Remote pc label.
        pt_id
            Pod type identifier.
        vdc_id
            Agent hostname/IP address.
        vdc_name
            VM Datacenter name.
        vh_bios_date
            Timestamp of BIOS creation date.
        vh_bios_version
            BIOS version installed.
        vh_com_path
            Virtual host communication path. :py:class:`netlab.enums.VirtualHostComPath`
        vh_cpu_cores
            Total count of CPU cores on virtual host.
        vh_cpu_mhz
            Speed in MHz of CPU.
        vh_cpu_model
            CPU model identification.
        vh_cpu_threads
            Number of threads CPUs can handle.
        vh_cpu_threads
            Number of threads CPUs can handle.
        vh_date_modified
            Timestamp of virtual host information has been modified.
        vh_date_tested
            Timestamp of virtual host test communication.
        vh_id
            Virtual host identifier.
        vh_inside_ipv4_addr
            Inside interface ipv4 address.
        vh_inside_vswitch_0
            Virtual host inside vSwitch.
        vh_last_test_status
            Status of last virtual host test communication.
        vh_memory_mb
            Total RAM in MB of virtual host.
        vh_name
            Virtual host hostname.
        vh_online
            Virtual host is online.
        vh_os_build
            Operating system build number.
        vh_os_description
            Operating system description.
        vh_os_name
            Operating system name.
        vh_os_type
            Operating system type.
        vh_os_vendor
            Operating system vendor.
        vh_os_version
            Operating system version.
        vh_outside_ipv4_addr
            Outside interface ipv4 address.
        vh_pra_enabled
            Proactive resource awareness is enabled.
        vh_pra_max_cpu
            Max number of CPUs for PRA.
        vh_pra_max_mem_mb
            Max amount of RAM in MB for PRA.
        vh_pra_max_vm
            Max amount of virtual machines for PRA.
        vh_sys_model
            System model.
        vh_sys_service_tag
            System service tag.
        vh_sys_vendor
            System vendor.
        vh_uuid
            Virtual host unique global identifier.
        vhg_id
            Virtual host group identifier.
        vm_alloc_cpu_n
            Total amount of allocated CPUs.
        vm_alloc_mem_mb
            Total amount of allocated RAM.
        vm_auto_display
            Virtual machine auto display port configuration.
        vm_auto_network
            Virtual machine auto networking.
        vm_auto_settings
            Virtual machine auto settings.
        vm_child_count
            Total count of children VMs.
        vm_comments
            Virtual machine comments from VMX.
        vm_date_added
            Timestamp of virtual machine added to NETLAB+ inventory.
        vm_id
            Virtual machine identifier.
        vm_name
            Virtual machine name.
        vm_netlab_os_id
            NETLAB+ match to vm_vendor_os_id.
        vm_parent_id
            Virtual machine parent identifier, if VM is a link clone.
        vm_parent_snapname
            Virtual machine parent snapshot name, if VM is a link clone.
        vm_path
            Virtual machine path on datastore.
        vm_power_state
            Virtual machine power state.
        vm_role
            Virtual machine role in NETLAB+ inventory. :py:class:`netlab.enums.VirtualMachineRole`
        vm_runtime_vh_id
            Unique identifier of runtime virtual host.
        vm_sanity_checks
            Sanity checks.
        vm_shutdown_pref
            Shutdown preference.
        vm_snapshot
            This is what the VM reverts to when the pod is reset. You can take multiple snapshots with the same name,
            without having to update this field. Update this field with a call to
            :meth:`~netlab.api.PodApiMixin.pod_pc_update`
        vm_uuid
            Virtual machine unique identifier.
        vm_vendor_os_id
            Vendor operating system identifier.
        vm_vendor_os_name
            Vendor operating system name.
        """

    def pod_pc_update(self, *, pc_id: int, pc_type: Optional[Literal['ABSENT', 'AVMI']] = None, pc_os_id: Optional[str] = None, pc_online: Optional[bool] = None, vm_shutdown_pref: Optional[str] = None, vm_id: Optional[int] = None, vm_snapshot: Optional[str] = None, vm_auto_display: Optional[bool] = None, vm_auto_network: Optional[bool] = None, vm_auto_settings: Optional[bool] = None, vm_sanity_checks: Optional[bool] = None, **kwargs) -> None:
        r"""
        Update information regarding a pod pc.

        :param pc_id: unique pc identifier
        :param pc_type: PC type (ABSENT, AVMI)
        :param pc_os_id: PC operating system identifier
        :param pc_online: PC online
        :param vm_shutdown_pref: Shutdown preference
        :param vm_id: Virtual machine identifier
        :param vm_snapshot: This is what the VM reverts to when the pod is reset. You can take multiple snapshots
                                with the same name, without having to update this field.
        :param vm_auto_display: Virtual machine auto display port configuration
        :param vm_auto_network: Virtual machine auto networking
        :param vm_auto_settings: Virtual machine auto settings
        :param vm_sanity_checks: Virtual machine sanity checks
        """

    def pod_remove_task(self, *, pod_id: int, remove_vms: netlab.enums.pod.RemoveVMS = netlab.enums.RemoveVMS.NONE, severity_level: netlab.enums.common.HDRSeverity = netlab.enums.HDRSeverity.WARN, **kwargs) -> netlab.datatypes.common.HDRResult:
        r"""
        :param pod_id: Pod unique identifier.
        :param remove_vms: Specifies the method for removing the virtual machines.
        :param severity_level: Display detailed events for the task only at this severity level or
            higher.

        :return: HDR result
        """

    def pod_state_change(self, *, pod_id: int, state: netlab.enums.pod.PodState, **kwargs) -> Literal['OK']:
        r"""
        Sets pod state to either ONLINE, OFFLINE or RESUME.

        :param pod_id: Pod ID
        :param state: PC Pod State
        """

    def pod_types_get(self, *, pt_id: str, properties: Union[List[str], Literal['default'], Literal['all']] = 'default', **kwargs) -> Dict[str, Any]:
        r"""
        Returns the build, id and name of installed pods on queried system.

        :param pt_id: Pod Type ID is a alpha/num hash with prefix.
        :param properties: Properties consist of any combination of properties listed below under Properties.
                           You may also use **"all"** to include all properties, or **"default"** for a smaller subset
                           of properties.

        :return: Returns all or selected properties from the list initially passed for return.

        **Properties**

        pt_id
            Pod type identifier.
        pt_name
            Account email.
        pt_build
            Account Family(Last) name.
        pt_gpdid
            Global unique identifer.
        pt_apdid
            Author identifier for pod design.
        pt_desc
            Pod type description.
        pt_index
            Pod type index.
        pt_type
            Pod type id
        sched_image
            Location of scheduler image.
        def_topology_image
            Default topology image URL.
        def_im_name
            Default image map name.
        def_vlan_map
            Default VLAN map.
        pt_tabs
            Pod type tabs.
        pt_actions
            Pod type actions.
        pt_origin
            Pod type origin.
        pt_vlan_pool
            Pod type vlan pool.
        pt_pod_max
            Max amount of pod types allowed on system.
        pt_notes
            Pod type notes.
        pt_csw_port_count
            Number of consecutive ports on control switch required by pod type.
        pt_as_port_count
            Number of access server ports required by pod type.
        pt_apc_port_count
            Number of switched outlet ports required by pod type.
        pt_build
            Pod type build number.
        pt_author
            Pod type author.
        pt_org
            Pod type organization.
        pt_copyright
            Pod type copyright.
        pt_url
            Pod type URL address.
        pt_removable
            Allows pod type to be uninstalled.
        pt_ae_pod
            Pod type is for NETLAB+ AE.
        pt_adv_settings
            Pod type advanced settings.
        hotspots
            Returns array of hotspot information for **pt_id**.

            - im_coords
            - im_dev_class
            - im_dev_name
            - im_group
            - im_name
            - im_shape

        remote_pc_layout
            Returns array of remote PC layout information for **pt_id**.

            - pl_access_types
            - pl_def_access_message
            - pl_def_offline_message
            - pl_icon
            - pl_index
            - pl_label
            - pl_os_types
            - pl_pt_id
            - pl_reboot_to_scrub
            - pl_required

        remote_pc_count
            Get a count of the remote PCs per pod type.
        device_layout
            Returns array of device layout information for **pt_id**.

            - dl_pt_id
            - dl_index
            - dl_name
            - dl_class
            - dl_auto
            - dl_managed
            - dl_so_base_ix
            - dl_as_base_ix
            - dl_cs_base_ix
            - dl_eth_recv_port
            - dl_eth_req
            - dl_ser_req
            - dl_ae_ifx

        device_count
            Get count of the devices for pod type.
        pod_cat_values
            Returns array of pod categories (``PodCategory``).
        cables
            Returns list of cable connections for pod type.

            - ca_pt_id
            - ca_from_type
            - ca_from_index
            - ca_from_port
            - ca_seq
            - ca_cable
            - ca_to_dev
            - ca_to_port
        """

    def pod_types_list(self, *, properties: Union[List[str], Literal['default', 'all']] = 'default', **kwargs) -> List[Dict[str, Any]]:
        r"""
        Obtain a list of pod types.

        :param properties: Properties consist of any combination of properties listed below under Properties.
                           You may also use **"all"** to include all properties, or **"default"** for a smaller subset
                           of properties.
        :return: On success, returns [rt_id, pt_build, pt_name] by default, or the following properties if requested.

        **Properties**

        pt_id
            Pod type identifier.
        pt_name
            Account email.
        pt_build
            Account Family(Last) name.
        pt_gpdid
            Global unique identifer.
        pt_apdid
            Short unique identifier.???
        pt_desc
            Pod type description.
        pt_index
            Pod type index.
        pt_type
            ???
        sched_image
            Location of scheduler image.
        def_topology_image
            Location of the default topology image.
        def_im_name
            Default image map name.
        def_vlan_map
            Default VLAN map.
        pt_tabs
            Pod type tabs.
        pt_actions
            Pod type actions.
        pt_origin
            Pod type origin.
        pt_vlan_pool
            Pod type vlan pool.
        pt_pod_max
            Max amount of pod types allowed on system.
        pt_notes
            Pod type notes.
        pt_csw_port_count
            Number of consecutive ports on control switch required by pod type.
        pt_as_port_count
            Number of access server ports required by pod type.
        pt_apc_port_count
            Number of switched outlet ports required by pod type.
        pt_build
            Pod type build number.
        pt_author
            Pod type author.
        pt_org
            Pod type organization.
        pt_copyright
            Pod type copyright.
        pt_url
            Pod type URL address.
        pt_removable
            Allows pod type to be uninstalled.
        pt_ae_pod
            Is pod type for NETLAB+ AE???.
        pt_adv_settings
            Pod type advanced settings.
        remote_pc_count
            Get count of the remote PCs per pod type.
        device_count
            Get count of the devices per pod type.

        """

    def pod_update(self, *, pod_id: int, pod_name: Optional[str] = None, pod_desc: Optional[str] = None, pod_auto_net_enabled: Optional[bool] = None, pod_auto_net_host_setup: Optional[bool] = None, pod_auto_net_host_teardown: Optional[bool] = None, pod_adv_settings: Optional[str] = None, pod_acl_enabled: Optional[bool] = None, **kwargs) -> None:
        r"""
        This method allows you to update a pod on the NETLAB+ system.

        :param int pod_id: Unique pod identifier.
        :param str pod_name: Pod name.
        :param str pod_desc: Pod description.
        :param bool pod_auto_net_enabled: Auto-networking enabled.
        :param bool pod_auto_net_host_setup: Auto-networking host setup enabled.
        :param bool pod_auto_net_host_teardown: Auto-networking host teardown enabled.
        :param str pod_adv_settings: Advanced settings for pod configuration.
        :param bool pod_acl_enabled: Pod access control list enabled.
        """

    def reservation_cancel(self, *, res_id: int, **kwargs) -> None:
        r"""
        Cancel a reservation in NETLAB+ prior to reservation being started.

        NOTE - if you wish to end a reservation that is already started use reservation_post.

        :param res_id: Reservation unique identifier.
        """

    def reservation_extend(self, *, res_id, **kwargs) -> Dict[str, Any]:
        r"""
        Request a 30 minute lab reservation extension.

        :param int res_id: Reservation identifier.

        :return: Returns an object with the following properties:
        :rtype: dict

        **Properties**

        status
            Status code.
        reason
            Textual message that is suitable for display (English).

        **Status Codes**

        OK
            The reservation was extended.
        CLASS_LIMIT_EXCEEDED
            Reservation cannot be extended because of **cls_ext_slots_per_res** setting limit.
        COMMUNITY_LIMIT_EXCEEDED
            Reservation cannot be extended because of **com_ext_slots_per_res** setting limit.
        TIME_SLOT_UNAVAILABLE
            The next time slot is occupied by another reservation.
        POD_ACTIVE_MAX
            Maximum number of pods in use.
        RESERVATION_ALREADY_COMPLETED
            The reservation has already completed and cannot be extended.
        E_ACCESS_DENIED
            Student/learner cannot extend ILT reservation.
        STATE_NOT_ACTIVE_LAB
            Reservation is not in the active lab state.
        TOO_EARLY
            Cannot extend before T-00:15:59 minutes/seconds.
        TOO_LATE
            Cannot extend after T-00:00:10 seconds.

        **Restrictions For All Users**

        + An extension cannot be made before T-00:15:59 from the reservation post time.  This is about 26 minutes from
          the blocked end time and 16 minutes of the usable time remaining.
        + The next 30 minute time slot must not be already scheduled by another reservation.
        + The extension cannot exceed maximum pods in use limit and/or proactive resource awareness settings.

        **Restrictions for Students and Teams**

        + The number of extensions that a student or team can request are limited by community and class settings.
        + For backward setting compatibility, communities and classes do not allow extensions to be made by students or
          teams by default.

            - The administrator must specifically allow extensions for students and teams per community via the
              **com_ext_slots_per_res** setting.
            - The instructor must specifically allow extensions for students and teams per class via the
              **cls_ext_slots_per_res** setting.
            - The number of extensions that a student or team can request in a single reservation will be the more
              restrictive of the two settings.
        + A student (or instructor learner) may not extend an ILT reservation.  Only a lead instructor can do that.
        """

    def reservation_get(self, *, res_id: int, **kwargs) -> Dict[str, Any]:
        r"""
        Get parameters of a reservation.

        :param int res_id: Reservation identifier.
        :return: On success, returns an object with the following properties:
        :rtype: dict

        **Properties**

        acc_com_id
            Community identifier.
        acc_full_name
            Account display name.
        acc_id
            Account identifier.
        cls_div_id
            Community identifier.
        cls_id
            Class identifier.
        cls_name
            Class name.
        ex_id
            Lab exercise identifier.
        ex_name
            Lab exercise name.
        pod_desc
            Pod description.
        pod_id
            Unique pod identifier.
        pod_name
            Pod name.
        pt_desc
            Pod type description.
        pt_id
            Pod type identifier.
        pt_name
            Account email.
        res_acc_id
            Account ID.
        res_active_time
            Active reservation timestamp.
        res_asm_data
            ???
        res_attend_time
            Time reservation was attended.
        res_cls_id
            Class identifier.
        res_com_id
            Community identifier.
        res_config
            Initial configuration.
        res_done
            Reservation is done.
        res_end
            Timestamp scheduled end of reservation.
        res_ex_id
            Reservation lab exercise identifier.
        res_flags
            ???
        res_id
            Reservation identifier.
        res_init_fail
            Count of failures during initialization.
        res_is_active
            Reservation is active.
        res_minutes
            Count of minutes for reservation.
        res_pod_id
            Reservation pod identifier.
        res_post_time
            Timestamp of actual end of reservation.
        res_preload_time
            Timestamp UTC lab will preload.
        res_pt_id
            Reservation pod type identifier.
        res_remaining_dhms
            Days, hours, min, sec remaining if pod is in ACTIVE_LOAD or ACTIVE_INIT state.
        res_remaining_sec
            Seconds remaining if pod is in ACTIVE_LOAD or ACTIVE_LAB state.
        res_start
            Timestamp to start reservation.
        res_team
            Reservation team setting.
        res_type
            Reservation type. :py:class:`netlab.enums.ReservationType`
        res_uuid
            Reservation unique identifier.
        sched_image
            Location of the scheduler image.
        """

    def reservation_make(self, *, type: netlab.enums.reservation.ReservationType, pod_id: int, cls_id: int, end_time: datetime.datetime, start_time: Optional[datetime.datetime] = None, acc_id: Optional[int] = None, reserver_id: Optional[int] = None, tz_id: Optional[int] = None, tz_olson: Optional[str] = None, team: Optional[str] = None, pt_id: Optional[int] = None, ex_id: str, init_config: netlab.enums.reservation.InitConfig = netlab.enums.InitConfig.NONE, **kwargs) -> Dict[str, Any]:
        r"""
        :param type: Type of reservation.
        :param pod_id: Pod identifier.
        :param cls_id: Class identifier.
        :param end_time: Local time end of reservation. This must be on a half hour slot boundary.
        :param start_time: Local time start of reservation. If not specified it will use the current
            datetime.
        :param tz_id: Timezone identifier.
        :param tz_olson: IANA timezone name. If not specified, the timezone of the user identified by acc_id will be
            used.
        :param team: Team identifier.
        :param pt_id: Pod type identifier.
        :param ex_id: Exercise identifier **(required)**.
        :param acc_id: Account identifier for the reservation. Defaults to **reserver_id**.
        :param init_config: Initial configuration.
        :param reserver_id: Reserver identifier. Defaults to the request user. An admin can use a **reserver_id** to
            make reservations for others.

        :return: On success, returns an object with the following properties:

        **Properties**

        res_id
            Reservation identifier.
        res_start_utc
            Reservation start in UTC.
        res_end_utc
            Reservation end in UTC.
        res_minutes
            Reservation time in minutes
        """

    def reservation_plan(self, *, acc_id: Optional[int] = None, cls_id: Optional[int] = None, date: datetime.date, ex_id: Optional[int] = None, pod_id: Optional[int] = None, reserver_id: Optional[int] = None, team: Optional[int] = None, type: netlab.enums.reservation.ReservationType, tz_id: Optional[int] = None, tz_olsen: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        r"""
        Used to provide information on all pods available for a proposed date.

        :param acc_id: Account identifier.
        :param cls_id: Class identifier.
        :param date: Date.
        :param ex_id: Exercise identifier.
        :param pod_id: Pod identifier.
        :param reserver_id: Reserver identifier.
        :param team: Team identifier.
        :param type: Type of reservation.
        :param tz_id: Timezone identifier.
        :return: On success, returns an object with the following properties:

        **Properties**

        clock_pref
            User clock preference.
        show_date
            Proposed date.
        min_date
            cls_id start date or SystemMinDate.
        max_date
            cls_id end date or SystemMaxDate.
        time_now
            Current time.
        time_format
            User preferred time format.
        first_weekday
            User preferred first day of the week.
        serial
            Incremented number when there is a scheduler transaction.
        slot_minutes
            Number of minutes in reservation slot.
        time_slots
            Array of available time slots.
        pods
            Array of pods available.
        """

    def reservation_post(self, *, res_id: int, **kwargs) -> None:
        r"""
        Ends a reservation that has already started.

        :param res_id: Reservation identifier.
        """

    def reservation_query(self, *, active: Optional[bool] = None, scope: netlab.enums.reservation.ReservationScope = netlab.enums.ReservationScope.ALL, min_time: Optional[datetime.datetime] = None, max_time: Optional[datetime.datetime] = None, com_id: Optional[int] = None, cls_id: Optional[int] = None, pod_id: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
        r"""
        Return a list of reservations filtered on criteria. Take note of the acceptable overrides.

        :param scope: Reservation scope.
        :param active: Filter active reservations.
        :param cls_id: Class identifier.
        :param com_id: Community identifier.
        :param max_time: Maximum time range.
        :param min_time: Minimum time range.
        :param pod_id: Pod identifier.

        :return: On success, returns an object with the following properties:

        **Properties**

        acc_com_id
            Community identifier.
        acc_full_name
            Account display name.
        acc_id
            Account identifier.
        cls_div_id
            Community identifier.
        cls_id
            Class identifier.
        cls_name
            Class name.
        ex_id
            Lab exercise identifier.
        ex_name
            Lab exercise name.
        pod_desc
            Pod description.
        pod_id
            Unique pod identifier.
        pod_name
            Pod name.
        pt_desc
            Pod type description.
        pt_id
            Pod type identifier.
        pt_name
            Account email.
        res_acc_id
            Account identifier.
        res_active_time
            Active reservation timestamp.
        res_attend_time
            Time reservation was attended.
        res_cls_id
            Class identifier.
        res_com_id
            Community identifier.
        res_config
            Initial configuration.
        res_done
            Reservation is done.
        res_end
            Timestamp scheduled end of reservation.
        res_ex_id
            Reservation lab exercise identifier.
        res_flags
            Reservation hex code for pod state.
        res_id
            Reservation identifier.
        res_init_fail
            Count of failures during initialization.
        res_is_active
            Reservation is active.
        res_minutes
            Count of minutes for reservation.
        res_pod_id
            Reservation pod identifier.
        res_post_time
            Timestamp of actual end of reservation.
        res_pt_id
            Reservation pod type identifier.
        res_start
            Timestamp to start reservation.
        res_team
            Reservation team setting.
        res_type
            Type of reservation. :py:class:`netlab.enums.ReservationType`
        res_uuid
            Reservation unique identifier.
        sched_image
            Location of the scheduler image.
        """

    def reservation_summary(self, **kwargs) -> Dict[str, Any]:
        r"""
        This method allows you to retrieve a summary of all reservations.

        :return: On success, returns an object with the following properties:

        **Properties**

        active_reservations
            Count of active reservations.
        completed_reservations
            Count of completed reservations.
        future_reservations
            Count of future reservations.
        pods_in_use
            Count of pods in use.
        total_reservations
            Count of total reservations.

        """

    def reservation_time_delta(self, *, end: datetime.datetime, start: Optional[datetime.datetime] = None, tz_id: Optional[int] = None, tz_olson: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        r"""
        This method returns time between two timestamps with optional timezone offset.

        :param datetime.datetime end: End time. This must be on a half hour increment.
        :param datetime.datetime start: Start time. Defaults to now if not specified.
        :param int tz_id: Timezone identifier.
        :param str tz_olson: Timezone olson.

        :return: On success, returns an object with the following properties:
        :rtype: dict

        **Properties**

        days
            Number of days to increase/decrease.
        hours
            Number of hours to increase/decrease.
        minutes
            Number of minutes to increase/decrease.
        months
            Number of months to increase/decrease.
        """

    def reservation_time_now(self, *, tz_id: Optional[int] = None, tz_olson: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        r"""
        This method returns the current NETLAB time.

        :param tz_id: Timezone identifier.
        :param tz_olson:

        :return: On success, returns an object with the following properties:
        :rtype: dict

        **Properties**

        local
            Local date time.
        local_am_pm
            AM/PM indicator.
        local_day
            Local day of the month.
        local_day_of_week
            Local day of the week.
        local_hmap
            Local time and am/pm.
        local_hms
            Local time.
        local_hour_12
            Local 12 Hour time.
        local_hour_24
            Local 24 Hour time.
        local_minute
            Local minute time.
        local_second
            Local second time.
        local_year
            Local year.
        local_ymd
            Local YYYY-MM-DD.
        tz_id
            Timezone identifier.
        tz_is_dst
            Timezone is in Daylight Savings Time.
        tz_name
            Name of the timezone.
        tz_olson
            Timezone olson.
        utc
            Coordinated Universal Time.
        """

    def reservation_time_offset(self, *, time: Optional[datetime.datetime] = None, op: Optional[Literal['+', '-']] = None, tz_id_in: Optional[int] = None, tz_olson_in=None, tz_id_out=None, tz_olson_out=None, slot_roundup=False, years=None, months=None, weeks=None, days=None, hours=None, minutes=None, seconds=None, **kwargs) -> Dict[str, Any]:
        r"""
        This method returns the current time with a timezone offset.

        :param datetime time: Time input.
        :param str op: Operator. "+" rounds up. "-" rounds down.
        :param int tz_id_in: Timezone identifier input.
        :param str tz_olson_in: Timezone olson input.
        :param int tz_id_out: Timezone identifier output.
        :param str tz_olson_out: Timezone olson output.
        :param bool slot_roundup: Round up to nearest slot. i.e. 30 min interval. Defaults to False.
        :param int years: Number of years to increase/decrease.
        :param int months: Number of months to increase/decrease.
        :param int weeks: Number of weeks to increase/decrease.
        :param int days: Number of days to increase/decrease.
        :param int hours: Number of hours to increase/decrease.
        :param int minutes: Number of minutes to increase/decrease.
        :param int seconds: Number of seconds to increase/decrease.

        :return: On success, returns an object with the following properties:
        :rtype: dict

        **Properties**

        days
            int
        hours
            int
        minutes
            int
        months
            int
        time_in_local
            datetime
        time_in_utc
            datetime
        time_out_local
            datetime
        time_out_utc
            datetime
        tz_id_in
            int
        tz_id_out
            int
        tz_olson_in
            str
        tz_olson_out
            str
        """

    @staticmethod
    def reservation_timeslot_adjuster(*, user_time: datetime.datetime, round_low: bool = False) -> datetime.datetime:
        r"""
        Round a datetime to the nearest half hour, which is required for some times in netlab.

        :param user_time: Must be a datetime object. Adjusted for fulfilling time slot
            if not already time slot acceptable.
        :param round_low: True: rounds time in minutes down to the low timeslot. False: rounds time up to next
            timeslot.

        :return: Datetime rounded to half hour.
        """

    def system_perf_query(self, *, start_time: datetime.datetime, end_time: Optional[datetime.datetime] = None, metrics: Optional[List[str]] = None, sources: Optional[List[str]] = None, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method is used to query system performance metrics.

        :param start_time: If specified, only return metrics recorded on or after start time.
        :param end_time: If specified, only return metrics recorded on or before end time.
        :param metrics: If specified, only returns metrics from :ref:`this list<System Performance Metrics>`.
        :param sources: If specified, only returns metrics originating from sources in this list.
            Valid sources include mbusd, podspd, sysspd, respd, userspd, vmspd, histpd, filespd.
        :return: A list of dicts with the following properties.

        **Properties**

        sp_time
            The date/time the metric was recorded.
        sp_metric
            The metric identifier.
        sp_source
            The module/program that produced the metric.
        sp_value
            The numeric value of the metric.
        """

    def system_status_get(self, **kwargs) -> netlab.api.system_results.SystemStatusGetResult:
        r"""
        This method allows you to query NETLAB+ system information.

        :return: Returns a system status object with the following properties:

        **Properties**

        cpu_n
            Number of CPUs detected by the virtual appliance.
        uptime_sec
            System uptime in seconds.
        hostname
            NETLAB+ domain name
        sys_lic_exp_date
            License expiration date
        sys_lic_op_state
            License operation stsate
        sys_logins_enabled
            User logins status
        sys_maint_ends
            Mainenance end date
        sys_mode
            System mode
        sys_name
            System name
        sys_product_id
            Product identifier
        sys_sdn_release_date
            Software distribution date
        sys_sdn_release_type
            Software distribution release type
        sys_sdn_version
            Software distribution version
        sys_serial
            System serial number
        """

    def system_time_timezone_get(self, *, tz_id, **kwargs) -> Dict[str, Any]:
        r"""
        Match a netlab timezone id to the timezone iana.

        :return: Returns an object that represents a timezone.

        **Properties**

        tz_id
            The id of timezone (specific to netlab).
        tz_iana
            The iana identifier of the timezone.
        tz_name
            The name of the timezone.
        tz_sort
            The sort order of the timezone.
        """

    def system_time_timezone_list(self, **kwargs) -> List[Dict[str, Any]]:
        r"""
        Match a netlab timezone id to the timezone iana.

        :return: Returns an object that represents a timezone.
        :rtype: dict

        **Properties**

        tz_id
            The id of timezone (specific to netlab).
        tz_iana
            The iana identifier of the timezone.
        tz_name
            The name of the timezone.
        tz_sort
            The sort order of the timezone.
        """

    def system_usage_cpu(self, **kwargs):
        r"""
        This method allows you to query NETLAB+ CPU usage.

        :return: Returns an object with N+1 properties, where N is the number of CPUs. The CPUs are listed from 0 to
                 N-1 and also includes **all** . They each contain an object with the following properties:
        :rtype: dict

        **Properties**

        gnice_pct
            The percentage of time spent by the CPU or CPUs to run a niced guest.
        guest_pct
            The percentage of time spent by the CPU or CPUs to run a virtual processor.
        idle_pct
            The percentage of time that the CPU or CPUs were idle and the system did not have an outstanding disk I/O
            request.
        iowait_pct
            The percentage of time that the CPU or CPUs were idle during which the system had an outstanding disk I/O
            request.
        irq_pct
            The percentage of time spent by the CPU or CPUs to service hardware interrupts.
        nice_pct
            The percentage of CPU utilization that occurred while executing at the user level with nice priority.
        soft_pct
            The percentage of time spent by the CPU or CPUs to service software interrupts.
        steal_pct
            The percentage of time spent in involuntary wait by the virtual CPU or CPUs while the hypervisor was
            servicing another virtual processor.
        sys_pct
            The percentage of CPU utilization that occurred while executing at the system level (kernel). Note that
            this does not include time spent servicing hardware and software interrupts.
        usr_pct
            The percentage of CPU utilization that occurred while executing at the user level (application).
        """

    def system_usage_disk(self, **kwargs) -> Dict[str, Any]:
        r"""
        This method allows you to query NETLAB+ disk usage.

        :return: Returns an object with two properties, **data** and **programs** . They each contain an object with the
                 following properties:

        **Properties**

        avail_b
            Available disk space in bytes.
        total_b
            Total disk space in bytes.
        used_b
            Used disk space in bytes.
        used_pct
            Disk space used as a percentage of the whole.
        """

    def system_usage_memory(self, **kwargs) -> Dict[str, Any]:
        r"""
        This method allows you to query NETLAB+ memory usage.

        :return: Returns an object with a single property, **ram**. It contains an object with the following properties:

        **Properties**

        free_b
            Free memory in bytes.
        total_b
            Total memory in bytes.
        used_b
            Used memory in bytes.
        """

    def user_account_add(self, *, com_id: int, acc_user_id: str, acc_password: str, acc_full_name: str, acc_type: netlab.enums.user.AccountType = netlab.enums.AccountType.STUDENT, acc_privs: Optional[List[Union[str, netlab.enums.user.AccountPrivileges]]] = None, acc_display_name: Optional[str] = None, acc_sort_name: Optional[str] = None, acc_email: Optional[str] = None, acc_can_login: bool = True, acc_pw_change: bool = True, cls_id: Optional[int] = None, tz_id: int = 11, date_format: netlab.enums.common.DateFormat = netlab.enums.DateFormat.ISO, time_format: netlab.enums.common.TimeFormat = netlab.enums.TimeFormat.HOUR24, first_weekday: int = 0, page_length: int = 25, **kwargs) -> int:
        r"""
        Add a user account on the NETLAB system. For accepted values see the properties documentation for
        :meth:`~netlab.api.UserApiMixin.user_account_get`.

        :param com_id: Community ID.
        :param acc_user_id: User Account ID.
        :param acc_password: Unencrypted account password.
        :param acc_full_name: Account full name.

        :param acc_type: Account type.
        :param acc_can_login: User can login. Defaults to True.
        :param acc_pw_change: Upon first login, force user to change password. Defaults to True.
        :param acc_privs: Supplemental account privileges for instructors in list or tuple
            format.
        :param acc_display_name: Account name, people will see this name in discussions, messages, and comments.
        :param acc_sort_name: Account name as it appears in sorted lists.
        :param acc_email: Account email address.
        :param cls_id: Class ID. (If you want to add user directly to a class during account creation.)
        :param tz_id: Timezone identifier. Defaults to 11.
        :param date_format: Date format preference.
        :param time_format: Time format preference.
        :param first_weekday: First day of week preference.
        :param page_length: The number of items to display in paginated lists.

        :return: On success, returns acc_id.
        """

    def user_account_get(self, *, acc_id: int, properties: Union[List[str], Literal['default', 'all']] = 'default', **kwargs) -> Dict[str, Any]:
        r"""
        Retrieves a user account on the NETLAB system.

        :param acc_id: User Account ID.
        :param properties: Properties consist of any combination of properties listed below under Properties.
                           You may also use **"all"** to include all properties, or **"default"** for a smaller subset
                           of properties.

        :return: Account data for the requested acc_id with the requested properties.

        **Properties**

        acc_can_login
            User allowed to login.
        acc_display_name
            Account name people will see this name in discussions, messages and comments.
        acc_email
            Account email.
        acc_fs_id
            Filesystem identifier of the account root folder.
        acc_full_name
            Account full name.
        acc_id
            Account identifier.
        acc_last_ip
            Last IP address of user.
        acc_last_login
            Datetime of last account login.
        acc_last_ua
            User agent string of the browser when logging in from the UI.
        acc_logins
            Number of account logins.
        acc_privs
            Supplemental account privileges for instructors only. :py:class:`AccountPrivileges`
        acc_pw_change
            Force user to change password.
        acc_session_time_started
            Datetime of session start time.
        acc_sort_name
            Account name as it appears in sorted lists.
        acc_sys
            Mark as system account.
        acc_time_created
            Datetime account was created.
        acc_time_last_access
            Datetime of last access.
        acc_type
            Account type. :py:class:`AccountType`
        acc_user_id
            Unique system-wide login identifier.
        acc_uuid
            Globally unique account ID.
        com_full_name
            Community name.
        com_id
            Unique community identifier.
        tz_iana
            Timezone IANA database identifier.
        tz_id
            Time zone identifier.
        tz_name
            Time zone name.
        acc_nlx_terms
            Lab designer terms and conditions acknowleged.
        acc_npd_terms
            Pod designer terms and conditions acknowleged.
        acc_pw_console
            Instructor's lab device console password.
        acc_pw_enable
            Instructor's lab device enable password.
        accman_list_com_id
            Persist account manager community selection in list view (admin and syswide).
        date_format
            Date format preference. :py:class:`netlab.enums.DateFormat`
        time_format
            Time format preference. :py:class:`netlab.enums.TimeFormat`
        first_weekday
            First day of week preference. An integer from 0 - 6 mapping to Sunday - Saturday.
        page_length
            The number of items to display in paginated lists. Possible values are *10, 25, 50, 100*. A value of
            *-1* will disable pagination and return all items.
        """

    def user_account_list(self, *, com_id: Optional[int] = None, acc_type: Optional[netlab.enums.user.AccountType] = None, properties: Union[List[str], Literal['default', 'all']] = 'default', **kwargs) -> List[Dict[str, Any]]:
        r"""
        Query a list of the user accounts in the NETLAB system. The list method
        is only restricted by community id and account types. The properties
        only identify those properties or fields that will be returned via
        the underlying query.

        :param com_id: Community ID
        :param acc_type: User account type.
        :param properties: Properties consist of any combination of properties listed below under Properties.
                           You may also use **"all"** to include all properties, or **"default"** for a smaller subset
                           of properties.

        :return: A list of dictionaries (a set of records) where the dictionaries contain requested properties
            per user.

        **Properties**

        acc_can_login
            User allowed to login.
        acc_display_name
            Account name people will see this name in discussions, messages and comments.
        acc_email
            Account email.
        acc_fs_id
            Filesystem identifier of the account root folder.
        acc_full_name
            Account full name.
        acc_id
            Account identifier.
        acc_last_ip
            Last IP address of user.
        acc_last_login
            Datetime of last account login.
        acc_last_ua
            User agent string of the browser when logging in from the UI.
        acc_logins
            Number of account logins.
        acc_privs
            Supplemental account privileges for instructors only. :py:class:`netlab.enums.AccountPrivileges`
        acc_pw_change
            Force user to change password.
        acc_session_time_started
            Datetime of session start time.
        acc_sort_name
            Account name as it appears in sorted lists.
        acc_sys
            Mark as system account.
        acc_time_created
            Datetime account was created.
        acc_time_last_access
            Datetime of last access.
        acc_type
            Account type. :py:class:`netlab.enums.AccountType`
        acc_user_id
            Unique system-wide login identifier.
        acc_uuid
            Globally unique account ID.
        com_id
            Unique community identifier.
        tz_id
            Time zone identifier.
        """

    def user_account_password_set(self, *, acc_id: int, new_password: str, force_reset: bool = False, **kwargs) -> Literal['OK']:
        r"""
        Sets the user account password.

        :param acc_id: Account ID.
        :param new_password: New account password.
        :param force_reset: Force user to reset password.
        """

    def user_account_remove(self, *, acc_id: int, **kwargs) -> None:
        r"""
        Removes the specified user account.

        :param acc_id: User Account ID
        """

    def user_account_search(self, *, properties: List[str] = ['acc_id'], order: Union[str, List[str], NoneType] = None, filter=None, limit: int = 100, page: Optional[int] = None, offset: Optional[int] = None, **kwargs) -> Dict[str, Any]:
        r"""
        This method queries and/or retrieves user accounts. Also see
        :meth:`~netlab.api.UserApiMixin.user_account_search_iter`.

        Filters and returns paged results of user accounts. Any property from
        :meth:`~netlab.api.UserApiMixin.user_account_list` can be filtered upon. Multiple
        **filter** will be combined using AND. Returns zero or more user accounts that match filter query.

        :param properties: Properties consist of any combination of properties listed below under Properties.
        :param order: List of properties to sort by in order of preference.
        :type order: str or list
        :param filter: Search criteria. See below for how to use filters.
        :param limit: Page size or maximum number of records returned. This method can return a maximum of 500 use
            account records. Call the method multiple times with successive page numbers to return all data.
        :param page: Starting page number (pages start at one). When page is `None`, returns only info like
            'total_records' with no accounts. A page that goes pass all records will return no accounts.
        :param offset: Starting record number. If page and offset are both None, no records are returned; only meta
            data about total users and pages are returned.

        :return: A list of user accounts that match **filter**.

        **Examples**

        Collect the account id and account user id with **acc_id** that is 100031.

            Client().user_account_search(properties=['acc_id', 'acc_user_id'], page=1, filter={'acc_id': 100031})

        Collect first page of accounts, ordered by **acc_id**.

            Client().user_account_search(properties=['acc_id', 'acc_user_id'], page=1, order='acc_id')

        Return how many users can login.

            Client().user_account_search(filter={'acc_can_login': True})['total_records']

        **Properties**

        The following properties may be used in this method. The text in bold indicates the contexts in which the
        property may be used (see contexts below). The text following the | character describes the property.

        Properties in **communities** and **timezones** must be fully qualified (i.e. `timezones.tz_name`). Properties
        starting with **accounts** my be specified without namespace (i.e. `acc_full_name` or `accounts.acc_full_name`
        may be used).

        accounts.acc_can_login
            **SELECT, FILTER, ORDER** | Logins enabled flag.

        accounts.acc_display_name
            **SELECT, FILTER, ORDER** | User display name.

        accounts.acc_email
            **SELECT, FILTER, ORDER** | Email address (RFC 2822).

        accounts.acc_full_name
            **SELECT, FILTER, ORDER** | User full name.

        accounts.acc_id
            **SELECT, FILTER, ORDER** | Local account identifier on system.

        accounts.acc_last_ip
            **SELECT, FILTER, ORDER** | Last IP address of user.

        accounts.acc_last_login
            **SELECT, FILTER, ORDER** | Timestamp of last account login.

        accounts.acc_last_ua
            **SELECT, FILTER, ORDER** | Last user agent string.

        accounts.acc_logins
            **SELECT, FILTER**        | Number of times user has logged in.

        accounts.acc_privs
            **SELECT, FILTER**        | Account privileges.

        accounts.acc_pw_change
            **SELECT, FILTER**        | Password change pending on next login.

        accounts.acc_session_time_started
            **SELECT, FILTER, ORDER** | Timestamp of session start time.

        accounts.acc_sort_name
            **SELECT, FILTER, ORDER** | User's sortable display name.

        accounts.acc_sys
            **SELECT, FILTER, ORDER** | System account flag.

        accounts.acc_time_created
            **SELECT, FILTER, ORDER** | Time account was created.

        accounts.acc_time_last_access
            **SELECT, FILTER, ORDER** | Time acocunts was last accessed.

        accounts.acc_type
            **SELECT, FILTER, ORDER** | Account type.

        accounts.acc_user_id
            **SELECT, FILTER, ORDER** | Local user ID on system.

        accounts.acc_uuid
            **SELECT, FILTER**        | Globally unique account identifier.

        accounts.com_id
            **SELECT, FILTER, ORDER** | Local community identifier on system.

        accounts.tz_id
            **SELECT, FILTER, ORDER** | Timezone identifier.

        communities.com_enabled
            **SELECT, FILTER, ORDER** | Community enabled flag.

        communities.com_full_name
            **SELECT, FILTER, ORDER** | Community name.

        communities.com_id
            **SELECT, FILTER, ORDER** | Local community identifier on system.

        communities.com_max_slots_per_res
            **SELECT, FILTER, ORDER** | Community maximum slots per reservation.

        communities.com_min_hours_btw_res
            **SELECT, FILTER, ORDER** | Community minimum hours between reservations.

        communities.com_mynetlab_news
            **SELECT, FILTER**        | Community MyNetlab page news markdown.

        communities.com_mynetlab_welcome
            **SELECT, FILTER**        | Community MyNetlab page welcome markdown.

        communities.com_tz_id
            **SELECT, FILTER, ORDER** | Timezone identifier.

        communities.com_uuid
            **SELECT, FILTER**        | Globally unique community identifier.

        timezones.tz_iana
            **SELECT, FILTER, ORDER** | Timezone IANA identifier.

        timezones.tz_id
            **SELECT, FILTER, ORDER** | Timezone identifier.

        timezones.tz_name
            **SELECT, FILTER, ORDER** | Timezone name.

        timezones.tz_sort
            **SELECT, FILTER, ORDER** | Timezone sort order.
        """

    def user_account_search_iter(self, *, properties: List[str] = ['acc_id'], order: Union[str, List[str], NoneType] = None, filter: Any = None, limit: int = 100) -> Generator[Dict[str, Any], NoneType, NoneType]:
        r"""
        This method queries and/or retrieves user accounts.

        Gets all users from server and then performs filtering locally. Any property from
        :meth:`~netlab.api.UserApiMixin.user_account_list` can be filtered upon. Multiple
        **filter** will be combined using AND. Returns zero or more user accounts that match filter query.

        :param properties: Properties consist of any combination of properties listed below under Properties.
        :param order: Sort order.
        :param filter: Search criteria. See below for how to use filters.
        :param limit: Page size collected in a single request from the server. This can be used to tune performace
            over large record sets. Maximum 500.

        :return: A series of user accounts that match **filter**. This method returns an iterator, which can be
            used in for loops like a list. See
            [the offical Python documenation](https://docs.python.org/3.6/library/stdtypes.html#iterator-types) for more
            infomation.

        **Examples**

        Collect the account id and account user id with **acc_id** that is 100031.

            Client().user_account_search_iter(properties=['acc_id', 'acc_user_id'], filter={'acc_id': 100031})

        Collect first page of accounts, ordered by **acc_id**.

            Client().user_account_search_iter(properties=['acc_id', 'acc_user_id'], order='acc_id')

        Return how many users can login.

            Client().user_account_search_iter(properties=['acc_id'], filter={'acc_can_login': True,
                                              'communities.com_id': 1})


        **Properties**

        The following properties may be used in this method. The text in bold indicates the contexts in which the
        property may be used (see contexts below). The text following the | character describes the property.

        Properties in **communities** and **timezones** must be fully qualified (i.e. `timezones.tz_name`). Properties
        starting with **accounts** my be specified without namespace (i.e. `acc_full_name` or `accounts.acc_full_name`
        may be used).

        accounts.acc_can_login
            **SELECT, FILTER, ORDER** | Logins enabled flag.

        accounts.acc_display_name
            **SELECT, FILTER, ORDER** | User display name.

        accounts.acc_email
            **SELECT, FILTER, ORDER** | Email address (RFC 2822).

        accounts.acc_full_name
            **SELECT, FILTER, ORDER** | User full name.

        accounts.acc_id
            **SELECT, FILTER, ORDER** | Local account identifier on system.

        accounts.acc_last_ip
            **SELECT, FILTER, ORDER** | Last IP address of user.

        accounts.acc_last_login
            **SELECT, FILTER, ORDER** | Timestamp of last account login.

        accounts.acc_last_ua
            **SELECT, FILTER, ORDER** | Last user agent string.

        accounts.acc_logins
            **SELECT, FILTER**        | Number of times user has logged in.

        accounts.acc_privs
            **SELECT, FILTER**        | Account privileges.

        accounts.acc_pw_change
            **SELECT, FILTER**        | Password change pending on next login.

        accounts.acc_session_time_started
            **SELECT, FILTER, ORDER** | Timestamp of session start time.

        accounts.acc_sort_name
            **SELECT, FILTER, ORDER** | User's sortable display name.

        accounts.acc_sys
            **SELECT, FILTER, ORDER** | System account flag.

        accounts.acc_time_created
            **SELECT, FILTER, ORDER** | Time account was created.

        accounts.acc_time_last_access
            **SELECT, FILTER, ORDER** | Time acocunts was last accessed.

        accounts.acc_type
            **SELECT, FILTER, ORDER** | Account type.

        accounts.acc_user_id
            **SELECT, FILTER, ORDER** | Local user ID on system.

        accounts.acc_uuid
            **SELECT, FILTER**        | Globally unique account identifier.

        accounts.com_id
            **SELECT, FILTER, ORDER** | Local community identifier on system.

        accounts.tz_id
            **SELECT, FILTER, ORDER** | Timezone identifier.

        communities.com_enabled
            **SELECT, FILTER, ORDER** | Community enabled flag.

        communities.com_full_name
            **SELECT, FILTER, ORDER** | Community name.

        communities.com_id
            **SELECT, FILTER, ORDER** | Local community identifier on system.

        communities.com_max_slots_per_res
            **SELECT, FILTER, ORDER** | Community maximum slots per reservation.

        communities.com_min_hours_btw_res
            **SELECT, FILTER, ORDER** | Community minimum hours between reservations.

        communities.com_mynetlab_news
            **SELECT, FILTER**        | Community MyNetlab page news markdown.

        communities.com_mynetlab_welcome
            **SELECT, FILTER**        | Community MyNetlab page welcome markdown.

        communities.com_tz_id
            **SELECT, FILTER, ORDER** | Timezone identifier.

        communities.com_uuid
            **SELECT, FILTER**        | Globally unique community identifier.

        timezones.tz_iana
            **SELECT, FILTER, ORDER** | Timezone IANA identifier.

        timezones.tz_id
            **SELECT, FILTER, ORDER** | Timezone identifier.

        timezones.tz_name
            **SELECT, FILTER, ORDER** | Timezone name.

        timezones.tz_sort
            **SELECT, FILTER, ORDER** | Timezone sort order.
        """

    def user_account_update(self, *, acc_id, acc_user_id=None, acc_type=None, acc_can_login=None, acc_pw_change=None, acc_password=None, acc_privs=None, acc_full_name=None, acc_display_name=None, acc_sort_name=None, acc_email=None, tz_id=None, date_format=None, time_format=None, first_weekday=None, page_length=None, **kwargs) -> Literal['OK']:
        r"""
        Update the user account. For accepted values see the properties documentation for
        :meth:`~netlab.api.UserApiMixin.user_account_get`.

        :param int acc_id: Account ID

        :param str acc_user_id: Unique system-wide login identifier.
        :param enums.AccountType acc_type: Account type.
        :param bool acc_can_login: User allowed to login.
        :param bool acc_pw_change: Force user to change password.
        :param str acc_password: Account password
        :param list[enums.AccountPrivileges] acc_privs: Supplemental account privileges for instructors in
            list or tuple format.
        :param str acc_full_name: Account full name.
        :param str acc_display_name: Account name people will see this name in discussions, messages and comments.
        :param str acc_sort_name: Account name as it appears in sorted lists.
        :param str acc_email: Account e-mail address.
        :param int tz_id: Timezone identifier.
        :param DateFormat date_format: Date format preference.
        :param TimeFormat time_format: Time format preference.
        :param int first_weekday: First day of week preference.
        :param int page_length: The number of items to display in paginated lists.
        """

    def user_community_add(self, *, com_full_name: str, com_id: int, com_enabled: bool = True, com_max_slots_per_res: Optional[int] = None, com_min_hours_btw_res: Optional[int] = None, com_mynetlab_news: Optional[str] = None, com_mynetlab_welcome: Optional[str] = None, **kwargs) -> int:
        r"""
        This method allows you to add a community to the NETLAB+ system.

        :param com_full_name: Community full name.
        :param com_id: Community identifier.
        :param com_enabled: Is community enabled.
        :param com_max_slots_per_res: Max amount of slots per reservation.
        :param com_min_hours_btw_res: Minimum hours between reservations.
        :param com_mynetlab_news: Community MyNETLAB+ news entry.
        :param com_mynetlab_welcome: Community MyNETLAB+ welcome message.

        :return: Community ID of the newly created community.
        """

    def user_community_find(self, *, com_full_name: str, **kwargs) -> Optional[int]:
        r"""
        This method allows you to find a community based on **com_full_name**.

        :param com_full_name: Community full name.

        :return: The Community ID on success.
        """

    def user_community_get(self, *, com_id: int, properties: Union[List[str], Literal['default', 'all']] = 'default', **kwargs) -> Dict[str, Any]:
        r"""
        This method allows you to retrieve a community and its properties.

        :param int com_id: Community ID.
        :param properties: Properties to return. Accepts string or list.
                        See below for all available properties. You may also use **"all"** to include all properties.
        :type properties: list[str] or 'all'

        :return: An object with the properties requested:
        :rtype: dict

        **Properties**

        com_alt_banner
            Alternate community banner.
        com_alt_banner_height
            Alternate banner height.
        com_alt_banner_width
            Alternate banner width.
        com_enabled
            Is community enabled.
        com_full_name
            Community full name.
        com_id
            Community identifier.
        com_max_slots_per_res
            Max amount of slots per reservation.
        com_min_hours_btw_res
            Minimum hours between reservations.
        com_mynetlab_news
            Community MyNETLAB+ news entry.
        com_mynetlab_welcome
            Community MyNETLAB+ welcome message.
        """

    def user_community_list(self, *, properties='default', sort_property='com_id', **kwargs):
        r"""
        Retrieve a list of communities.

        :param properties: Properties to return. Accepts string or list.
                        See below for all available properties. You may also use **"all"** to include all properties.
        :type properties: list[str] or 'all' or 'default'
        :param str sort_property: Property to sort list by. Only **com_id** (default) and **com_full_name** are
                   valid options.

        :return: A list of objects with the properties requested:
        :rtype: list[dict]

        **Properties**

        com_alt_banner
            Alternate community banner.
        com_alt_banner_height
            Alternate banner height.
        com_alt_banner_width
            Alternate banner width.
        com_enabled
            Is community enabled.
        com_full_name
            Community full name.
        com_id
            Community identifier.
        com_max_slots_per_res
            Max amount of slots per reservation.
        com_min_hours_btw_res
            Minimum hours between reservations.
        com_mynetlab_news
            Community MyNETLAB+ news entry.
        com_mynetlab_welcome
            Community MyNETLAB+ welcome message.
        """

    def user_community_remove(self, *, com_id, **kwargs) -> None:
        r"""
        This method allows you to remove a community.

        :param int com_id: Community identifier.
        """

    def user_community_update(self, *, com_id: int, com_full_name: Optional[str] = None, com_enabled: Optional[bool] = None, com_mynetlab_welcome: Optional[str] = None, com_mynetlab_news: Optional[str] = None, com_min_hours_btw_res: Optional[int] = None, com_max_slots_per_res: Optional[int] = None, com_ext_slots_per_res: Union[NoneType, int, netlab.enums.user.CommunityExtensionSlots] = None, **kwargs) -> None:
        r"""
        Update a community.

        :param int com_id: Community ID.
        :param str com_full_name: Community full name.
        :param bool com_enabled: Is community enabled.
        :param str com_mynetlab_welcome: Community MyNETLAB+ welcome message.
        :param str com_mynetlab_news: Community MyNETLAB+ news entry.
        :param int com_min_hours_btw_res: Minimum hours between reservations.
        :param int com_max_slots_per_res: Max amount of slots per reservation.
        :param com_ext_slots_per_res: Allow extensions to reservations for students and teams.
            Instructors are not restricted to this limit.
        :type com_ext_slots_per_res: int or enums.CommunityExtensionSlots
        """

    def user_logins_system_get(self, **kwargs):
        r"""
        This method allows you to query the User Logins status and number of active logins.

        :return: A dictionary with the following properties:
        :rtype: dict

        active
            Number of active users logged in.
        enabled
            User logins status.
        """

    def user_logins_system_set(self, *, enabled, logout=False, **kwargs):
        r"""
        This method allows you to enable and disable user logins.

        :param bool enabled: Enable or disable user logins.
        :param bool logout: Logout users that are already logged in.

        :return: A dictionary with the following properties:
        :rtype: dict

        changed
            Whether user login status was changed.
        logouts
            Number of users logged out.
        """

    def user_session_keepalive(self, *, acc_id, **kwargs):
        r"""
        This method performs a keepalive on a logged in user's session and
        restarts their session timeout. The last access for the session is set
        to the current time.

        :param int acc_id: Local account identifier.

        :return: A dictionary with the following properties:
        :rtype: dict

        acc_session_time_started
            Session start time, or None if the administrator specifies an
            acc_id that is not logged in.
        acc_time_last_access
            Updated last access time, or None if the administrator specifies an
            acc_id that is not logged in.
        """

    def vm_clone_task(self, *, parent_vm_id: int, parent_snapname: str, clone_role: netlab.enums.pod.VirtualMachineRole, clone_type: netlab.enums.vm.CloneType, clone_name: str, clone_datastore: Optional[str] = None, clone_storage_alloc: netlab.enums.vm.CloneStorageAllocation = netlab.enums.CloneStorageAllocation.ONDEMAND, clone_vh_id: Optional[int] = None, clone_vhg_id: Optional[int] = None, clone_comments: Optional[str] = None, copy_bios_uuid: bool = False, **kwargs) -> int:
        r"""
        Method to call a task to clone a virtual machine.

        :param parent_vm_id: Parent virtual machine identifier.
        :param parent_snapname: Parent snapshot name.
        :param clone_role: Cloned virtual machine role.
        :param clone_type: Cloned virtual machine type.
        :param clone_name: Cloned virtual machine name.
        :param clone_datastore: Datastore cloned virtual machine will reside on.
        :param clone_storage_alloc: Cloned virtual machine storage allocation.
        :param clone_vh_id: The virtual host the cloned virtual machine will reside on.
        :param clone_vhg_id: The virtual host group identifier. NOT SUPPORTED!
        :param clone_comments: Comments for the cloned virtual machine.

        :returns: Created task id
        """

    def vm_datacenter_find(self, *, vdc_name: str, **kwargs) -> Optional[int]:
        r"""
        This method allows you to find a datacenter's **vdc_id** by the datacenter name.

        :param vdc_name: VM Datacenter name.

        :return: On success, returns vdc_id. If there is no VDC matching, returns None.
        """

    def vm_datacenter_get(self, *, vdc_id: int, **kwargs) -> Dict[str, Any]:
        r"""
        This method allows you to retrieve a datacenter's information by vdc_id.

        :param vdc_id: VM Datacenter identifier.

        :return: On success, returns an object with the following properties:

        **Properties**

        vdc_agent_hostname
            Agent hostname/IP address.
        vdc_agent_password
            Agent password.
        vdc_agent_username
            Agent username.
        vdc_date_added
            Timestamp of when VDC was added to NETLAB+.
        vdc_date_tested
            Timestamp of when VDC was last tested.
        vdc_last_test_status
            Status of last VDC test.
        vdc_id
            VM Datacenter identifier.
        vdc_name
            VM Datacenter name.
        vdt_type
            VM Datacenter type.
        vdt_name
            VM Datacenter type name.
        """

    def vm_datacenter_list(self, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method allows you to retrieve all datacenters' information.

        :return: A list of objects with the following properties:

        **Properties**

        vdc_agent_hostname
            Agent hostname/IP address.
        vdc_agent_password
            Agent password.
        vdc_agent_username
            Agent username.
        vdc_date_added
            Timestamp of when VDC was added to NETLAB+.
        vdc_date_tested
            Timestamp of when VDC was last tested.
        vdc_last_test_status
            Status of last VDC test.
        vdc_id
            VM Datacenter identifier.
        vdc_name
            VM Datacenter name.
        vdt_type
            VM Datacenter type.
        vdt_name
            VM Datacenter type name.
        """

    def vm_datacenter_test(self, *, vdc_id: int, **kwargs) -> Literal['PASSED', 'FAILED']:
        r"""
        This method allows you to call a task to test communication to datacenter.

        :param vdc_id: VM Datacenter identifier.

        :return: On success returns 'PASSED', otherwise returns 'FAILED'.
        """

    def vm_host_find(self, *, vh_name: str, **kwargs) -> Optional[int]:
        r"""
        This method allows you to find a virtual host's **vh_id** by the virtual host name.

        :param vh_name: Virtual Host name.

        :return: On success, returns vh_id. If there is no matching Virtual Host, returns None.
        """

    def vm_host_get(self, *, vh_id: int, **kwargs) -> Dict[str, Any]:
        r"""
        This method allows you to retrieve a virtual host information.

        :param vh_id: Virtual host identifier.

        :return: On success, returns an object with the following properties:

        **Properties**

        vdc_id
            Agent hostname/IP address.
        vdc_name
            VM Datacenter name.
        vdt_type
            VM Datacenter type.
        vdt_name
            VM Datacenter type name.
        vh_bios_date
            Timestamp of BIOS creation date.
        vh_bios_version
            BIOS version installed.
        vh_com_path
            Virtual host communication path.
        vh_cpu_cores
            Total count of CPU cores on virtual host.
        vh_cpu_count
            Total count of physical CPUs on virtual host.
        vh_cpu_mhz
            Speed in MHz of CPU.
        vh_cpu_model
            CPU model identification.
        vh_cpu_threads
            Number of threads CPUs can handle.
        vh_date_added
            Timestamp of virtual host added to NETLAB+.
        vh_date_modified
            Timestamp of virtual host information has been modified.
        vh_date_tested
            Timestamp of virtual host test communication.
        vh_id
            Virtual host identifier.
        vh_inside_ipv4_addr
            Inside interface ipv4 address.
        vh_inside_vswitch_0
            Virtual host inside vSwitch.
        vh_last_test_status
            Status of last virtual host test communication.
        vh_memory_mb
            Total RAM in MB of virtual host.
        vh_name
            Virtual host hostname.
        vh_online
            Virtual host is online.
        vh_os_build
            Operating system build number.
        vh_os_description
            Operating system description.
        vh_os_name
            Operating system name.
        vh_os_type
            Operating system type.
        vh_os_vendor
            Operating system vender.
        vh_os_version
            Operating system version.
        vh_outside_ipv4_addr
            Outside interface ipv4 address.
        vh_pra_enabled
            Proactive resource awareness is enabled.
        vh_pra_max_cpu
            Max number of CPUs for PRA.
        vh_pra_max_mem_mb
            Max amount of RAM in MB for PRA.
        vh_pra_max_vm
            Max amount of virtual machines for PRA.
        vh_sys_model
            System model.
        vh_sys_service_tag
            System service tag.
        vh_sys_vendor
            System vendor.
        vh_uuid
            Virtual host unique global identifier.
        """

    def vm_host_list(self, *, vdc_id: Optional[str] = None, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method allows you to retrieve a list of virtual hosts information.

        :param vdc_id: VM Datacenter identifier. If not specified, will return from all datacenters.

        :return: Returns a list of objects with the following properties:

        **Properties**

        vdc_id
            Agent hostname/IP address.
        vdc_name
            VM Datacenter name.
        vdt_type
            VM Datacenter type.
        vdt_name
            VM Datacenter type name.
        vh_bios_date
            Timestamp of BIOS creation date.
        vh_bios_version
            BIOS version installed.
        vh_com_path
            Virtual host communication path.
        vh_cpu_cores
            Total count of CPU cores on virtual host.
        vh_cpu_count
            Total count of physical CPUs on virtual host.
        vh_cpu_mhz
            Speed in MHz of CPU.
        vh_cpu_model
            CPU model identification.
        vh_cpu_threads
            Number of threads CPUs can handle.
        vh_date_added
            Timestamp of virtual host added to NETLAB+.
        vh_date_modified
            Timestamp of virtual host information has been modified.
        vh_date_tested
            Timestamp of virtual host test communication.
        vh_id
            Virtual host identifier.
        vh_inside_ipv4_addr
            Inside interface ipv4 address.
        vh_inside_vswitch_0
            Virtual host inside vSwitch.
        vh_last_test_status
            Status of last virtual host test communication.
        vh_memory_mb
            Total RAM in MB of virtual host.
        vh_name
            Virtual host hostname.
        vh_online
            Virtual host is online.
        vh_os_build
            Operating system build number.
        vh_os_description
            Operating system description.
        vh_os_name
            Operating system name.
        vh_os_type
            Operating system type.
        vh_os_vendor
            Operating system vender.
        vh_os_version
            Operating system version.
        vh_outside_ipv4_addr
            Outside interface ipv4 address.
        vh_pra_enabled
            Proactive resource awareness is enabled.
        vh_pra_max_cpu
            Max number of CPUs for PRA.
        vh_pra_max_mem_mb
            Max amount of RAM in MB for PRA.
        vh_pra_max_vm
            Max amount of virtual machines for PRA.
        vh_sys_model
            System model.
        vh_sys_service_tag
            System service tag.
        vh_sys_vendor
            System vendor.
        vh_uuid
            Virtual host unique global identifier.
        """

    def vm_host_perf_realtime_list(self, *, vh_id: Optional[List[int]] = None, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method returns real-time virtual machine host performance data for one or more hosts.

        :params vh_id: NETLAB+ host identifier of hosts to return. If omitted or empty, all
            hosts are returned.
        :returns: A dictionary with the following properties.

        **Recommended Usage**

        1. Obtain a list of hosts systems from vm.host.list.
        2. Call this method to obtain real-time performance data for one or more hosts. You
           may optionally specify which hosts to return by passing an array or CSV list of
           host IDs; long running applications that specify vh_id should always be prepared
           to handle this exception in case a host host is deleted.
        3. Real-time data is available every 20 seconds with observations for T+00, T+20, and
           T+40 seconds of every minute. For optimal results, call this method at T+05, T+25,
           and T+45 seconds; calling system should have accurate system clock (i.e. NTP). To
           avoid unnecessary overhead on the NETLAB+ server API, calls to this method should
           be at least 20 seconds apart.

        **Properties**

        vh_id
            The NETLAB+ host identifier of the associated host.
        data_available
            real-time performance properties are available for this host.
        vhp_time
            The ending date and time (UTC) of the performance interval (UTC).
        age_sec
            The age of the data in second from time of call. If greater than 60, data will
            be considered too stale to be real-time, and data_available will be 0. If None,
            no data was available for host, data_available will be 0 and vhp_time will be None.

        """

    def vm_inventory_add(self, *, vdc_id, vm_uuid, vm_name, vm_path=None, vm_alloc_mem_mb, vm_alloc_cpu_n, vhg_id=None, vh_id=None, vm_role=netlab.enums.VirtualMachineRole.NORMAL, vm_comments=None, vm_vendor_os_id=None, vm_vendor_os_name=None, vm_netlab_os_id=None, vm_parent_id=None, vm_parent_snapname=None, **kwargs) -> List[Dict[str, Any]]:
        r"""
        *``vm_inventory_add`` is deprecated, please use ``vm_inventory_import_task`` instead*

        Add virtual machines to NETLAB+ inventory.

        :param int vdc_id: VM Datacenter identifier.
        :param int vhg_id: Virtual host group identifier.
        :param int vh_id: Virtual host identifier.
        :param str vm_uuid: Virtual machine unique identifier.
        :param str vm_name: Virtual machine name.
        :param str vm_path: Virtual machine path on datastore.
        :param netlab.enums.VirtualMachineRole vm_role: Virtual machine role in NETLAB+ inventory.
        :param int vm_alloc_mem_mb: Total amount of allocated RAM.
        :param int vm_alloc_cpu_n: Total amount of allocated CPUs.
        :param str vm_comments: Virtual machine comments from VMX.
        :param str vm_vendor_os_id: Vendor operating system identifier.
        :param str vm_vendor_os_name: Vendor operating system name.
        :param str vm_netlab_os_id: NETLAB+ match to vm_vendor_os_id.
        :param int vm_parent_id: Virtual machine parent identifier, if VM is a link clone.
        :param str vm_parent_snapname: Virtual machine parent snapname, if VM is a link clone.

        :return: Returns a list of object with the following properties:
        :rtype: list[dict]

        **properties**

        vm_id
            Virtual machine identifier.
        """

    def vm_inventory_get(self, *, vm_id: int, **kwargs) -> Dict[str, Any]:
        r"""
        This method allows you to retrieve one or more virtual machines from NETLAB+ inventory.

        :param vm_id: Virtual machine identifier.

        :return: Returns an object with the following properties:

        **Properties**

        pc_id
            Remote pc identifier.
        pc_label
            Remote pc label.
        pc_os_id
            NETLAB+ operating system identifier.
        pc_os_name
            NETLAB+ operating system name.
        pc_pod_id
            If attached to a pod, pod identifier.
        pc_vm_id
            Virtual machine identifier.
        pod_name
            Pod name.
        vdc_id
            Virtual datacenter identifier.
        vdc_name
            Virtual datacenter name.
        vh_id
            Virtual host identifier.
        vh_name
            Virtual host name.
        vhg_id
            Virtual host group identifier.
        vhg_name
            Virtual host group name.
        vm_alloc_cpu_n
            Total amount of allocated CPUs.
        vm_alloc_mem_mb
            Total amount of allocated RAM.
        vm_child_count
            Total count of children VMs.
        vm_comments
            Virtual machine comments from VMX.
        vm_date_added
            Timestamp of virtual machine added to NETLAB+ inventory.
        vm_id
            Virtual machine identifier.
        vm_name
            Virtual machine name.
        vm_netlab_os_id
            NETLAB+ match to vm_vendor_os_id.
        vm_parent_id
            Virtual machine parent identifier, if VM is a link clone.
        vm_parent_name
            Virtual machine parent name.
        vm_parent_role
            Parent virtual machine role.
        vm_parent_snapname
            Virtual machine parent snapname, if VM is a link clone.
        vm_path
            Virtual machine path on datastore.
        vm_power_state
            Virtual machine power state.
        vm_role
            Virtual machine role in NETLAB+ inventory.
        vm_snapshot
            This is what the VM reverts to when the pod is reset. You can take multiple snapshots with the same name,
            without having to update this field. Update this field with a call to
            :meth:`~netlab.api.PodApiMixin.pod_pc_update`
        vm_uuid
            Virtual machine unique identifier.
        vm_vendor_os_id
            Vendor operating system identifier.
        vm_vendor_os_name
            Vendor operating system name.

        """

    def vm_inventory_import_task(self, *, vdc_id: int, vm_property_list: List[Dict[str, Any]], **kwargs) -> List[Dict[str, Any]]:
        r"""
        Method to call a task to import virtual machine into NETLAB+ inventory.

        :param int vdc_id: Virtual datacenter identifier.
        :param list vm_property_list: Virtual machine property list of the following properties:

        **properties**

        vm_uuid
            Virtual machine unique identifier.
        vhg_id
            Virtual host group identifier.
        vh_id
            Virtual host identifier.
        vm_name
            Virtual machine name.
        vm_role
            Virtual machine role in NETLAB+ inventory. :py:class:`netlab.enums.VirtualMachineRole`
        vm_alloc_mem_mb
            Total amount of allocated RAM.
        vm_alloc_cpu_n
            Total amount of allocated CPUs.
        vm_comments
            Virtual machine comments from VMX.
        vm_vendor_os_id
            Vendor operating system identifier.
        vm_vendor_os_name
            Vendor operating system name.
        vm_netlab_os_id
            NETLAB+ match to `vm_vendor_os_id`.

        :return: List of results

        **return properties**

        status
            'OK' or error.
        vm_id
            Virtual machine identifier.
        """

    def vm_inventory_list(self, *, vdc_id: Optional[int] = None, roles: Optional[List[str]] = None, attached: Optional[bool] = None, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method allows you to list the virtual machines from NETLAB+ inventory.

        :param vdc_id: VM Datacenter identifier.
        :param roles: Filter by specified roles.
        :param attached: List virtual machines attached to a pod.


        :return: Returns an object with the following properties:

        **Properties**

        pc_id
            Remote pc identifier.
        pc_label
            Remote pc label.
        pc_os_id
            NETLAB+ operating system identifier.
        pc_os_name
            NETLAB+ operating system name.
        pc_pod_id
            If attached to a pod, pod identifier.
        pc_vm_id
            Virtual machine identifier.
        pod_name
            Pod name.
        vdc_id
            Virtual datacenter identifier.
        vdc_name
            Virtual datacenter name.
        vh_id
            Virtual host identifier.
        vh_name
            Virtual host name.
        vhg_id
            Virtual host group identifier.
        vhg_name
            Virtual host group name.
        vm_alloc_cpu_n
            Total amount of allocated CPUs.
        vm_alloc_mem_mb
            Total amount of allocated RAM.
        vm_child_count
            Total count of children VMs.
        vm_comments
            Virtual machine comments from VMX.
        vm_date_added
            Timestamp of virtual machine added to NETLAB+ inventory.
        vm_id
            Virtual machine identifier.
        vm_name
            Virtual machine name.
        vm_netlab_os_id
            NETLAB+ match to vm_vendor_os_id.
        vm_parent_id
            Virtual machine parent identifier, if VM is a link clone.
        vm_parent_name
            Virtual machine parent name.
        vm_parent_role
            Parent virtual machine role.
        vm_parent_snapname
            Virtual machine parent snapname, if VM is a link clone.
        vm_path
            Virtual machine path on datastore.
        vm_power_state
            Virtual machine power state.
        vm_role
            Virtual machine role in NETLAB+ inventory.
        vm_snapshot
            This is what the VM reverts to when the pod is reset. You can take multiple snapshots with the same name,
            without having to update this field. Update this field with a call to
            :meth:`~netlab.api.PodApiMixin.pod_pc_update`
        vm_uuid
            Virtual machine unique identifier.
        vm_vendor_os_id
            Vendor operating system identifier.
        vm_vendor_os_name
            Vendor operating system name.
        """

    def vm_inventory_remove_datacenter_task(self, *, vm_id: int, **kwargs) -> None:
        r"""
        Remove virtual machine from NETLAB+ inventory and datacenter.
        Does NOT remove VM from disk.

        :param int vm_id: Virtual machine identifier.
        """

    def vm_inventory_remove_disk_task(self, *, vm_id: int, **kwargs) -> None:
        r"""
        Remove virtual machine from NETLAB+ inventory, datacenter, and disk.

        **WARNING: this method permanantly deletes the virtual machine files
        from disk.  This operation cannot be undone.**

        :param vm_id: Virtual machine identifier.
        """

    def vm_inventory_remove_local(self, *, vm_id, **kwargs) -> None:
        r"""
        Remove virtual machine from NETLAB+ inventory only.
        Does NOT remove VM from datacenter or disk.

        :param vm_id: Virtual machine identifier.
        """

    def vm_license_list(self, *, vdc_id: Optional[int] = None, vh_id: Optional[int] = None, vl_server: Optional[int] = None, vl_key: Optional[int] = None, vl_type: Optional[netlab.enums.vm.VirtualMachineLicenseType] = None, **kwargs) -> List[Dict[str, Any]]:
        r"""
        This method returns a list of cached VMware vCenter and server licenses.

        This license cache is populated by any of the following events:
        - every 12 hours per scheduled task
        - when datacenters are added or removed
        - when virtual machine host servers are added or removed
        - by calling API method :py:meth:`VmApiMixin.vm_license_update_task`

        The cache updates each time licenses are scanned.  If a vCenter server for a datacenter is
        unreachable during the scan, the licenses managed by that vCenter will be missing from the
        cache until the vCenter can be reached on a subsequent scan.

        :param vdc_id: return licenses for datacenter identified by **vdc_id** in NETLAB+
        :param vh_id: return license for vm host identified by **vh_id** in NETLAB+
        :param vl_server: return license with hostname or IP address matching **vl_server** in vCenter
        :param vl_key: return license with key matching **vl_key** in vCenter
        :param vl_type: License type.

        :returns: A list of dictionaries with the following properties.

        **Properties**

        vdc_id
            NETLAB+ datacenter identifier associated with license.
        vh_id
            If not `None`, the NETLAB+ vm host identifier associated with license.
        vl_type
            License type. :py:class:`netlab.enums.VirtualMachineLicenseType`
        vl_server
            Hostname or IP address of the server as registered in vCenter.
        vl_product
            Licensed product name.
        vl_key
            Licnese key.
        vl_units
            Number of units licensed (i.e. processors) depending on server type.
        vl_expiration
            The expiration date and time of the license (UTC) or `None` if no expiration.
        vl_last_udpate
            The date and time this license was last queried and cached.
        """

    def vm_license_update_task(self, **kwargs) -> Dict[str, Any]:
        r"""
        This method scans each vCenter server in all NETLAB+ datacenters and returns the VMware
        license status of VMware vCenter and VMware host servers.

        * The license information is cached for quick retreival using subsequent calls to
          :py:meth:`VmApiMixin.vm_license_list`.

        * It is usually not necessary to call vm.liense.update.task directly.  It is automatically run:
            - every 12 hours per scheduled task
            - when datacenters are added or removed
            - when virtual machine host servers are added or removed

        * The license cache is cleared updated each time vm.license.udpate.task is run.
            - If a vCenter server for a datacenter is unreachable during the scan, the licenses
              managed by that vCenter will be missing from the cache until the vCenter can be
              reached on a subsequent scan.

        * This task ignores licenses that are not associated with NETLAB+ servers.

        :returns: A dictionary with the following properties.

        **Properties**

        servers_tried
            The number of vCenter servers that contact was attempted.
        servers_reporting
            The number of vCenter servers that responded with license information.
        license_count
            The number of licenses that were found and cached.
        licenses
            Information about each licence (see below).
        earliest_expiration
            The earliest license expiration at time of call. Can be `None`.

        **License Properties**

        vdc_id
            NETLAB+ datacenter identifier associated with license.
        vh_id
            If not `None`, the NETLAB+ vm host identifier associated with license.
        vl_type
            License type. :py:class:`netlab.enums.VirtualMachineLicenseType`
        vl_server
            Hostname or IP address of the server as registered in vCenter.
        vl_product
            Licensed product name.
        vl_key
            Licnese key.
        vl_units
            Number of units licensed (i.e. processors) depending on server type.
        vl_expiration
            The expiration date and time of the license (UTC) or `None` if no expiration.
        vl_last_udpate
            The date and time this license was last queried and cached.
        """

    def vm_snapshot_add(self, *, vm_id: Optional[int] = None, pc_id: Optional[int] = None, snapshot_name: str, dump_memory: bool = False, sync: bool = False, description: Optional[str] = None, **kwargs) -> None:
        r"""
        Method to call a task to add snapshot to virtual machine.

        :param vm_id: Virtual datacenter identifier.
        :param pc_id: Remote pc identifier.
        :param snapshot_name: Name of snapshot to take.
        :param dump_memory: Dump memory files.
        :param sync: Sync files.
        :param description: Snapshot description.
        """

    def vm_snapshot_edit(self, *, vm_id: Optional[int] = None, pc_id: Optional[int] = None, snapshot_id: Optional[int] = None, new_snapshot_name: Optional[str] = None, new_snapshot_description: Optional[str] = None, **kwargs) -> None:
        r"""
        Method to call a task to edit a snapshot.

        :param vm_id: Virtual datacenter identifier.
        :param pc_id: Remote pc identifier.
        :param snapshot_id: Snapshot identifier.
        :param new_snapshot_name: New name of snapshot to take.
        :param new_snapshot_description: New description of snapshot.
        """

    def vm_snapshot_get_list(self, *, vm_id: Optional[int] = None, pc_id: Optional[int] = None, **kwargs) -> Dict[str, Any]:
        r"""
        Method to call a task to retrieve a list of snapshots.

        :param vm_id: Virtual datacenter identifier.
        :param pc_id: Remote pc identifier.

        :return: Returns a dict with the following properties:

        **Properties**

        current_snapshot
            The current snapshot. See *Snapshot properties* for more info.
        snapshot_list
            A list of all snapshots. See *Snapshot properties* for more info.

        **Snapshot properties**

        power_state
            The state of the snapshot. :py:class:`PowerState`
        name
            The snapshot name.
        description
            The snapshot description.
        parent_id
            The id of the snapshot parent.
        id
            The snapshot id.
        mo_ref
            The unique identifier of the managed object in vSphere.
        """

    def vm_snapshot_get_tree(self, *, vm_id: Optional[int] = None, pc_id: Optional[int] = None, **kwargs) -> Dict[str, Any]:
        r"""
        Method to call a task to retrieve snapshot tree.

        :param vm_id: Virtual datacenter identifier.
        :param pc_id: Remote pc identifier.

        :return: Returns a dict with the following properties:

        **Properties**

        current_snapshot
            The current snapshot. See *Snapshot properties* for more info.
        snapshot_list
            A list of all snapshots. See *Snapshot properties* for more info.

        **Snapshot properties**

        power_state
            The state of the snapshot. :py:class:`PowerState`
        name
            The snapshot name.
        description
            The snapshot description.
        id
            The snapshot id.
        mo_ref
            The unique identifier of the managed object in vSphere.
        """

    def vm_snapshot_remove(self, *, vm_id: Optional[int] = None, pc_id: Optional[int] = None, snapshot_name: Optional[str] = None, snapshot_id: Optional[int] = None, remove_children: Optional[bool] = None, remove_all_snapshots: Optional[bool] = None, **kwargs) -> None:
        r"""
        Method to call a task to remove snapshot from virtual machine.

        :param vm_id: Virtual datacenter identifier.
        :param pc_id: Remote pc identifier.
        :param snapshot_name: Name of snapshot to take.
        :param snapshot_id: Snapshot identifier.
        :param remove_children: Remove children snapshots.
        :param remove_all_snapshots: Remove all snapshots of virtual machine.
        """

    def vm_snapshot_revert(self, *, vm_id: Optional[int] = None, pc_id: Optional[int] = None, snapshot_name: Optional[str] = None, snapshot_id: Optional[int] = None, **kwargs) -> None:
        r"""
        Method to call a task to revert to snapshot from virtual machine.

        :param vm_id: Virtual datacenter identifier.
        :param pc_id: Remote pc identifier.
        :param snapshot_name: Name of snapshot to take.
        :param snapshot_id: Snapshot identifier.
        """



    def __init__(self, system: str = 'default', config: Union[NoneType, netlab.config.NetlabServerConfig, Dict[str, Any]] = None, config_path: Optional[str] = None):
        r"""
        :param system: The name to identify a NETLAB+ system. Defaults to **'default'**.
        :param config: Configuration options. See below for all possible options for the :attr:`config`.
        :param config_path: File path location of a JSON config file to be used instead of the default location.
        """

    def disconnect(self) -> None:
        r"""
        Disconnect from NETLAB+.
        """

