# flake8: noqa
import asyncio
from netlab.async_client import NetlabClient


# Create a function that we can use `await` in
async def main():
    # Create and connect the NetlabConnection
    async with NetlabClient() as client:

        # List communities
        result = await client.user_community_list()
        print('>>>>', result)
        # List used pod ids
        result = await client.pod_list_used_ids()
        print('>>>>', result)

        # Iterate over user accounts
        async for user in client.user_account_search_iter(properties=['acc_id']):
            print(user)

        # Make 10 requests simultaneously
        result = await asyncio.gather(*[client.user_account_search(properties=['acc_id'], page=1) for i in range(10)])
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
