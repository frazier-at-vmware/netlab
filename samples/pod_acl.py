import asyncio

from netlab.async_client import NetlabClient
from netlab.errors.common import NetlabError

#####################
# Variables to change
#####################

COM_ID = 1  # community this is for
CLS_ID = 99  # class to get roster from
NETLAB_SYSTEM = 'DEMO'  # must be a valid entry in your config.json

# Make a list of pod ids, first one is for first student, second is for second student, and so on.
# Must have the same number of list items as number of students in class.
POD_IDS = [1001, 1002, 1003, 1004, 1005]

#########################
# Don't modify code below
#########################


async def main():
    async with NetlabClient(NETLAB_SYSTEM) as client:
        acls_created = 0
        acls_with_errors = 0

        # Get list of student IDs in a particular class
        student_ids = [student['acc_id'] for student in await client.class_roster_list(cls_id=CLS_ID, leads=False)]

        assert len(student_ids) == len(POD_IDS), "There are not the same number of pods and students"

        # Loop through student_ids and add a pod acl for the corresponding pod in POD_IDS list
        for index, acc_id in enumerate(student_ids):
            try:
                pod_id = POD_IDS[index]

                # create pod acl
                await client.pod_acl_add(com_id=COM_ID, pod_id=pod_id, acc_id=acc_id)

                # enable ACLs on the pod itself
                await client.pod_update(pod_id=POD_IDS[index], pod_acl_enabled=True)
            except NetlabError as err:
                # The server returned an error. The exception will contain more information about the error.
                acls_with_errors += 1
                print("  -! {}".format(err))
            else:
                print("  -> Creating ACL for pod {} and user {}".format(pod_id, acc_id))
                acls_created += 1

        print("\nSuccessfully created {} Pod ACLs.".format(acls_created))
        if acls_with_errors > 0:
            print("There were {} errors encountered. Please review the output above.".format(acls_with_errors))


asyncio.run(main())
