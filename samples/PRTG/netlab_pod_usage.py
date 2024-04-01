import asyncio
from typing import DefaultDict
import json
import sys
from collections import defaultdict

from paepy.ChannelDefinition import CustomSensorResult  # type: ignore

from netlab.async_client import NetlabClient


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
        total: DefaultDict[int, int] = defaultdict(int)
        used: DefaultDict[int, int] = defaultdict(int)

        for pod in await client.pod_list():
            total[pod['pt_id']] += 1
            if pod['pod_res_id']:
                used[pod['pt_id']] += 1

        pod_types = {pt['pt_id']: pt['pt_name'] for pt in await client.pod_types_list()}

        # create sensor result
        result = CustomSensorResult("OK")

        # add primary channel for total pods reserved
        total_pods = sum(total.values())
        used_pods = sum(used.values())
        total_used_pct = (used_pods / total_pods) * 100
        result.add_channel(channel_name="Overall Percent Used", primary_channel=True, unit='Percent',
                           value=int(total_used_pct), is_float=False)

        # additional channel for each individual pod type percent, used and total
        for pt_id, total_count in total.items():
            used_count = used[pt_id]
            used_pct = (used_count / total_count) * 100
            result.add_channel(channel_name="% - {}".format(pod_types[pt_id]), unit="Percent",
                               value=int(used_pct), is_float=False)
            result.add_channel(channel_name="Total - {}".format(pod_types[pt_id]), unit="Count",
                               value=total_count, is_float=False)
            result.add_channel(channel_name="Used - {}".format(pod_types[pt_id]), unit="Count",
                               value=used_count, is_float=False)

        # print sensor result to stdout
        print(result.get_json_result())

asyncio.run(main())
