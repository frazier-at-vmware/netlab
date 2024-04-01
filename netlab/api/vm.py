from typing import Optional, List, Any, Dict, overload
from typing_extensions import Literal

import warnings

from .. import enums
from ..errors.vm import VirtualMachineDatacenterNotFoundError
from ..utils import minimum_version

from ._client_protocol import ClientProtocol


class VmApiMixin(ClientProtocol):
    async def vm_datacenter_get(
                self,
                *,
                vdc_id: int,
                **kwargs
            ) -> Dict[str, Any]:
        """
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

        method = "vm.datacenter.get"
        return await self.call(method, vdc_id=vdc_id, **kwargs)

    async def vm_datacenter_find(
                self,
                *,
                vdc_name: str,
                **kwargs
            ) -> Optional[int]:
        """
        This method allows you to find a datacenter's **vdc_id** by the datacenter name.

        :param vdc_name: VM Datacenter name.

        :return: On success, returns vdc_id. If there is no VDC matching, returns None.
        """

        method = "vm.datacenter.get"
        try:
            result = await self.call(method, vdc_name=vdc_name, **kwargs)
            return result['vdc_id']
        except VirtualMachineDatacenterNotFoundError:
            return None

    async def vm_datacenter_list(self, **kwargs) -> List[Dict[str, Any]]:
        """
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

        method = "vm.datacenter.list"
        return await self.call(method, **kwargs)

    async def vm_datacenter_test(
                self,
                *,
                vdc_id: int,
                **kwargs
            ) -> Literal['PASSED', 'FAILED']:
        """
        This method allows you to call a task to test communication to datacenter.

        :param vdc_id: VM Datacenter identifier.

        :return: On success returns 'PASSED', otherwise returns 'FAILED'.
        """

        method = "vm.datacenter.test.task"
        return await self.call(method, vdc_id=vdc_id, **kwargs)

    async def vm_host_get(
                self,
                *,
                vh_id: int,
                **kwargs
            ) -> Dict[str, Any]:
        """
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

        method = "vm.host.get"
        return await self.call(method, vh_id=vh_id, **kwargs)

    async def vm_host_find(
                self,
                *,
                vh_name: str,
                **kwargs
            ) -> Optional[int]:
        """
        This method allows you to find a virtual host's **vh_id** by the virtual host name.

        :param vh_name: Virtual Host name.

        :return: On success, returns vh_id. If there is no matching Virtual Host, returns None.
        """

        method = "vm.host.list"

        hosts = await self.call(method, **kwargs)

        for host in hosts:
            if host.get('vh_name') == vh_name:
                return host['vh_id']
        else:
            return None

    async def vm_host_list(
                self,
                *,
                vdc_id: Optional[str] = None,
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
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

        method = "vm.host.list"
        return await self.call(method, vdc_id=vdc_id, **kwargs)

    async def vm_inventory_add(
                self,
                *,
                vdc_id,
                vm_uuid,
                vm_name,
                vm_path=None,
                vm_alloc_mem_mb,
                vm_alloc_cpu_n,
                vhg_id=None,
                vh_id=None,
                vm_role=enums.VirtualMachineRole.NORMAL,
                vm_comments=None,
                vm_vendor_os_id=None,
                vm_vendor_os_name=None,
                vm_netlab_os_id=None,
                vm_parent_id=None,
                vm_parent_snapname=None,
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
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
        warnings.warn("'vm_inventory_add' is deprecated, please use 'vm_inventory_import_task' instead",
                      DeprecationWarning)

        method = 'vm.inventory.add'
        return await self.call(
            method, vdc_id=vdc_id, vm_uuid=vm_uuid, vm_name=vm_name, vm_path=vm_path,
            vm_alloc_mem_mb=vm_alloc_mem_mb, vm_alloc_cpu_n=vm_alloc_cpu_n, vhg_id=vhg_id, vh_id=vh_id,
            vm_role=vm_role, vm_comments=vm_comments, vm_vendor_os_id=vm_vendor_os_id,
            vm_vendor_os_name=vm_vendor_os_name, vm_netlab_os_id=vm_netlab_os_id,
            vm_parent_id=vm_parent_id, vm_parent_snapname=vm_parent_snapname, **kwargs)

    async def vm_inventory_import_task(
                self,
                *,
                vdc_id: int,
                vm_property_list: List[Dict[str, Any]],
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
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
        method = 'vm.inventory.import.task'
        return await self.call(method, vdc_id=vdc_id, vm_property_list=vm_property_list, **kwargs)

    async def vm_inventory_get(
                self,
                *,
                vm_id: int,
                **kwargs
            ) -> Dict[str, Any]:
        """
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
        method = "vm.inventory.get"
        return await self.call(method, vm_id=vm_id, **kwargs)

    async def vm_inventory_list(
                self,
                *,
                vdc_id: Optional[int] = None,
                roles: Optional[List[str]] = None,
                attached: Optional[bool] = None,
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
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
        method = "vm.inventory.get"
        params: Dict[str, Any] = {}

        if vdc_id:
            params['vdc_id'] = vdc_id
        if roles:
            params['roles'] = roles
        if attached is not None:
            params['attached'] = attached

        params.update(kwargs)
        return await self.call(method, **params)

    async def vm_snapshot_add(
                self,
                *,
                vm_id: Optional[int] = None,
                pc_id: Optional[int] = None,
                snapshot_name: str,
                dump_memory: bool = False,
                sync: bool = False,
                description: Optional[str] = None,
                **kwargs
            ) -> None:
        """
        Method to call a task to add snapshot to virtual machine.

        :param vm_id: Virtual datacenter identifier.
        :param pc_id: Remote pc identifier.
        :param snapshot_name: Name of snapshot to take.
        :param dump_memory: Dump memory files.
        :param sync: Sync files.
        :param description: Snapshot description.
        """

        method = "vm.snapshot.add.task"
        return await self.call(
            method, vm_id=vm_id, pc_id=pc_id, snapshot_name=snapshot_name, dump_memory=dump_memory,
            sync=sync, description=description, **kwargs)

    async def vm_snapshot_edit(
                self,
                *,
                vm_id: Optional[int] = None,
                pc_id: Optional[int] = None,
                snapshot_id: Optional[int] = None,
                new_snapshot_name: Optional[str] = None,
                new_snapshot_description: Optional[str] = None,
                **kwargs
            ) -> None:
        """
        Method to call a task to edit a snapshot.

        :param vm_id: Virtual datacenter identifier.
        :param pc_id: Remote pc identifier.
        :param snapshot_id: Snapshot identifier.
        :param new_snapshot_name: New name of snapshot to take.
        :param new_snapshot_description: New description of snapshot.
        """
        method = "vm.snapshot.edit.task"
        return await self.call(
            method, vm_id=vm_id, pc_id=pc_id, snapshot_id=snapshot_id,
            new_snapshot_name=new_snapshot_name, new_snapshot_description=new_snapshot_description,
            **kwargs)

    @overload
    async def vm_snapshot_get_list(
        self,
        *,
        pc_id: int,
    ) -> Dict[str, Any]:
        ...

    @overload
    async def vm_snapshot_get_list(
        self,
        *,
        vm_id: int,
    ) -> Dict[str, Any]:
        ...

    async def vm_snapshot_get_list(
                self,
                *,
                vm_id: Optional[int] = None,
                pc_id: Optional[int] = None,
                **kwargs
            ) -> Dict[str, Any]:
        """
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
        method = "vm.snapshot.get.list.task"
        return await self.call(method, vm_id=vm_id, pc_id=pc_id, **kwargs)

    @overload
    async def vm_snapshot_get_tree(
        self,
        *,
        pc_id: int,
    ) -> Dict[str, Any]:
        ...

    @overload
    async def vm_snapshot_get_tree(
        self,
        *,
        vm_id: int,
    ) -> Dict[str, Any]:
        ...

    async def vm_snapshot_get_tree(
                self,
                *,
                vm_id: Optional[int] = None,
                pc_id: Optional[int] = None,
                **kwargs
            ) -> Dict[str, Any]:
        """
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
        method = "vm.snapshot.get.tree.task"
        return await self.call(method, vm_id=vm_id, pc_id=pc_id, **kwargs)

    async def vm_snapshot_remove(
                self,
                *,
                vm_id: Optional[int] = None,
                pc_id: Optional[int] = None,
                snapshot_name: Optional[str] = None,
                snapshot_id: Optional[int] = None,
                remove_children: Optional[bool] = None,
                remove_all_snapshots: Optional[bool] = None,
                **kwargs
            ) -> None:
        """
        Method to call a task to remove snapshot from virtual machine.

        :param vm_id: Virtual datacenter identifier.
        :param pc_id: Remote pc identifier.
        :param snapshot_name: Name of snapshot to take.
        :param snapshot_id: Snapshot identifier.
        :param remove_children: Remove children snapshots.
        :param remove_all_snapshots: Remove all snapshots of virtual machine.
        """
        method = "vm.snapshot.remove.task"
        return await self.call(
            method, vm_id=vm_id, pc_id=pc_id, snapshot_name=snapshot_name, snapshot_id=snapshot_id,
            remove_children=remove_children, remove_all_snapshots=remove_all_snapshots, **kwargs)

    async def vm_snapshot_revert(
                self,
                *,
                vm_id: Optional[int] = None,
                pc_id: Optional[int] = None,
                snapshot_name: Optional[str] = None,
                snapshot_id: Optional[int] = None,
                **kwargs
            ) -> None:
        """
        Method to call a task to revert to snapshot from virtual machine.

        :param vm_id: Virtual datacenter identifier.
        :param pc_id: Remote pc identifier.
        :param snapshot_name: Name of snapshot to take.
        :param snapshot_id: Snapshot identifier.
        """
        method = "vm.snapshot.revert.task"
        return await self.call(
            method, vm_id=vm_id, pc_id=pc_id, snapshot_name=snapshot_name, snapshot_id=snapshot_id, **kwargs)

    async def vm_clone_task(
                self,
                *,
                parent_vm_id: int,
                parent_snapname: str,
                clone_role: enums.VirtualMachineRole,
                clone_type: enums.CloneType,
                clone_name: str,
                clone_datastore: Optional[str] = None,
                clone_storage_alloc: enums.CloneStorageAllocation = enums.CloneStorageAllocation.ONDEMAND,
                clone_vh_id: Optional[int] = None,
                clone_vhg_id: Optional[int] = None,
                clone_comments: Optional[str] = None,
                copy_bios_uuid: bool = False,
                **kwargs
            ) -> int:
        """
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
        method = "vm.clone.task"
        args = {
            'clone_name': clone_name,
            'clone_type': clone_type,
            'clone_role': clone_role,
            'parent_vm_id': parent_vm_id,
            'copy_bios_uuid': copy_bios_uuid,
            'parent_snapname': parent_snapname,
        }
        args.update(kwargs)

        # if parent_snapname is not None:
        #     args['parent_snapname'] = parent_snapname
        if clone_datastore is not None:
            args['clone_datastore'] = clone_datastore
        if clone_vh_id is not None:
            args['clone_vh_id'] = clone_vh_id
        if clone_vhg_id is not None:
            args['clone_vhg_id'] = clone_vhg_id
        if clone_comments is not None:
            args['clone_comments'] = clone_comments

        return await self.call(method, **args)

    async def vm_inventory_remove_disk_task(
                self,
                *,
                vm_id: int,
                **kwargs
            ) -> None:
        """
        Remove virtual machine from NETLAB+ inventory, datacenter, and disk.

        **WARNING: this method permanantly deletes the virtual machine files
        from disk.  This operation cannot be undone.**

        :param vm_id: Virtual machine identifier.
        """
        method = 'vm.inventory.remove.disk.task'

        args = {
            'vm_id': vm_id,
        }

        args.update(kwargs)

        return await self.call(method, **args)

    async def vm_inventory_remove_datacenter_task(
                self,
                *,
                vm_id: int,
                **kwargs
            ) -> None:
        """
        Remove virtual machine from NETLAB+ inventory and datacenter.
        Does NOT remove VM from disk.

        :param int vm_id: Virtual machine identifier.
        """
        method = "vm.inventory.remove.datacenter.task"

        args = {
            'vm_id': vm_id,
        }
        args.update(kwargs)

        return await self.call(method, **args)

    async def vm_inventory_remove_local(
                self,
                *,
                vm_id,
                **kwargs
            ) -> None:
        """
        Remove virtual machine from NETLAB+ inventory only.
        Does NOT remove VM from datacenter or disk.

        :param vm_id: Virtual machine identifier.
        """
        method = "vm.inventory.remove.local"

        args = {
            'vm_id': vm_id,
        }
        args.update(kwargs)

        return await self.call(method, **args)

    @minimum_version('18.2.0')
    async def vm_license_list(
                self,
                *,
                vdc_id: Optional[int] = None,
                vh_id: Optional[int] = None,
                vl_server: Optional[int] = None,
                vl_key: Optional[int] = None,
                vl_type: Optional[enums.VirtualMachineLicenseType] = None,
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
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

        method = "vm.license.list"

        params: Dict[str, Any] = {}
        params.update(**kwargs)

        if vdc_id is not None:
            params['vdc_id'] = vdc_id
        if vh_id is not None:
            params['vh_id'] = vh_id
        if vl_server is not None:
            params['vl_server'] = vl_server
        if vl_key is not None:
            params['vl_key'] = vl_key
        if vl_type is not None:
            params['vl_type'] = vl_type

        return await self.call(method, **params)

    @minimum_version('18.2.0')
    async def vm_license_update_task(self, **kwargs) -> Dict[str, Any]:
        """
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

        method = "vm.license.update.task"
        return await self.call(method, **kwargs)

    async def vm_host_perf_realtime_list(
                self,
                *,
                vh_id: Optional[List[int]] = None,
                **kwargs,
            ) -> List[Dict[str, Any]]:
        """
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
        method = "vm.host.perf.realtime.list"

        params = {}

        if vh_id is not None:
            params['vh_id'] = ','.join(map(str, vh_id))

        return await self.call(method, **params, **kwargs)
