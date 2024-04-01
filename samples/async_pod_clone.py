import asyncio

from netlab.async_client import NetlabClient, NetlabConnection
from netlab import enums

SOURCE_POD_ID = 9000
POD_NAME_TEMPLATE = 'example_pod_{}'
POD_RANGE = range(900, 910)


async def clone_pod(client: NetlabConnection, pod_number: int):
    pod_name = POD_NAME_TEMPLATE.format(pod_number)

    await client.pod_clone_task(
        source_pod_id=SOURCE_POD_ID,
        clone_pod_id=pod_number,
        clone_pod_name=pod_name,
        pc_clone_specs=[{
            "source_snapshot": "master",
            "clone_snapshot": "master",
        }])
    await client.pod_state_change(pod_id=pod_number, state=enums.PodState.ONLINE)

    return pod_name


async def main():
    async with NetlabClient() as client:
        for pod_task in asyncio.as_completed([
            clone_pod(client, i) for i in POD_RANGE
        ]):
            pod_name = await pod_task

            print(f'Cloned pod: {pod_name}')


if __name__ == '__main__':
    asyncio.run(main())
