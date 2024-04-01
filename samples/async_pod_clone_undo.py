import asyncio

from netlab.async_client import NetlabClient
from netlab import enums

POD_RANGE = range(900, 910)


async def remove_pod(client, pod_number):
    await client.pod_state_change(pod_id=pod_number, state=enums.PodState.OFFLINE)
    await client.pod_remove_task(pod_id=pod_number, remove_vms=enums.RemoveVMS.DISK)

    return pod_number


async def main():
    async with NetlabClient() as client:
        for pod_task in asyncio.as_completed([
            remove_pod(client, i) for i in POD_RANGE
        ]):
            pod_name = await pod_task

            print(f'Removed pod: {pod_name}')


if __name__ == '__main__':
    asyncio.run(main())
