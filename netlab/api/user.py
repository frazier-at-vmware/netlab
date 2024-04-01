from typing import Optional, List, Dict, Any, Union, AsyncGenerator
from typing_extensions import Literal

from .. import enums
from ..utils import minimum_version
from ._client_protocol import ClientProtocol


class UserApiMixin(ClientProtocol):
    user_account_default_props = ['acc_id', 'acc_user_id', 'acc_email', 'acc_type']
    user_account_list_props = ['acc_can_login', 'acc_display_name', 'acc_email', 'acc_full_name', 'acc_id',
                               'acc_last_ip', 'acc_last_login', 'acc_last_ua',
                               'acc_logins', 'acc_privs', 'acc_pw_change', 'acc_session_time_started', 'acc_sort_name',
                               'acc_sys', 'acc_time_created', 'acc_time_last_access', 'acc_type', 'acc_user_id',
                               'acc_uuid', 'com_id', 'tz_id']
    user_account_get_props = user_account_list_props + ['com_full_name', 'tz_iana', 'tz_name', 'acc_nlx_terms',
                                                        'acc_npd_terms', 'acc_pw_console', 'acc_pw_enable',
                                                        'accman_list_com_id', 'date_format', 'time_format',
                                                        'first_weekday', 'page_length']

    user_account_privs = ['COMWIDE', 'SYSWIDE', 'POD_DESIGNER', 'LAB_DESIGNER']

    community_default_props = ['com_id', 'com_full_name']
    community_props = ['com_alt_banner', 'com_alt_banner_height', 'com_alt_banner_width', 'com_enabled',
                       'com_full_name', 'com_id', 'com_max_slots_per_res', 'com_min_hours_btw_res',
                       'com_mynetlab_news', 'com_mynetlab_welcome']

    async def user_account_list(
                self,
                *,
                com_id: Optional[int] = None,
                acc_type: Optional[enums.AccountType] = None,
                properties: Union[List[str], Literal['all', 'default']] = "default",
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
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

        if properties == 'all':
            properties = self.user_account_list_props
        if properties == 'default':
            properties = self.user_account_default_props

        filters: Dict[str, Any] = {}
        if com_id is not None:
            filters['com_id'] = com_id
        if acc_type is not None:
            filters['acc_type'] = acc_type

        result = []

        async for user in self.user_account_search_iter(properties=properties, filter=filters, limit=500):
            result.append(user)
        return result

    @minimum_version('17.1.4')
    async def user_account_search_iter(
                self,
                *,
                properties: List[str] = ['acc_id'],
                order: Optional[Union[str, List[str]]] = None,
                filter: Any = None,  # TODO
                limit: int = 100,
            ) -> AsyncGenerator[Dict[str, Any], None]:
        """
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

        total_pages = 1
        current_page = 1
        acc_ids = set()

        while current_page <= total_pages:
            data = await self.user_account_search(
                page=current_page,
                properties=properties,
                order=order,
                filter=filter,
                limit=limit,
            )
            current_page += 1
            total_pages = data['total_pages']
            for record in data['data']:
                acc_id = record['acc_id']
                if acc_id not in acc_ids:
                    acc_ids.add(acc_id)
                    yield record

    @minimum_version('17.1.4')
    async def user_account_search(
                self,
                *,
                properties: List[str] = ['acc_id'],
                order: Optional[Union[str, List[str]]] = None,
                filter=None,  # TODO
                limit: int = 100,
                page: Optional[int] = None,
                offset: Optional[int] = None,
                **kwargs
            ) -> Dict[str, Any]:
        """
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
        # Netlab does not understand bool; json.dumps(default) is not called for bools, only on
        # non-json-native objects.
        new_filter: Optional[Dict[str, Any]]
        if filter is None:
            new_filter = None
        else:
            new_filter = {}
            for k, v in filter.items():
                if isinstance(v, bool):
                    new_filter[k] = int(v)
                else:
                    new_filter[k] = v

        return await self.call(
            'user.account.search.task', properties=properties, order=order, filter=new_filter,
            limit=limit, page=page, offset=offset, **kwargs)

    async def user_account_get(
                self,
                *,
                acc_id: int,
                properties: Union[List[str], Literal['all', 'default']] = 'default',
                **kwargs
            ) -> Dict[str, Any]:
        """
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
        method = 'user.account.get'

        if properties == 'all':
            properties = self.user_account_get_props
        if properties == 'default':
            properties = self.user_account_default_props

        return await self.call(method, acc_id=acc_id, properties=properties, **kwargs)

    async def user_account_add(
                self,
                *,
                com_id: int,
                acc_user_id: str,
                acc_password: str,
                acc_full_name: str,
                acc_type: enums.AccountType = enums.AccountType.STUDENT,
                acc_privs: Optional[List[Union[str, enums.AccountPrivileges]]] = None,
                acc_display_name: Optional[str] = None,
                acc_sort_name: Optional[str] = None,
                acc_email: Optional[str] = None,
                acc_can_login: bool = True,
                acc_pw_change: bool = True,
                cls_id: Optional[int] = None,
                tz_id: int = 11,
                date_format: enums.DateFormat = enums.DateFormat.ISO,
                time_format: enums.TimeFormat = enums.TimeFormat.HOUR24,
                first_weekday: int = 0,
                page_length: int = 25,
                **kwargs
            ) -> int:
        """
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

        method = "user.account.add"
        params = {
            'com_id': com_id,
            'acc_user_id': acc_user_id,
            'acc_password': acc_password,
            'acc_full_name': acc_full_name,
            'acc_type': acc_type,
            'acc_can_login': acc_can_login,
            'acc_pw_change': acc_pw_change,
            'tz_id': tz_id,
            'date_format': date_format,
            'time_format': time_format,
            'first_weekday': first_weekday,
            'page_length': page_length
        }

        if acc_privs:
            acc_privs_str: List[str] = []
            for acc in acc_privs:
                if isinstance(acc, str):
                    acc_privs_str.append(acc)
                else:
                    acc_privs_str.append(acc.value)
            params['acc_privs'] = ','.join(acc_privs_str).upper()
        if acc_display_name:
            params['acc_display_name'] = acc_display_name
        if acc_sort_name:
            params['acc_sort_name'] = acc_sort_name
        if acc_email:
            params['acc_email'] = acc_email
        if cls_id:
            params['cls_id'] = cls_id

        params.update(kwargs)
        return int(await self.call(method, **params))

    async def user_account_password_set(
                self,
                *,
                acc_id: int,
                new_password: str,
                force_reset: bool = False,
                **kwargs
            ) -> Literal["OK"]:
        """
        Sets the user account password.

        :param acc_id: Account ID.
        :param new_password: New account password.
        :param force_reset: Force user to reset password.
        """

        method = "user.account.password.set"
        return await self.call(method, acc_id=acc_id, new_password=new_password, force_reset=force_reset, **kwargs)

    async def user_account_remove(
                self,
                *,
                acc_id: int,
                **kwargs
            ) -> None:
        """
        Removes the specified user account.

        :param acc_id: User Account ID
        """

        method = "user.account.remove"
        return await self.call(method, acc_id=acc_id, **kwargs)

    async def user_account_update(
                self,
                *,
                acc_id,
                acc_user_id=None,
                acc_type=None,
                acc_can_login=None,
                acc_pw_change=None,
                acc_password=None,
                acc_privs=None,
                acc_full_name=None,
                acc_display_name=None,
                acc_sort_name=None,
                acc_email=None,
                tz_id=None,
                date_format=None,
                time_format=None,
                first_weekday=None,
                page_length=None,
                **kwargs
            ) -> Literal["OK"]:
        """
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
        method = "user.account.update"
        params: Dict[str, Any] = {'acc_id': acc_id}

        if acc_user_id:
            params['acc_user_id'] = acc_user_id
        if acc_type:
            params['acc_type'] = acc_type
        if acc_can_login is not None:
            params['acc_can_login'] = acc_can_login
        if acc_pw_change is not None:
            params['acc_pw_change'] = acc_pw_change
        if acc_password:
            params['acc_password'] = acc_password
        if acc_privs:
            if isinstance(acc_privs, (list, tuple, set)):
                acc_privs = ",".join(map(lambda v: v.value, acc_privs))
            params['acc_privs'] = acc_privs.upper()
        if acc_full_name:
            params['acc_full_name'] = acc_full_name
        if acc_display_name:
            params['acc_display_name'] = acc_display_name
        if acc_sort_name:
            params['acc_sort_name'] = acc_sort_name
        if acc_email:
            params['acc_email'] = acc_email
        if tz_id:
            params['tz_id'] = tz_id
        if date_format:
            params['date_format'] = date_format
        if time_format:
            params['time_format'] = time_format
        if first_weekday:
            params['first_weekday'] = first_weekday
        if page_length:
            params['page_length'] = page_length

        params.update(kwargs)
        return await self.call(method, **params)

    async def user_community_add(
                self,
                *,
                com_full_name: str,
                com_id: int,
                com_enabled: bool = True,
                com_max_slots_per_res: Optional[int] = None,
                com_min_hours_btw_res: Optional[int] = None,
                com_mynetlab_news: Optional[str] = None,
                com_mynetlab_welcome: Optional[str] = None,
                **kwargs
            ) -> int:
        """
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

        assert com_id < 100, "Community id out of range"  # TODO document and confirm
        return await self.call(
            'user.community.add',
            com_full_name=com_full_name,
            com_id=com_id,
            com_enabled=com_enabled,
            com_max_slots_per_res=com_max_slots_per_res,
            com_min_hours_btw_res=com_min_hours_btw_res,
            com_mynetlab_news=com_mynetlab_news,
            com_mynetlab_welcome=com_mynetlab_welcome,
            **kwargs)

    async def user_community_update(
                self,
                *,
                com_id: int,
                com_full_name: Optional[str] = None,
                com_enabled: Optional[bool] = None,
                com_mynetlab_welcome: Optional[str] = None,
                com_mynetlab_news: Optional[str] = None,
                com_min_hours_btw_res: Optional[int] = None,
                com_max_slots_per_res: Optional[int] = None,
                com_ext_slots_per_res: Union[None, int, enums.CommunityExtensionSlots] = None,
                **kwargs
            ) -> None:
        """
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
        return await self.call(
            'user.community.update', com_id=com_id, com_full_name=com_full_name, com_enabled=com_enabled,
            com_mynetlab_welcome=com_mynetlab_welcome, com_mynetlab_news=com_mynetlab_news,
            com_min_hours_btw_res=com_min_hours_btw_res, com_max_slots_per_res=com_max_slots_per_res,
            com_ext_slots_per_res=com_ext_slots_per_res, **kwargs)

    async def user_community_remove(self, *, com_id, **kwargs) -> None:
        """
        This method allows you to remove a community.

        :param int com_id: Community identifier.
        """

        return await self.call('user.community.remove', com_id=com_id)

    async def user_community_find(self, *, com_full_name: str, **kwargs) -> Optional[int]:
        """
        This method allows you to find a community based on **com_full_name**.

        :param com_full_name: Community full name.

        :return: The Community ID on success.
        """

        method = "user.community.find"
        result = await self.call(method, com_full_name=com_full_name, **kwargs)

        return None if result is None else int(result)

    async def user_community_get(
                self,
                *,
                com_id: int,
                properties: Union[List[str], Literal['all', 'default']] = "default",
                **kwargs
            ) -> Dict[str, Any]:
        """
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

        method = "user.community.get"
        if properties == 'all':
            properties = self.community_props
        if properties == 'default':
            properties = self.community_default_props

        return await self.call(method, com_id=com_id, properties=properties, **kwargs)

    async def user_community_list(self, *, properties="default", sort_property="com_id", **kwargs):
        """
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

        method = "user.community.list"
        if properties == 'all':
            properties = self.community_props
        if properties == 'default':
            properties = self.community_default_props

        return await self.call(method, properties=properties, sort_property=sort_property, **kwargs)

    async def user_logins_system_get(self, **kwargs):
        """
        This method allows you to query the User Logins status and number of active logins.

        :return: A dictionary with the following properties:
        :rtype: dict

        active
            Number of active users logged in.
        enabled
            User logins status.
        """
        method = "user.logins.system.get"
        return await self.call(method, **kwargs)

    async def user_logins_system_set(self, *, enabled, logout=False, **kwargs):
        """
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
        method = "user.logins.system.set"
        return await self.call(method, enabled=enabled, logout=logout, **kwargs)

    @minimum_version('18.2.0')
    async def user_session_keepalive(self, *, acc_id, **kwargs):
        """
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
        method = "user.session.keepalive"
        return await self.call(method, acc_id=acc_id, **kwargs)
