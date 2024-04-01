import json
import sys

from netlab.client import Client
from paepy.ChannelDefinition import CustomSensorResult  # type: ignore

if __name__ == "__main__":
    # interpret first command line parameter as json object
    if len(sys.argv) == 1:
        # for command line debugging, use the default system
        sys_args = '{"params": "default"}'
    else:
        sys_args = sys.argv[1]
    prtg = json.loads(sys_args)
    system = prtg.get('params', "default").lower()

    # PRTG runs sensors as a different user. Specify the Administrator user's netlab config file here
    client = Client(system, config_path='C:/Users/Administrator/.netlab/config.json')

    # query data from netlab api
    response = client.system_usage_cpu()

    # create sensor result
    result = CustomSensorResult("OK")

    # add primary channel for "all" CPU
    total = response.pop('all')
    total_load = 100 - total['idle_pct']
    result.add_channel(channel_name="Total", primary_channel=True, unit='Percent',
                       value=float(total_load), is_float=True)

    # additional channel for each individual CPU
    for cpu, values in response.items():
        cpu_load = 100 - values['idle_pct']
        result.add_channel(channel_name="Processor {}".format(cpu), unit="Percent",
                           value=float(cpu_load), is_float=True)

    # print sensor result to stdout
    print(result.get_json_result())
