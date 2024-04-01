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
        response = await client.system_usage_disk()
        data_free_space = int(100 - response['data']['used_pct'])
        data_free_bytes = response['data']['total_b'] - response['data']['used_b']
        programs_free_space = int(100 - response['programs']['used_pct'])
        programs_free_bytes = response['programs']['total_b'] - response['programs']['used_b']

        # create sensor result
        result = CustomSensorResult("OK")

        # add primary channel for percentage of data partition free space
        result.add_channel(channel_name="Free Space - data", primary_channel=True, unit='Percent',
                           value=data_free_space, is_limit_mode=True, limit_min_warning=25, limit_min_error=10)

        # additional channels for remaining values
        result.add_channel(channel_name="Free Bytes - data", unit="BytesDisk", value=data_free_bytes)
        result.add_channel(channel_name="Free Space - programs", unit="Percent", value=programs_free_space)
        result.add_channel(channel_name="Free Bytes - programs", unit="BytesDisk", value=programs_free_bytes)

        # print sensor result to stdout
        print(result.get_json_result())


if __name__ == "__main__":
    asyncio.run(main())
