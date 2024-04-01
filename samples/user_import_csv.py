import csv
import os
import sys
from typing import Any

from netlab.client import Client
from netlab.errors.common import NetlabError

#####################
# Variables to change
#####################

COMMUNITY_ID = 1  # User accounts must belong to a community.
CLASS_ID = None  # All users will be added directly to this class during account creation.
# Set CLASS_ID to None if you don't want to enroll users into a class automatically.
DEFAULT_INITIAL_PASSWORD = 'CHANGEMEPLEASE'  # can be overidden per user by including acc_password in the CSV
NETLAB_SYSTEM = 'DEMO'  # must be a valid entry in your config.json

#################################################################
# Don't change the code below unless you know what you are doing.
#################################################################

try:
    # Pass a filename as the first argument to the script
    user_csv_file = sys.argv[1]
except IndexError:
    # Or default to users.csv
    user_csv_file = 'users.csv'

print("Opening {}".format(user_csv_file))

if not os.path.exists(user_csv_file):
    print("    File not found!")
    sys.exit(1)
else:
    print("  -> Beginning user import")

client = Client(NETLAB_SYSTEM)
users_created = 0
users_with_errors = 0

with open(user_csv_file) as csvfile:
    reader = csv.DictReader(csvfile)
    row: Any
    for row in reader:
        # Use the default password if acc_password is not a column in the csv or if it is empty
        if not row.get('acc_password', ''):
            row['acc_password'] = DEFAULT_INITIAL_PASSWORD

        try:
            acc_id = client.user_account_add(com_id=COMMUNITY_ID, cls_id=CLASS_ID, **row)
        except NetlabError as err:
            # The server returned an error. The exception will contain more information about the error.
            users_with_errors += 1
            print("  -! {}".format(err))
        else:
            users_created += 1
            print("  -+ Created user {} with id {}".format(row['acc_user_id'], acc_id))

print("\nSuccessfully imported {} new users.".format(users_created))
if users_with_errors > 0:
    print("There were {} errors encountered. Please review the output above.".format(users_with_errors))
