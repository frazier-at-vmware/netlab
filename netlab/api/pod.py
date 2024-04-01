from typing import Union, List, Dict, Any, Optional
from typing_extensions import Literal

from uuid import UUID

import re

from ..utils import hdr_result, version_gte, omit_nones
from ..datatypes import PCCloneSpec, HDRResult
from .. import enums
from ._client_protocol import ClientProtocol


class PodApiMixin(ClientProtocol):
    pod_default_props = ['pod_id', 'pod_name', 'pt_id', 'pod_current_state']
    pod_props = [
        'def_im_name',
        'def_topology_image',
        'def_vlan_map',
        'device_count',
        'devices',
        'pod_acl_enabled',
        'pod_admin_state',
        'pod_adv_settings',
        'pod_auto_net_enabled',
        'pod_auto_net_host_setup',
        'pod_auto_net_host_teardown',
        'pod_cat',
        'pod_csw_base_vlan',
        'pod_csw_id',
        'pod_current_state',
        'pod_desc',
        'pod_id',
        'pod_id',
        'pod_managed',
        'pod_name',
        'pod_origin',
        'pod_res_id',
        'pod_task_id',
        'pod_task_info',
        'pod_task_type',
        'pod_uuid',
        'pt_actions',
        'pt_adv_settings',
        'pt_apc_port_count',
        'pt_apdid',
        'pt_as_port_count',
        'pt_author',
        'pt_build',
        'pt_copyright',
        'pt_csw_port_count',
        'pt_desc',
        'pt_gpdid',
        'pt_id',
        'pt_name',
        'pt_notes',
        'pt_org',
        'pt_origin',
        'pt_pod_max',
        'pt_removable',
        'pt_tabs',
        'pt_url',
        'pt_vlan_pool',
        'remote_pc',
        'remote_pc_count',
        'reservations',
        'sched_image',
        'vm_alloc']

    pod_types_default_props = ['pt_id', 'pt_name', 'pt_build']
    pod_types_props = ['pt_id', 'pt_name', 'pt_build', 'pt_gpdid', 'pt_apdid', 'pt_desc', 'pt_index', 'pt_type',
                       'sched_image', 'def_topology_image', 'def_im_name', 'def_vlan_map', 'pt_tabs', 'pt_actions',
                       'pt_origin', 'pt_vlan_pool', 'pt_pod_max', 'pt_notes', 'pt_csw_port_count', 'pt_as_port_count',
                       'pt_apc_port_count', 'pt_build', 'pt_author', 'pt_org', 'pt_copyright', 'pt_url', 'pt_removable',
                       'pt_ae_pod', 'pt_adv_settings', 'remote_pc_count', 'device_count']

    def __pc_clone_specs(self, *, user_pc_clone_specs, remote_pc_list, clone_pod_name):
        # Ensure that user_pc_clone_specs is a list of dicts
        if isinstance(user_pc_clone_specs, dict):
            user_pc_clone_specs = [user_pc_clone_specs] * len(remote_pc_list)
        elif user_pc_clone_specs is None:
            user_pc_clone_specs = [{}] * len(remote_pc_list)

        if len(user_pc_clone_specs) != len(remote_pc_list):
            raise ValueError("`user_pc_clone_specs` and `remote_pc_list` must be the same length.")

        # Ensure that the remote_pc_list is in order
        remote_pc_list = sorted(remote_pc_list, key=lambda e: e['pl_index'])

        # Result of this function
        new_vm_out = []

        for pl_index, vms in enumerate(zip(user_pc_clone_specs, remote_pc_list), 1):
            user_vm, existing_vm = vms
            bad_clone_specs = set(user_vm.keys()) - PCCloneSpec.__annotations__.keys()
            if bad_clone_specs:
                raise ValueError("These keys are not allowed: {}".format(bad_clone_specs))

            if user_vm.get('pc_type', existing_vm['pc_type']) == enums.PCType.ABSENT:
                new_vm_out.append({
                    'pl_index': pl_index,
                    'pc_type': user_vm.get('pc_type', existing_vm['pc_type']),
                })
            else:

                vm_path_match = re.match(r'^\[(.*)\].*', existing_vm['vm_path'])
                assert vm_path_match

                copied_user_vm = user_vm.copy()
                del user_vm

                new_vm_out.append({
                    'pl_index': pl_index,
                    'pc_type': copied_user_vm.pop('pc_type', existing_vm['pc_type']),
                    'source_vm_id': existing_vm['vm_id'],
                    'source_snapshot': copied_user_vm.pop('source_snapshot', existing_vm['vm_snapshot']),
                    'clone_snapshot': copied_user_vm.pop('clone_snapshot', existing_vm['vm_snapshot']),
                    'clone_type': copied_user_vm.pop('clone_type', 'LINKED'),
                    'clone_role': copied_user_vm.pop('clone_role', 'NORMAL'),
                    'clone_name': copied_user_vm.pop('clone_name', clone_pod_name + '_' + existing_vm['pc_label']),
                    'clone_storage_alloc': copied_user_vm.pop('clone_storage_alloc', 'ONDEMAND'),
                    'clone_datastore': copied_user_vm.pop('clone_datastore', vm_path_match.group(1)),
                    'clone_vh_id': copied_user_vm.pop('clone_vh_id', existing_vm['vh_id']),
                    **copied_user_vm,
                })

        return new_vm_out

    async def pod_update(
                self,
                *,
                pod_id: int,
                pod_name: Optional[str] = None,
                pod_desc: Optional[str] = None,
                pod_auto_net_enabled: Optional[bool] = None,
                pod_auto_net_host_setup: Optional[bool] = None,
                pod_auto_net_host_teardown: Optional[bool] = None,
                pod_adv_settings: Optional[str] = None,
                pod_acl_enabled: Optional[bool] = None,
                **kwargs
            ) -> None:
        """
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

        method = "pod.update"
        param: Dict[str, Any] = {
            'pod_id': pod_id,
            'pod_name': pod_name,
            'pod_desc': pod_desc,
            'pod_auto_net_enabled': pod_auto_net_enabled,
            'pod_auto_net_host_setup': pod_auto_net_host_setup,
            'pod_auto_net_host_teardown': pod_auto_net_host_teardown,
            'pod_adv_settings': pod_adv_settings,
            'pod_acl_enabled': pod_acl_enabled,
        }

        param = omit_nones(param, {
            'pod_name',
            'pod_desc',
            'pod_auto_net_enabled',
            'pod_auto_net_host_setup',
            'pod_auto_net_host_teardown',
            'pod_adv_settings',
            'pod_acl_enabled',
        })

        return await self.call(method, **param, **kwargs)

    async def pod_add(
                self,
                *,
                pod_id: int,
                pt_id: str,
                devices: Optional[List[Dict[str, Any]]] = None,  # TODO
                pod_acl_enabled: bool = False,
                pod_adv_settings: Optional[str] = None,
                pod_auto_net_enabled: bool = True,
                pod_auto_net_host_setup: bool = True,
                pod_auto_net_host_teardown: bool = True,
                pod_cat: enums.PodCategory = enums.PodCategory.PERSISTENT_VM,
                pod_desc: Optional[str] = None,
                pod_name: Optional[str] = None,
                **kwargs
            ) -> Literal['OK']:
        """
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

        method = "pod.add"
        param = {
            'pod_id': pod_id,
            'pt_id': pt_id,
            'devices': devices,
            'pod_acl_enabled': pod_acl_enabled,
            'pod_adv_settings': pod_adv_settings,
            'pod_auto_net_enabled': pod_auto_net_enabled,
            'pod_auto_net_host_setup': pod_auto_net_host_setup,
            'pod_auto_net_host_teardown': pod_auto_net_host_teardown,
            'pod_cat': pod_cat,
            'pod_desc': pod_desc,
            'pod_name': pod_name,
        }

        param = omit_nones(param, {
            'devices',
            'pod_acl_enabled',
            'pod_adv_settings',
            'pod_desc',
            'pod_name',
        })

        param.update(kwargs)
        return await self.call(method, **param)

    async def pod_get(
                self,
                *,
                pod_id: int,
                properties: Union[List[str], Literal['all', 'default']] = "default",
                **kwargs
            ) -> Dict[str, Any]:
        """

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

        method = "pod.get"

        if properties == 'all':
            properties = self.pod_props
        if properties == 'default':
            properties = self.pod_default_props

        res_param = {
            'pod_id': pod_id,
            'properties': properties,
        }
        res_param.update(kwargs)
        return await self.call(method, **res_param)

    async def pod_list(
                self,
                *,
                pod_cat: Optional[enums.PodCategory] = None,
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
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
        method = "pod.list"

        res_param = {}
        if pod_cat is not None:
            res_param['pod_cat'] = pod_cat

        res_param.update(kwargs)
        return await self.call(method, **res_param)

    async def pod_list_used_ids(self, **kwargs) -> List[int]:
        """
        List the used pod_id's on the system.

        :return: Returns a list of pod_ids
        """

        method = "pod.list.used_ids"

        pod_ids = await self.call(method, **kwargs)

        return list(map(int, pod_ids))

    async def pod_pc_get(
                self,
                *,
                pod_id: Optional[int] = None,
                pl_index: Optional[int] = None,
                pc_id: Optional[int] = None,
                **kwargs
            ) -> Dict[str, Any]:
        """
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

        method = "pod.pc.get"

        res_param = {}
        if pod_id is not None:
            res_param['pod_id'] = pod_id
        if pl_index is not None:
            res_param['pl_index'] = pl_index
        if pc_id is not None:
            res_param['pc_id'] = pc_id

        res_param.update(kwargs)
        return await self.call(method, **res_param)

    async def pod_pc_update(
                self,
                *,
                pc_id: int,
                pc_type: Optional[Literal['ABSENT', 'AVMI']] = None,
                pc_os_id: Optional[str] = None,
                pc_online: Optional[bool] = None,
                vm_shutdown_pref: Optional[str] = None,
                vm_id: Optional[int] = None,
                vm_snapshot: Optional[str] = None,
                vm_auto_display: Optional[bool] = None,
                vm_auto_network: Optional[bool] = None,
                vm_auto_settings: Optional[bool] = None,
                vm_sanity_checks: Optional[bool] = None,
                **kwargs
            ) -> None:
        """
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

        method = "pod.pc.update"
        params: Dict[str, Any] = {
            'pc_id': pc_id,
        }

        if pc_type:
            params['pc_type'] = pc_type
        if pc_os_id:
            params['pc_os_id'] = pc_os_id
        if pc_online:
            params['pc_online'] = pc_online
        if vm_shutdown_pref:
            params['vm_shutdown_pref'] = vm_shutdown_pref
        if vm_id:
            params['vm_id'] = vm_id
        if vm_snapshot:
            params['vm_snapshot'] = vm_snapshot
        if vm_auto_display:
            params['vm_auto_display'] = vm_auto_display
        if vm_auto_network:
            params['vm_auto_network'] = vm_auto_network
        if vm_auto_settings:
            params['vm_auto_settings'] = vm_auto_settings
        if vm_sanity_checks:
            params['vm_sanity_checks'] = vm_sanity_checks

        params.update(kwargs)
        return await self.call(method, **params)

    async def pod_state_change(
                self,
                *,
                pod_id: int,
                state: enums.PodState,
                **kwargs
            ) -> Literal["OK"]:
        """
        Sets pod state to either ONLINE, OFFLINE or RESUME.

        :param pod_id: Pod ID
        :param state: PC Pod State
        """

        method = "pod.state.change"

        res_param = {
            'pod_id': pod_id,
            'state': state,
        }

        res_param.update(kwargs)
        return await self.call(method, **res_param)

    async def pod_types_get(
                self,
                *,
                pt_id: str,
                properties: Union[List[str], Literal["default"], Literal["all"]] = "default",
                **kwargs,
            ) -> Dict[str, Any]:
        """
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

        method = "pod.types.get"

        if properties == 'all':
            properties = self.pod_types_props
        if properties == 'default':
            properties = self.pod_types_default_props

        res_param = {
            'pt_id': pt_id,
            'properties': properties
        }

        res_param.update(kwargs)
        return await self.call(method, **res_param)

    async def pod_types_list(
                self,
                *,
                properties: Union[List[str], Literal['all', 'default']] = "default",
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
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
        method = "pod.types.list"

        if properties == 'all':
            properties = self.pod_types_props
        if properties == 'default':
            properties = self.pod_types_default_props

        return await self.call(method, properties=properties, **kwargs)

    async def pod_remove_task(
                self,
                *,
                pod_id: int,
                remove_vms: enums.RemoveVMS = enums.RemoveVMS.NONE,
                severity_level: enums.HDRSeverity = enums.HDRSeverity.WARN,
                **kwargs
            ) -> HDRResult:
        """
        :param pod_id: Pod unique identifier.
        :param remove_vms: Specifies the method for removing the virtual machines.
        :param severity_level: Display detailed events for the task only at this severity level or
            higher.

        :return: HDR result
        """

        method = "pod.remove.task"

        params = {
            'pod_id': pod_id,
            'remove_vms': remove_vms,
            'notify_progress': False,
            'notify_complete': False,
        }

        params.update(kwargs)
        result = await self.call(method, **params)

        if version_gte(self._server_version, '17.1.4'):
            return hdr_result(result, severity_level)
        else:
            return result

    async def pod_clone_task(
                self,
                *,
                source_pod_id: int,
                clone_pod_id: int,
                clone_pod_name: str,
                pc_clone_specs: Optional[Union[List[PCCloneSpec],  PCCloneSpec]] = None,
                severity_level: enums.HDRSeverity = enums.HDRSeverity.WARN,
                **kwargs
            ) -> HDRResult:
        """
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

        method = "pod.clone.task"

        remote_pc = await self.pod_get(pod_id=source_pod_id, properties=['remote_pc'])

        pc_clone_specs = self.__pc_clone_specs(
            clone_pod_name=clone_pod_name,
            user_pc_clone_specs=pc_clone_specs,
            remote_pc_list=remote_pc['remote_pc'])

        result = await self.call(
            method, source_pod_id=source_pod_id,
            clone_pod_id=clone_pod_id, clone_pod_name=clone_pod_name,
            pc_clone_specs=pc_clone_specs, **kwargs)

        if version_gte(self._server_version, '17.1.4'):
            return hdr_result(result, severity_level)
        else:
            return result

    async def pod_acl_add(
                self,
                *,
                com_id: int,
                pod_id: int,
                acc_id: Optional[int] = None,
                cls_id: Optional[int] = None,
                team: Optional[str] = None,
                **kwargs
            ) -> UUID:
        """
        This method allows you to add access controls to a pod on the NETLAB+ system.

        :param com_id: Community identifier.
        :param pod_id: Pod identifier.
        :param acc_id: Account identifier.
        :param cls_id: Class identifier.
        :param team: Team assignment.
        :return: Pod access control list UUID.
        """

        args = {
            'com_id': com_id,
            'pod_id': pod_id,
            'acc_id': acc_id,
            'cls_id': cls_id,
            'team': team,
        }
        args.update(kwargs)
        return await self.call('pod.acl.add', **args)

    async def pod_acl_admin_add(
                self,
                *,
                acc_id: int,
                pod_id: int,
                **kwargs
            ) -> None:
        """
        This method allows you add additional pod access control administrators.

        :param int acc_id: Account identifier.
        :param int pod_id: Pod identifier.
        """

        return await self.call('pod.acl.admin.add', acc_id=acc_id, pod_id=pod_id, **kwargs)

    async def pod_acl_admin_auth(
                self,
                *,
                acc_id: int,
                pod_id: int,
                **kwargs,
            ) -> bool:
        """
        This method returns true if a specified instructor account is authorized to manage POD
        ACLs on a specified pod.

        :param acc_id: Account identifier.
        :param pod_id: Pod identifier.

        :return: acc_id is authorized for pod_id.
        """

        result = await self.call('pod.acl.admin.auth', acc_id=acc_id, pod_id=pod_id, **kwargs)

        return bool(int(result))

    async def pod_acl_admin_list(
                self,
                *,
                pod_id: int,
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
        This method allows you to retrieve a list of pod access controls per pod.

        :param pod_id: Pod identifier.
        :return: Pod access control list.
        """

        return await self.call('pod.acl.admin.list', pod_id=pod_id, **kwargs)

    async def pod_acl_admin_pods(
                self,
                *,
                acc_id: int,
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
        This method allows you to retrieve a list of pods a user has access to.

        :param int acc_id: Account identifier.
        """

        return await self.call('pod.acl.admin.pods', acc_id=acc_id, **kwargs)

    async def pod_acl_admin_remove(
                self,
                *,
                acc_id: int,
                pod_id: int,
                **kwargs
            ) -> None:
        """
        This method allows you to remove authorization for an account.

        :param acc_id: Account identifier.
        :param pod_id: Pod identifier.
        """

        return await self.call('pod.acl.admin.remove', acc_id=acc_id, pod_id=pod_id, **kwargs)

    async def pod_acl_challenge(
                self,
                *,
                com_id: int,
                pod_id: int,
                acc_id: Optional[int] = None,
                cls_id: Optional[int] = None,
                team: Optional[str] = None,
                **kwargs
            ) -> UUID:
        """
        This method allows you to test against a pod access control list.

        :param int com_id: Community identifier.
        :param int pod_id: Pod identifier.
        :param int acc_id: Account identifier.
        :param int cls_id: Class identifier.
        :param str team: Team assignment.
        :return: If matching rule found, pod access control list UUID.
        """

        return await self.call('pod.acl.challenge', com_id=com_id, pod_id=pod_id, acc_id=acc_id, cls_id=cls_id,
                               team=team, **kwargs)

    async def pod_acl_get(
                self,
                *,
                pacl_uuid: UUID,
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
        This method allows you to retrieve a pod access control list.

        :param pacl_uuid: Pod access control list UUID.
        :return: Pod access control list.
        """

        return await self.call('pod.acl.get', pacl_uuid=pacl_uuid, **kwargs)

    async def pod_acl_list(
                self,
                *,
                pod_id: int,
                **kwargs
            ) -> List[Dict[str, Any]]:
        """
        This method allows you to retrieve a list of pod access controls per pod.

        :param pod_id: Pod identifier.
        :return: Pod access control list.
        """

        return await self.call('pod.acl.list', pod_id=pod_id, **kwargs)

    async def pod_acl_remove(
                self,
                *,
                pacl_uuid: UUID,
                **kwargs
            ) -> None:
        """
        This method allows you to remove a pod access control list.

        :param pacl_uuid: Pod access control list UUID.
        """

        return await self.call('pod.acl.remove', pacl_uuid=pacl_uuid, **kwargs)
