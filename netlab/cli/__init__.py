from typing import Any
import asyncio
# TODO Backport in stdlib in py3.8
from importlib_metadata import version as get_version

import click
import platform

from .api import api
from .config import config
from .utils import print_exception
from ..async_client import NetlabClient

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass


@main.command()
@click.option('--system', default='default', help="The NETLAB+ system to get server version from. Leave blank for "
                                                  "'default'.")
def version(system):
    """ Show the client, server, Python, and OS versions"""

    asyncio.run(_async_version(system))


async def _async_version(system):
    results: Any
    try:
        async with NetlabClient(system) as client:
            results = await client.system_status_get()
    except Exception as e:
        results = {}
        print_exception(e)
        click.echo('')
    server_version = results.get('sys_sdn_version', click.style("Unable to connect to server", fg='red'))

    click.echo('NETLAB+ Server : {}'.format(server_version))
    click.echo('Python Client  : {}'.format(get_version('netlab')))
    click.echo('Python Version : {}'.format(platform.python_version()))
    click.echo('OS Platform    : {}'.format(platform.platform()))


# manually setup top level command groups
main.add_command(api)
main.add_command(config)
