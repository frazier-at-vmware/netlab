from datetime import date
from typing import Optional, List, Any, Union, Dict, cast
from typing_extensions import Literal

from .. import enums
from ._client_protocol import ClientProtocol


class ClassApiMixin(ClientProtocol):
    "Methods for working with classes."

    class_default_props = ['cls_id', 'cls_name', 'com_id']
    class_props = ['cls_change_ex', 'cls_def_pw_account', 'cls_def_pw_console', 'cls_def_pw_enable',
                   'cls_email_logs', 'cls_end_date', 'cls_id', 'cls_lab_limit', 'cls_max_slots_per_res',
                   'cls_min_hours_btw_res', 'cls_name', 'cls_no_delete', 'cls_retain_ilt', 'cls_retain_period',
                   'cls_retain_st', 'cls_self_sched', 'cls_start_date', 'cls_team_sched', 'cls_uuid', 'com_id',
                   'enrollment', 'leads']

    roster_default_props = ['acc_id', 'acc_user_id', 'acc_email', 'lead']
    roster_props = ['acc_display_name', 'acc_email', 'acc_full_name', 'acc_id', 'acc_last_login', 'acc_logins',
                    'acc_sort_name', 'acc_time_last_access', 'acc_type', 'acc_user_id', 'cls_id', 'lead', 'ros_team']

    async def class_list(
                self,
                *,
                com_id: Optional[int] = None,
                member: bool = False,
                properties: Union[List[str], Literal['default', 'all']] = "default",
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
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
        method = "class.list"
        if properties == 'all':
            properties = self.class_props
        if properties == 'default':
            properties = self.class_default_props
        return await self.call(method, com_id=com_id, member=member, properties=properties, **kwargs)

    async def class_add(
                self,
                *,
                cls_name: str,
                com_id: int,
                cls_change_ex: bool = True,
                cls_def_pw_account: Optional[str] = None,
                cls_def_pw_console: Optional[str] = None,
                cls_def_pw_enable: Optional[str] = None,
                cls_email_logs: enums.ClassEmailLogs = enums.ClassEmailLogs.NO,
                cls_end_date: Optional[date] = None,
                cls_lab_limit: enums.ClassLabLimit = enums.ClassLabLimit.ENFORCE,
                cls_max_slots_per_res: Optional[int] = None,
                cls_min_hours_btw_res: Optional[int] = None,
                cls_no_delete: bool = False,
                cls_retain_ilt: bool = False,
                cls_retain_period: Optional[date] = None,
                cls_retain_st: bool = True,
                cls_self_sched: bool = True,
                cls_start_date: Optional[date] = None,
                cls_team_sched: bool = False,
                **kwargs
            ) -> int:
        """
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

        method = "class.add"
        params = {'cls_name': cls_name, 'com_id': com_id, 'cls_change_ex': cls_change_ex,
                  'cls_email_logs': cls_email_logs, 'cls_lab_limit': cls_lab_limit, 'cls_no_delete': cls_no_delete,
                  'cls_retain_ilt': cls_retain_ilt, 'cls_retain_st': cls_retain_st, 'cls_self_sched': cls_self_sched,
                  'cls_team_sched': cls_team_sched}

        if cls_def_pw_account:
            params['cls_def_pw_account'] = cls_def_pw_account
        if cls_def_pw_console:
            params['cls_def_pw_console'] = cls_def_pw_console
        if cls_def_pw_enable:
            params['cls_def_pw_enable'] = cls_def_pw_enable

        if cls_start_date:
            params['cls_start_date'] = cls_start_date
        if cls_end_date:
            params['cls_end_date'] = cls_end_date

        if cls_max_slots_per_res:
            params['cls_max_slots_per_res'] = cls_max_slots_per_res
        if cls_min_hours_btw_res:
            params['cls_min_hours_btw_res'] = cls_min_hours_btw_res

        if cls_retain_period:
            params['cls_retain_period'] = cls_retain_period

        params.update(kwargs)
        return int(await self.call(method, **params))

    async def class_get(
                self,
                *,
                cls_id: int,
                properties: Union[List[str], Literal['all', 'default']] = "default",
                **kwargs
            ) -> Dict[str, Any]:
        """
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

        method = "class.get"
        if properties == 'all':
            properties = self.class_props
        if properties == 'default':
            properties = self.class_default_props
        return await self.call(method, cls_id=cls_id, properties=properties, **kwargs)

    async def class_update(
                self,
                *,
                cls_id: int,
                cls_change_ex: Optional[bool] = None,
                cls_def_pw_account: Optional[str] = None,
                cls_def_pw_console: Optional[str] = None,
                cls_def_pw_enable: Optional[str] = None,
                cls_email_logs: Optional[enums.ClassEmailLogs] = None,
                cls_end_date: Optional[date] = None,
                cls_lab_limit: Optional[enums.ClassLabLimit] = None,
                cls_max_slots_per_res: Optional[int] = None,
                cls_min_hours_btw_res: Optional[int] = None,
                cls_name: Optional[str] = None,
                cls_no_delete: Optional[bool] = None,
                cls_retain_ilt: Optional[bool] = None,
                cls_retain_period: Optional[int] = None,
                cls_retain_st: Optional[bool] = None,
                cls_self_sched: Optional[bool] = None,
                cls_start_date: Optional[date] = None,
                cls_team_sched: Optional[bool] = None,
                cls_ext_slots_per_res: Optional[Union[int, enums.ClassExtensionSlots]] = None,
                **kwargs
            ) -> Literal["OK"]:
        """
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

        method = "class.update"
        params: Dict[str, Any] = {'cls_id': cls_id}

        if cls_name:
            params['cls_name'] = cls_name
        if cls_start_date:
            params['cls_start_date'] = cls_start_date
        if cls_end_date:
            params['cls_end_date'] = cls_end_date
        if cls_def_pw_account:
            params['cls_def_pw_account'] = cls_def_pw_account
        if cls_def_pw_console:
            params['cls_def_pw_console'] = cls_def_pw_console
        if cls_def_pw_enable:
            params['cls_def_pw_enable'] = cls_def_pw_enable
        if cls_email_logs:
            params['cls_email_logs'] = cls_email_logs
        if cls_lab_limit:
            params['cls_lab_limit'] = cls_lab_limit
        if cls_no_delete is not None:
            params['cls_no_delete'] = cls_no_delete
        if cls_retain_ilt is not None:
            params['cls_retain_ilt'] = cls_retain_ilt
        if cls_retain_st is not None:
            params['cls_retain_st'] = cls_retain_st
        if cls_retain_period:
            params['cls_retain_period'] = cls_retain_period
        if cls_self_sched is not None:
            params['cls_self_sched'] = cls_self_sched
        if cls_team_sched is not None:
            params['cls_team_sched'] = cls_team_sched
        if cls_change_ex is not None:
            params['cls_change_ex'] = cls_change_ex
        if cls_min_hours_btw_res:
            params['cls_min_hours_btw_res'] = cls_min_hours_btw_res
        if cls_max_slots_per_res:
            params['cls_max_slots_per_res'] = cls_max_slots_per_res
        if cls_ext_slots_per_res is not None:
            params['cls_ext_slots_per_res'] = cls_ext_slots_per_res

        params.update(kwargs)
        return await self.call(method, **params)

    async def class_remove(
                self,
                *,
                cls_id: int,
                delete_students: bool = False,
                **kwargs
            ) -> None:
        """
        This method removes a class from the NETLAB+ system.

        :param cls_id: Local system class.
        :param delete_students: `False` Do not delete student accounts. `True` Delete student accounts
            that are exclusively in this class. Student accounts that are members of multiple classes are not deleted.
        """

        method = "class.remove"
        return await self.call(method, cls_id=cls_id, delete_students=delete_students, **kwargs)

    async def class_roster_add(
                self,
                *,
                acc_id: str,
                cls_id: str,
                lead: bool = False,
                ros_team: Optional[str] = None,
                **kwargs
            ) -> Literal["OK"]:
        """
        This method allows you to add a member to a class roster.

        :param acc_id: Unique account identifier.
        :param cls_id: Unique class identifier.
        :param lead: Add as lead.
        :param ros_team: Assign user to a team. Single character, A-Z.
        """

        method = "class.roster.add"
        params = {'acc_id': acc_id, 'cls_id': cls_id, 'lead': lead}

        if ros_team:
            params['ros_team'] = ros_team

        params.update(kwargs)
        return await self.call(method, **params)

    async def class_roster_list(
                self,
                *,
                cls_id: int,
                leads: bool = False,
                **kwargs
            ):
        """
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

        method = "class.roster.list"
        return await self.call(method, cls_id=cls_id, leads=leads, **kwargs)

    async def class_roster_remove(
                self,
                *,
                acc_id: int,
                cls_id: str,
                **kwargs
            ) -> None:
        """
        This method removes a user from the class roster.

        :param acc_id: Account identifier of user to be removed.
        :param cls_id: Unique class identifier.
        """

        method = "class.roster.remove"
        return await self.call(method, acc_id=acc_id, cls_id=cls_id, **kwargs)

    async def class_roster_get(
                self,
                *,
                cls_id: int,
                acc_id: Optional[int],
                **kwargs,
            ) -> Dict[str, Any]:
        """
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
        method = 'class.roster.get'

        return await self.call(method, acc_id=acc_id, cls_id=cls_id, **kwargs)

    async def class_roster_team_update(
                self,
                *,
                cls_id: int,
                ros_team: Optional[str] = None,
                roster_acc_id: List[int],
                **kwargs,
            ) -> str:
        """
        This method will create and update teams (groups of students) for a given class roster.

        :param cls_id: Local system class identifier.
        :param ros_team: A single uppercase letter [A,Z] as the designation of the team to add
            the student(s) to. If this value is `None`, the student(s) are assigned to no team
            (unassigned).
        :param roster_acc_id: A list of account IDs to assign to the specified team.
        """

        method = 'class.roster.team.update'

        acc_id_csv = ','.join(map(str, roster_acc_id))

        return await self.call(method, cls_id=cls_id, ros_team=ros_team, roster_acc_id=acc_id_csv, **kwargs)

    async def class_content_add(
        self,
        *,
        cls_id: int,
        con_id: str,
        **kwargs,
    ) -> None:
        """
        This method allows you to add content to a class.

        :param cls_id: Class identifier.
        :param con_id: Content identifier.
        """

        method = "class.content.add"
        return await self.call(
            method,
            cls_id=cls_id,
            con_id=con_id,
            **kwargs,
        )

    async def class_content_availability(
        self,
        *,
        cls_id: int,
        **kwargs,
    ) -> List[Dict[str, Any]]:
        """
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
        method = "class.content.availability"

        return await self.call(
            method,
            cls_id=cls_id,
            **kwargs,
        )

    async def class_content_list(
        self,
        *,
        cls_id: int,
        properties: Union[Literal['all'], List[str]] = 'all',
        **kwargs,
    ) -> List[Dict[str, Any]]:
        """
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
        method = "class.content.list"

        if properties == 'all':
            properties = cast(Literal['all'], None)

        return await self.call(
            method,
            cls_id=cls_id,
            properties=properties,
            **kwargs,
        )

    async def class_content_remove(
        self,
        *,
        cls_id: int,
        con_id: str,
        **kwargs,
    ) -> None:
        """
        This method removes content from a class.

        :param cls_id: Class identifier.
        :param con_id: Content identifier.
        """
        method = "class.content.remove"

        return await self.call(
            method,
            cls_id=cls_id,
            con_id=con_id,
            **kwargs,
        )
