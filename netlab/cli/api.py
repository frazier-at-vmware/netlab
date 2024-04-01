import asyncio
import csv
import io
import sys

import click

from .utils import print_exception, output, resolve_enum
from ..constants import NL_OK
from ..errors.common import InvalidVersion, NetlabError
from ..serializer import serialize, ENUMS
from ..async_client import NetlabClient


@click.command()
@click.pass_context
@click.argument('method', nargs=1)
@click.argument('arguments', nargs=-1)
@click.option('--system', default='default', help="NETLAB+ system to communicate with.")
@click.option('--output', 'output_type', default='table', type=click.Choice(['table', 'csv', 'tsv', 'json', 'var']))
def api(ctx, method, arguments, system, output_type):
    """ Communicate with a remote NETLAB+ server API"""
    return asyncio.run(
        _async_api(ctx, method, arguments, system, output_type)
    )


async def _async_api(ctx, method, arguments, system, output_type):
    try:
        async with NetlabClient(system) as netlab_client:
            api_method = getattr(netlab_client, method, None)
            if api_method is None:
                click.echo("{} is not a valid API method. Please check the documentation.".format(
                    click.style(method, fg='red')))
                ctx.exit(1)
            assert api_method is not None

            api_arguments = {}
            try:
                for arg in arguments:
                    key, value = arg.split('=')
                    key = key.lower()
                    if key in ENUMS:
                        enum = ENUMS[key]
                        value = resolve_enum(enum, value, param=key)
                    api_arguments[key.lower()] = value
            except ValueError:
                # user probably didn't pass arguments in the key=value format
                click.secho("There is an error with your method arguments.", fg='red')
                click.secho("Please ensure they are in the format of arg=value. \n\nExample:")
                click.secho("    {} user_account_get acc_id=100001".format(ctx.command_path), fg='cyan')
                ctx.exit(1)

            try:
                results = await api_method(**api_arguments)
            except (TypeError, NetlabError, InvalidVersion) as err:
                results = None
                click.secho("{}: {}".format(type(err).__name__, err), fg='red')
                click.echo("Please check the documentation for help.")
                ctx.exit(1)

            if results == NL_OK:
                click.secho("Success!", fg='green')
            elif isinstance(results, int) or isinstance(results, str):
                click.echo(results)
            else:
                outputs = {
                    'table': table_output,
                    'csv': csv_output,
                    'tsv': tsv_output,
                    'json': json_output,
                    'var': var_output
                }
                outputs[output_type](results)  # type: ignore

    except Exception as e:
        print_exception(e)
        sys.exit(1)


def table_output(results):
    if isinstance(results, dict):
        results = [results]
    output(results, headers='keys')


def csv_output(results, delimiter=','):
    out = io.StringIO()

    if isinstance(results, dict):
        results = [results]

    fieldnames = list(results[0].keys())

    writer = csv.DictWriter(out, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, delimiter=delimiter)
    writer.writeheader()
    for result in results:
        writer.writerow(result)
    click.echo(out.getvalue())


def tsv_output(results):
    csv_output(results, delimiter='\t')


def json_output(results):
    click.echo(serialize(results, pretty=True))


def var_output(results):
    if isinstance(results, dict):
        results = [results]

    out = []
    for result in results:
        row = ""
        for key, value in result.items():
            row += "{}={} ".format(key, value)
        out.append(row)
    click.echo("\n".join(out))
