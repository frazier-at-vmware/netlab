from datetime import datetime
from typing import List, Optional, Dict, Any

from ..utils import minimum_version
from ._client_protocol import ClientProtocol

from .system_results import SystemStatusGetResult


class SystemApiMixin(ClientProtocol):
    async def system_status_get(self, **kwargs) -> SystemStatusGetResult:
        """
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
        method = "system.status.get"
        return await self.call(method, **kwargs)

    @minimum_version('17.1.3')
    def system_usage_cpu(self, **kwargs):
        """
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
        method = "system.usage.cpu"
        return self.call(method, **kwargs)

    @minimum_version('17.1.3')
    async def system_usage_disk(self, **kwargs) -> Dict[str, Any]:
        """
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
        method = "system.usage.disk"
        return await self.call(method, **kwargs)

    @minimum_version('17.1.3')
    async def system_usage_memory(self, **kwargs) -> Dict[str, Any]:
        """
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
        method = "system.usage.memory"
        return await self.call(method, **kwargs)

    @minimum_version('17.1.4')
    async def system_time_timezone_get(self, *, tz_id, **kwargs) -> Dict[str, Any]:
        """
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
        method = 'system.time.timezone.get'
        return await self.call(method, tz_id=tz_id, **kwargs)

    @minimum_version('17.1.4')
    async def system_time_timezone_list(self, **kwargs) -> List[Dict[str, Any]]:
        """
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

        method = 'system.time.timezone.list'
        return await self.call(method, **kwargs)

    @minimum_version('19.0.1')
    async def system_perf_query(
                self,
                *,
                start_time: datetime,
                end_time: Optional[datetime] = None,
                metrics: Optional[List[str]] = None,
                sources: Optional[List[str]] = None,
                **kwargs,
            ) -> List[Dict[str, Any]]:
        """
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

        # Technically start_time is optional, but omitting it causes too much load on the server and
        # returns weird results.

        #  If both start_time and end_time
        # are omitted, the latest observation for each requested metric or source are returned.  If
        # all parameters are omitted, the latest recorded value (if any) for all metrics (if any) are
        # returned.

        method = "system.perf.query"

        params = {
            'start_time': start_time,
            'end_time': end_time,
            'metrics': metrics,
            'sources': sources
        }

        return await self.call(method, **params, **kwargs)
