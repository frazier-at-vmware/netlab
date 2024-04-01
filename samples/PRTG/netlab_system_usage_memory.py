import asyncio

import json
import sys

from netlab.async_client import NetlabClient
from paepy.ChannelDefinition import CustomSensorResult  # type: ignore


async def main():
    # interpret first command line parameter as json object
    if len(sys.argv) == 1:
        # for command line debugging, use the default system
        sys_args = '{"params": "default"}'
    else:
        sys_args = sys.argv[1]
    prtg = json.loads(sys_args)
    system = prtg.get('params', "default").lower()

    # PRTG runs sensors as a different user. Specify the Administrator user's netlab config file here
    async with NetlabClient(system, config_path='C:/Users/Administrator/.netlab/config.json') as client:
        # query data from netlab api
        response = await client.system_usage_memory()

        total_b = response['ram']['total_b']
        free_b = response['ram']['free_b']
        free_pct = int((free_b / total_b) * 100)

        # create sensor result
        result = CustomSensorResult("OK")

        # add primary channel for percentage of free memory
        result.add_channel(channel_name="Percent Free Memory", primary_channel=True, unit='Percent', value=free_pct)

        # additional channels for remaining values
        result.add_channel(channel_name="Free Memory", unit="BytesMemory", value=free_b)
        result.add_channel(channel_name="Total Memory", unit="BytesMemory", value=total_b)

        # print sensor result to stdout
        print(result.get_json_result())


if __name__ == "__main__":
    asyncio.run(main())
