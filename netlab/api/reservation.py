from typing import Optional, Any, Dict, List
from typing_extensions import Literal
from datetime import datetime, timedelta, date as date_type

from .. import enums
from ..utils import minimum_version, omit_nones
from ._client_protocol import ClientProtocol

from typing import overload


class ReservationApiMixin(ClientProtocol):
    @staticmethod
    def reservation_timeslot_adjuster(*, user_time: datetime, round_low: bool = False) -> datetime:
        """
        Round a datetime to the nearest half hour, which is required for some times in netlab.

        :param user_time: Must be a datetime object. Adjusted for fulfilling time slot
            if not already time slot acceptable.
        :param round_low: True: rounds time in minutes down to the low timeslot. False: rounds time up to next
            timeslot.

        :return: Datetime rounded to half hour.
        """

        adjusted_minutes = 30 * (user_time.minute // 30)  # floor division used to round minutes down
        adjusted_time = user_time.replace(minute=adjusted_minutes, second=0, microsecond=0)

        if adjusted_time == user_time or round_low:
            pass
        else:
            adjusted_time += timedelta(minutes=30)

        return adjusted_time

    async def reservation_make(
                self,
                *,
                type: enums.ReservationType,
                pod_id: int,
                cls_id: int,
                end_time: datetime,
                start_time: Optional[datetime] = None,
                acc_id: Optional[int] = None,
                reserver_id: Optional[int] = None,
                tz_id: Optional[int] = None,
                tz_olson: Optional[str] = None,
                team: Optional[str] = None,
                pt_id: Optional[int] = None,
                ex_id: str,
                init_config: enums.InitConfig = enums.InitConfig.NONE,
                **kwargs
            ) -> Dict[str, Any]:
        """
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

        method = "reservation.make"

        assert isinstance(type, enums.ReservationType)

        # Because for some reason these are diffrent
        if type is enums.ReservationType.INDIVIDUAL:
            fixed_type = 'INDIVIDUAL'
        elif type is enums.ReservationType.ILT_CLASS:
            fixed_type = 'ILT_CLASS'
        elif type is enums.ReservationType.INSTRUCTOR:
            fixed_type = 'INSTRUCTOR'
        elif type is enums.ReservationType.TEAM:
            fixed_type = 'TEAM'

        res_param = {
            'type': fixed_type,
            'pod_id': pod_id,
            'end_time': end_time,
            'start_time': start_time,
            'acc_id': acc_id,
            'reserver_id': reserver_id,
            'tz_id': tz_id,
            'tz_olson': tz_olson,
            'team': team,
            'pt_id': pt_id,
            'ex_id': ex_id,
            'cls_id': cls_id,
            'init_config': init_config,
        }

        res_param = omit_nones(res_param, {
            'start_time',
            'acc_id',
            'reserver_id',
            'tz_id',
            'tz_olson',
            'team',
            'pt_id',
            'ex_id',
            'cls_id',
            'init_config',
        })

        res_param.update(kwargs)
        return await self.call(method, **res_param)

    async def reservation_plan(
                self,
                *,
                acc_id: Optional[int] = None,
                cls_id: Optional[int] = None,
                date: date_type,
                ex_id: Optional[int] = None,
                pod_id: Optional[int] = None,
                reserver_id: Optional[int] = None,
                team: Optional[int] = None,
                type: enums.ReservationType,
                tz_id: Optional[int] = None,
                tz_olsen: Optional[str] = None,
                **kwargs,
            ) -> Dict[str, Any]:
        """
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
        method = "reservation.plan"

        params = {
            'date': date,
            'type': type,
            'acc_id': acc_id,
            'cls_id': cls_id,
            'ex_id': ex_id,
            'pod_id': pod_id,
            'reserver_id': reserver_id,
            'team': team,
            'tz_id': tz_id,
            'tz_olson': tz_olsen,
        }

        params = omit_nones(params, {
            'acc_id',
            'cls_id',
            'ex_id',
            'pod_id',
            'reserver_id',
            'team',
            'tz_id',
            'tz_olson',
        })

        return await self.call(method, **params, **kwargs)

    async def reservation_get(
                self,
                *,
                res_id: int,
                **kwargs
            ) -> Dict[str, Any]:
        """
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

        method = "reservation.get"
        res_param = {'res_id': res_id}

        res_param.update(kwargs)
        return await self.call(method, **res_param)

    async def reservation_post(
                self,
                *,
                res_id: int,
                **kwargs
            ) -> None:
        """
        Ends a reservation that has already started.

        :param res_id: Reservation identifier.
        """

        method = "reservation.post"
        return await self.call(method, res_id=res_id, **kwargs)

    async def reservation_cancel(
                self,
                *,
                res_id: int,
                **kwargs
            ) -> None:
        """
        Cancel a reservation in NETLAB+ prior to reservation being started.

        NOTE - if you wish to end a reservation that is already started use reservation_post.

        :param res_id: Reservation unique identifier.
        """

        method = "reservation.cancel"
        return await self.call(method, res_id=res_id, **kwargs)

    async def reservation_summary(self, **kwargs) -> Dict[str, Any]:
        """
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

        method = "reservation.summary"
        return await self.call(method, **kwargs)

    @overload
    async def reservation_query(
            self,
            *,
            active: Optional[bool] = None,
            min_time: Optional[datetime] = None,
            max_time: Optional[datetime] = None,
            cls_id: Optional[int] = None,
            pod_id: Optional[int] = None,
        ) -> List[Dict[str, Any]]: ...

    @overload
    async def reservation_query(
            self,
            *,
            active: Optional[bool] = None,
            scope: enums.ReservationScope = enums.ReservationScope.ALL,
            min_time: Optional[datetime] = None,
            max_time: Optional[datetime] = None,
            com_id: Optional[int] = None,
            pod_id: Optional[int] = None,
        ) -> List[Dict[str, Any]]: ...

    async def reservation_query(
                self,
                *,
                active: Optional[bool] = None,
                scope: enums.ReservationScope = enums.ReservationScope.ALL,
                min_time: Optional[datetime] = None,
                max_time: Optional[datetime] = None,
                com_id: Optional[int] = None,
                cls_id: Optional[int] = None,
                pod_id: Optional[int] = None,
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
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

        method = "reservation.query"

        assert not (cls_id is not None and com_id is not None)

        if com_id is not None:
            assert cls_id is None
            scope = enums.ReservationScope.CLASS

        res_param: Dict[str, Any] = {}
        if active:
            res_param['active'] = active
        if cls_id:
            res_param['cls_id'] = cls_id
        if com_id:
            res_param['com_id'] = com_id
        if max_time:
            res_param['max_time'] = max_time
        if min_time:
            res_param['min_time'] = min_time
        if pod_id:
            res_param['pod_id'] = pod_id
        if scope:
            res_param['scope'] = scope

        res_param.update(kwargs)
        return await self.call(method, **res_param)

    async def reservation_time_now(
                self,
                *,
                tz_id: Optional[int] = None,
                tz_olson: Optional[str] = None,
                **kwargs
            ) -> Dict[str, Any]:
        """
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

        method = "reservation.time.now"
        res_param: Dict[str, Any] = {}

        if not (tz_id is None or tz_id == 0):  # tz_id==0 is utc, but this fails if passed to api
            res_param['tz_id'] = tz_id
        if tz_olson is not None:
            res_param['tz_olson'] = tz_olson

        res_param.update(kwargs)
        return await self.call(method, **res_param)

    async def reservation_time_offset(
                self,
                *,
                time: Optional[datetime] = None,
                op: Optional[Literal['+', '-']] = None,
                tz_id_in: Optional[int] = None,
                tz_olson_in=None,
                tz_id_out=None,
                tz_olson_out=None,
                slot_roundup=False,
                years=None,
                months=None,
                weeks=None,
                days=None,
                hours=None,
                minutes=None,
                seconds=None,
                **kwargs
            ) -> Dict[str, Any]:
        """
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

        method = "reservation.time.offset"
        res_param = {'slot_roundup': slot_roundup}

        if time:
            res_param['time'] = time
        if op:
            res_param['op'] = op
        if not (tz_id_in is None or tz_id_in == 0):  # tz_id==0 is utc, but this fails if passed to api
            res_param['tz_id_in'] = tz_id_in
        if tz_olson_in:
            res_param['tz_olson_in'] = tz_olson_in
        if not (tz_id_out is None or tz_id_out == 0):  # tz_id==0 is utc, but this fails if passed to api
            res_param['tz_id_out'] = tz_id_out
        if tz_olson_out:
            res_param['tz_olson_out'] = tz_olson_out
        if years:
            res_param['years'] = years
        if months:
            res_param['months'] = months
        if weeks:
            res_param['weeks'] = weeks
        if days:
            res_param['days'] = days
        if hours:
            res_param['hours'] = hours
        if minutes:
            res_param['minutes'] = minutes
        if seconds:
            res_param['seconds'] = seconds

        res_param.update(kwargs)
        return await self.call(method, **res_param)

    async def reservation_time_delta(
                self,
                *,
                end: datetime,
                start: Optional[datetime] = None,
                tz_id: Optional[int] = None,
                tz_olson: Optional[str] = None,
                **kwargs
            ) -> Dict[str, Any]:
        """
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
        method = "reservation.time.delta"

        res_param: Dict[str, Any] = {
            'end': end,
        }
        if start:
            res_param['start'] = start
        if not (tz_id is None or tz_id == 0):  # tz_id==0 is utc, but this fails if passed to api
            res_param['tz_id'] = tz_id
        if tz_olson:
            res_param['tz_olson'] = tz_olson

        res_param.update(kwargs)
        return await self.call(method, **res_param)

    async def reservation_extend(
                self,
                *,
                res_id,
                **kwargs
            ) -> Dict[str, Any]:
        """
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

        method = 'reservation.extend'
        return await self.call(method, res_id=res_id, **kwargs)

    @minimum_version('18.1.0')
    async def history_reservation_get(
                self,
                *,
                res_id,
                **kwargs
            ) -> Dict[str, Any]:
        method = "history.reservation.get"
        return await self.call(method, res_id=res_id, **kwargs)
