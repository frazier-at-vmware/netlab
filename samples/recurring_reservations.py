import asyncio
from datetime import datetime, timedelta

from netlab.async_client import NetlabClient
from netlab.errors.common import NetlabError
from netlab.errors.user import AccountNotFoundError
from netlab.enums import ReservationType

#####################
# Variables to change
#####################

POD_ID = 4402  # The pod to reserve
CLASS_ID = 2  # The class this reservation is for. Can only be set to None if the type below is INSTRUCTOR
RESERVATION_TYPE = ReservationType.ILT_CLASS  # choose from ('INDIVIDUAL'|'ILT_CLASS'|'TEAM'|'INSTRUCTOR')
RESERVATION_USERNAME = ''  # This is the user you want to make the reservation for.
EXERCISE_ID = ""

RESERVATION_TIME_ZONE = 'America/Chicago'  # Find your IANA timezone here - https://ndg.tech/hReahU
RESERVATION_START_TIME = '09:00'  # in HH:MM format, 24 hour time
RESERVATION_END_TIME = '12:00'  # in HH:MM format, 24 hour time
RESERVATION_FIRST_DAY = '2017-01-23'  # in YYYY-MM-DD format
RESERVATION_LAST_DAY = '2017-05-12'  # in YYYY-MM-DD format
# days of the week the reservations should be created, separated by spaces: M T W Th F Sa Su
RESERVATION_REPEAT_DAYS = 'M W F'  # This will repeat on Monday, Wednesday and Friday

NETLAB_SYSTEM = 'DEMO'  # must be a valid entry in your config.json

#########################
# Don't modify code below
#########################


async def main():
    days_of_the_week = ['M', 'T', 'W', 'Th', 'F', 'Sa', 'Su']
    repeat_days = RESERVATION_REPEAT_DAYS.split(" ")

    async with NetlabClient(NETLAB_SYSTEM) as client:
        reservations_created = 0
        reservations_with_errors = 0

        # find acc_id by looking up the username
        results = await client.user_account_search(
            properties=['acc_id'], filter={'acc_user_id': RESERVATION_USERNAME}, page=1)
        if results['data']:
            acc_id = results['data'][0]['acc_id']
        else:
            raise AccountNotFoundError(RESERVATION_USERNAME)

        # turn date strings into datetime objects
        first_day = datetime.strptime("{}".format(RESERVATION_FIRST_DAY), '%Y-%m-%d')
        last_day = datetime.strptime("{}".format(RESERVATION_LAST_DAY), '%Y-%m-%d')

        # loop through all the days between first and last day, inclusive
        current_day = first_day
        while current_day <= last_day:
            current_day_of_the_week = days_of_the_week[current_day.weekday()]
            if current_day_of_the_week in repeat_days:
                start_time = datetime.strptime('{} {}'.format(current_day.strftime('%Y-%m-%d'), RESERVATION_START_TIME),
                                               '%Y-%m-%d %H:%M')
                end_time = datetime.strptime('{} {}'.format(current_day.strftime('%Y-%m-%d'), RESERVATION_END_TIME),
                                             '%Y-%m-%d %H:%M')
                try:
                    await client.reservation_make(
                        type=RESERVATION_TYPE, pod_id=POD_ID, cls_id=CLASS_ID, start_time=start_time,
                        end_time=end_time, acc_id=acc_id, tz_olson=RESERVATION_TIME_ZONE,
                        ex_id=EXERCISE_ID)
                except NetlabError as err:
                    # The server returned an error. The exception will contain more information about the error.
                    reservations_with_errors += 1
                    print("  -! {}".format(err))
                else:
                    print("  -> Creating reservation at {}".format(start_time))
                    reservations_created += 1
            current_day += timedelta(days=1)

        print("\nSuccessfully created {} new reservations.".format(reservations_created))
        if reservations_with_errors > 0:
            print("There were {} errors encountered. Please review the output above.".format(reservations_with_errors))


if __name__ == '__main__':
    asyncio.run(main())
