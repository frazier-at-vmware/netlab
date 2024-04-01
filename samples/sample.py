import datetime

from netlab.sync_client import SyncClient
from netlab.enums import PodState

"""
The intent of this code is to help you, the NETLAB+ administrator, learn how you can use the
NETLAB+ API to automate repetitive and tasks associate with administering NETLAB+. This sample
file contains functions that identify how to make an API call and what you can do with it's
output.

You will need to have a running version of python 3 (python 3.5 or greater is best) and install pip.
The netlab api can be obtained by running the following PIP command:

     pip install https://ndg.tech/netlab-py-latest

You are encouraged to use code in this document as you see fit for your environment.

If you are new to programming, do not fear. You can copy this document or functions in the document,
alter noted variables and be up and running in minutes.
"""

# The system will need to be changed to the name given to your system in the .netlab/config.json file
# or create a entry for DEMO in your config.json.
tapi = SyncClient(system='DEMO')


def pod_add():
    """
    This function will add pods with corresponding pod designs from pods listed below.

    The pod type id (pt_id) is the pod design UUID and is subject to change with new revisions of the
    pod design or new course.

    Also note that the the pod id (pod_id) and pod name (pod_name) does not need to follow the scheme
    as they are layed out below. They can be adjusted to your preference.
    """
    # tapi.pod_add(pod_id=1000, pt_id=str("RHSA7_0050_56A9_38CC_5682_A22E"), pod_name="RHSA7_GM")
    # tapi.pod_add(pod_id=2000, pt_id=str("NDGEH_0050_56A9_38CC_5612_BA75"), pod_name="NDG_EH_GM")
    # tapi.pod_add(pod_id=3000, pt_id=str("NDGDF_0050_56A9_38CC_568E_877A"), pod_name="NDG_Forensics_GM")
    # tapi.pod_add(pod_id=4999, pt_id=str("PAN7GW_0050_56A9_38CC_5682_D5F0"), pod_name="PAN7_GW_GM")
    # tapi.pod_add(pod_id=4000, pt_id=str("PAN7FE_0050_56A9_38CC_5682_D3B7"), pod_name="PAN7_FE_GM")
    # tapi.pod_add(pod_id=5000, pt_id=str("VMVCADCV6_0050_56A9_38CC_5628_F6DE"), pod_name="VM_VCA_DCV_6_GM")
    # tapi.pod_add(pod_id=6000, pt_id=str("VCPICM6F1_0050_56A9_DC6B_5643_78BE"), pod_name="VM_VCP_ICM_6_GM")
    # tapi.pod_add(pod_id=7000, pt_id=str("VMWOS6_0050_56A9_38CC_5630_CB6A"), pod_name="VM_VCP_ONS_6_GM")
    # tapi.pod_add(pod_id=8000, pt_id=str("EMCCIS01_0050_56B3_0CC0_54C0_03A9"), pod_name="EMC_CIS_1_GM")
    # tapi.pod_add(pod_id=9000, pt_id=str("EMCISMV2_0050_56B3_0CC0_54BF_D4A1"), pod_name="EMC_ISM_v2_GM")
    # tapi.pod_add(pod_id=10000, pt_id=str("DOLPYSEC_0050_56A9_38CC_54B4_797A"), pod_name="NISGTC_PySec_GM")
    # tapi.pod_add(pod_id=11000, pt_id=str("DOLAPV2_0050_56A9_3CF1_54BE_CE1D"), pod_name="NISGTC_APlus_v2_GM")
    # tapi.pod_add(pod_id=12000, pt_id=str("DOLLPINST_0025_9015_B226_50F7_F3AF"), pod_name="NISGTC_LPlus_Install_GM")
    # tapi.pod_add(pod_id=13000, pt_id=str("DOLLP_0025_9015_B226_50B5_47A2"), pod_name="NISGTC_LPlus_Base_GM")
    # tapi.pod_add(pod_id=14000, pt_id=str("DOLNETP_0025_9015_B226_519E_15D6"), pod_name="NISGTC_NetPlus_GM")
    # tapi.pod_add(pod_id=15000, pt_id=str("DOLNSEC_0050_56A9_38CC_53C5_7988"), pod_name="NISGTC_NetSec_GM")
    # tapi.pod_add(pod_id=16000, pt_id=str("DOLSECPV2_0050_56A9_38CC_54C1_5A23"), pod_name="NISGTC_SecPlus_GM")


def pod_clone(src_pid=None, clone_pid_rng=None, clone_pname=None, pc_clone_specs=None):
    """
    Clones an existing pod.

    The pod_clone_task() available via the API is one of the most complex, requested and used of the methods
    available in the API. There are many variables that can be changed to allow cloning of pods to changing
    hardware configurations as well as various pod configurations.

    Required information includes:
    source_pod_id: the numerical pod identifier of the pod you wish to clone, normally this is the Master.
    clone_pod_id: the numerical pod id that you will assign to the pod.
    clone_pod_name: the name given to the cloned instance of the pod.
        - <Program><Course><DataStore><Host><PodId>
          NDG_EH_L_H81_P1001

    Alternate information predominantly include data in the pc_clone_specs that you may need to change for
    operations in your environment. This will normally specify on which host and on which datastore the
    virtual machine will reside.

    The following shows how to specify the pc_clone_specs which sets the datastore "datastore1" on ESXi
    host id 1. To find the vh_id of a host, see the docs for the API method `vm_host_find`.

    pc_clone_specs=[{"clone_datastore": "datastore1", "clone_vh_id": 1}]

    """
    # TODO: JJ/TK: need to ensure that we give a best practice of for enumerating pods and pod naming conventions.
    for pid in clone_pid_rng:
        print(datetime.datetime.now())
        output = tapi.pod_clone_task(source_pod_id=src_pid, clone_pod_id=pid, clone_pod_name=clone_pname+str(pid),
                                     pc_clone_specs=pc_clone_specs)
        print("Cloned Pod: " + str(pid) + '\t' + str(output['status']))


def pod_list():
    """
    Retrievs a list of pods on your NETLAB+ VE system.

    Initially, this method in the API will return
    """
    # Initiate the nlapi.pod_lst() method to bring back a list of dictionaries of key/value pirs of data.

    mlist = tapi.pod_list()

    # If you want an easy way to see your returned values and have values appear in columns you can
    # use the following for loop to iterate through the returned records and print their values:
    for i in mlist:
        output = '{0}\t{1}\t{2}\t{3}\n'.format(str(i['pod_id']), str(i['pod_name']), str(i['pod_desc']),
                                               str(i['pod_uuid']))
        print(output)

    # This will return the contents of the mlist variable to the calling function.
    return mlist


def pod_get(pod_id=int()):
    """
    Retrieves information about an individual pod. Requires pod_id for input.
    """
    result = tapi.pod_get(pod_id=pod_id, properties=['pod_id', 'pod_name', 'pod_desc', 'pod_uuid'])
    print(result)

    return result


def pod_remove(pidrange, remove_vms="DISK"):
    """
    Removes an existing pod from the NETLAB+ pod inventory.

    This is comparable to selecting a pod from the NETLAB+ pod list and clicking "Delete".

    As with the web interface, you can what you do with the virtual machines when you
    execute. The following is the list of valid parameters: 'NONE', 'LOCAL', 'DATACENTER', 'DISK'.

    - 'NONE':  Do not delete any VMs (they will remain in the NETLAB+ inventory)
    - 'LOCAL':  Remove VMs from NETLAB+ inventory only (VMs remains in datacenter)
    - 'DATACENTER': Remove VMs from NETLAB+ inventory and datacenter (VM files not deleted from disk)
    - 'DISK': Remove VMs from NETLAB+ inventory, datacenter, AND delete unshared VM files from disk

    nlapi.pod_remove_task(pod_id=13001, remove_vms="DISK")

    """
    # Check to see if if the pidrange variable is range or int type
    if isinstance(pidrange, range):
        for pid in pidrange:
            # First, set or ensure the pod is set to offline
            tapi.pod_state_change(pod_id=pid, state=PodState.OFFLINE)
            offline_time = datetime.datetime.now()
            print("Pod Offline: " + str(pid) + '\tOK\t' + str(offline_time))
            # Now we can remove the pod.
            result = tapi.pod_remove_task(pod_id=pid, remove_vms=remove_vms)
            removed_time = datetime.datetime.now()
            print("Pod Removed: " + str(pid) + '\t' + str(result['status']) + "\t" + str(removed_time))
    elif isinstance(pidrange, int):
        tapi.pod_state_change(pod_id=pidrange, state=PodState.OFFLINE)
        offline_time = datetime.datetime.now()
        print("Pod Offline: " + str(pidrange) + '\tOK\t' + str(offline_time))
        # Now we can remove the pod.
        result = tapi.pod_remove_task(pod_id=pidrange, remove_vms=remove_vms)
        removed_time = datetime.datetime.now()
        print("Pod Removed: " + str(pidrange) + '\t' + str(result['status']) + "\t" + str(removed_time))


def pod_online(pidrange):
    """
    Brings pod or pods online.

    This function accepts either an integer for the pod_id or a range object.
    You can specify a range of pods that you wish to loop through or an individul pod id.

    pod_online(1001) or pod_online(range(1001, 1011))

    Uses the pod_state_changed() method in the NETLAB+ API.
    """
    if isinstance(pidrange, range):
        for pid in pidrange:
            tapi.pod_state_change(pod_id=pid, state=PodState.OFFLINE)
            print("Brought Online: " + str(pid) + "\tOK")
    elif isinstance(pidrange, int):
        tapi.pod_state_change(pod_id=pidrange, state=PodState.OFFLINE)
        print("Brought Online: " + str(pidrange) + "\tOK")


def pod_offline(pidrange):
    """
    Takes pod or pods offline.

    This function accepts either an integer for the pod_id or a range object.
    You can specify a range of pods that you wish to loop through or an individul pod id.

    pod_offline(1001) or pod_offline(range(1001, 1011))

    Uses the pod_state_changed() method in the NETLAB+ API.
    """
    if isinstance(pidrange, range):
        for pid in pidrange:
            tapi.pod_state_change(pod_id=pid, state=PodState.OFFLINE)
            print("Brought Offline: " + str(pid) + "\tOK")
    elif isinstance(pidrange, int):
        tapi.pod_state_change(pod_id=pidrange, state=PodState.OFFLINE)
        print("Brought Offline: " + str(pidrange) + "\tOK")


def user_list(search_param=''):
    """
    List users and restrict the output to a passed search parameter.

    user_list('student1')
    """
    temp_list = tapi.user_account_list()
    del_acc_ids = []
    for x in temp_list:
        if x['acc_user_id'].startswith(search_param):
            ret_acc_id = x['acc_id']
            ret_acc_user_id = x['acc_user_id']
            print('acc_id=' + str(ret_acc_id) + '\tacc_user_id=' + str(ret_acc_user_id))
            del_acc_ids.append(ret_acc_id)
    return del_acc_ids


def user_add(com_id, acc_user_id, acc_password, acc_full_name, acc_type="S", cls_id=None):
    """
    Add a user to your system.

    You can add other parameters to the user_account_add() method.

    Other parameters  that may be of interest:

    - cls_id : Class ID will allow you to add the user to a class when creating the user.
    - tz_id : Time Zone ID allows you set the set the time zone for the user upon creation.
    - acc_type: Account Type, "S" for student and "I" for instructor accounts.

    user_add(com_id, acc_user_id, acc_password, acc_full_name, acc_type="S",
            cls_id, tz_id, acc_display_name, acc_sort_name, acc_email )
    """

    tapi.user_account_add(com_id=com_id, acc_user_id=acc_user_id, acc_password=acc_password,
                          acc_full_name=acc_full_name, acc_type=acc_type, cls_id=cls_id)
    return


def user_del(search_param=''):
    """
    Delete a user from the system.

    user_del('student1')
    """
    del_list = user_list(search_param=search_param)
    for x in del_list:
        tapi.user_account_remove(acc_id=x)
        print('acc_id=' + str(x) + '\tdeleted')
    return


def class_add(cls_name, com_id):
    """
    Adds a class to system.

    class_add(cls_name, com_id)

    cls_name: The name of the class
    com_id: The community ID that the class belongs to.

    """
    # TODO: JJ: What if com_id is not known? - Can go to web gui and obtain?
    result = tapi.class_add(cls_name=cls_name, com_id=com_id)
    print(result)
    return result


def class_remove(cls_id, delete_students=False):
    """
    Removes a class from system.

    class_remove(cls_id, delete_students=False)

    cls_id: Class ID - can be obtained via class_list() method.
    """
    tapi.class_remove(cls_id=cls_id, delete_students=delete_students)


def class_get(cls_id):
    """
    Gets information about class.


    """
    result = tapi.class_get(cls_id=cls_id)
    print(result)
    return result


def class_list(com_id='1'):
    """
    List available classes on system.


    """
    result = tapi.class_list(com_id=com_id)
    for iklass in result:
        print('output: \t' + str(iklass['cls_id']) + '\t' + iklass['cls_name'] + '\t' + iklass['cls_uuid'] + '\n')
    return


def lplus_base():
    # Specify the pod id of the master pod.
    pod_master = 13000

    # pod_rng specifies a linear range of pod id's that you wish to manipulate.
    pod_rng = range(13006, 13008)

    # Set a prefix for pod identification.
    # A good prefix will include identifiers for course/lab set, datastore location and host. In the sample
    # below we also supply a P at the end as the pod_id will be attached to it, please see pod_clone().
    pod_prefix = 'LPlus_Base_L_H81_P'

    pod_clone(src_pid=pod_master, clone_pid_rng=pod_rng, clone_pname=pod_prefix,
              pc_clone_specs={"clone_datastore": "MCNC_HOST81_LOCAL", "clone_vh_id": 1})
    # Uncomment the following if you wish to bring pods online. You can change the pod_online()
    # function to pod_offline() to take the pods offline.
    # for i in pod_rng:
    #     pod_online(i)
    # Uncomment the following line to remove the pods in the pod id range (pod_rng) passed to the function.
    # pod_remove(pod_rng)
