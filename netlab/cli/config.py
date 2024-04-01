import asyncio
import click
import sys
from netlab.auth import load_config, add_config, remove_config

from ..async_client import NetlabClient
from .utils import print_exception, output


@click.group(invoke_without_command=True)
@click.option('--system', default=None, help="Only show settings from a specific NETLAB+ system.")
@click.pass_context
def config(ctx, system):
    """ Manage config.json settings """
    if ctx.invoked_subcommand is None:
        systems = {}
        system_configs = load_config(system)

        if not system_configs:
            click.secho("No config settings present. See below on how to add them.", fg='red', bg='white')
            click.echo()
            click.echo(ctx.get_help())
            ctx.exit(0)

        if system:
            systems[system] = system_configs
        else:
            systems = system_configs

        for system, conf in systems.items():
            click.echo('System: {}'.format(click.style(system, fg='cyan')))
            output(conf)
            click.echo()
        click.echo("To learn more about modifying these settings, display the help text by running:")
        click.secho("    {} {}".format(ctx.command_path, ctx.help_option_names[0]), fg='cyan')


@config.command()
@click.option('--system', default='default', help="A friendly name to identify this NETLAB+ system. Leave blank for "
                                                  "'default'.")
@click.option('--host', prompt=True, help="IP Address or hostname of remote NETLAB+ API.")
@click.option('--user', prompt=True, help="User account ID from NETLAB+ system.")
@click.option('--token', prompt=True, help="Token obtained from NETLAB+ system.")
@click.option('--port', type=click.INT, help="TCP port to connect to the remote NETLAB+ API. Defaults to 9000.")
def add(system, host, user, token, port):
    """ Add a new system with all required settings """
    current_config = load_config()
    if system in current_config:
        click.confirm('\nYou already have a system named {}. If you continue, the existing one will be overwritten. '
                      'Are you sure?'.format(click.style(system, fg='cyan')), abort=True)

    new_config = {
        'host': host,
        'user': user,
        'token': token,
    }

    if port:
        new_config['port'] = port

    add_config(system, new_config)
    click.secho("Success!", fg='green')


@config.command()
@click.pass_context
@click.option('--system', help="The NETLAB+ system to remove. Required.")
@click.option('--confirm', is_flag=True, help="Skips the prompt to confirm removal. This will remove the "
                                              "config without warning. {warning}"
              .format(warning=click.style("Use at your own risk!", bg='white', fg='red')))
@click.option('--all', 'all_systems', is_flag=True, help="Removes all systems and settings. Resets your "
                                                         "config.json back to nothing.")
def remove(ctx, system, confirm, all_systems):
    """ Remove all settings for a system """
    if not system and not all_systems:
        click.echo(ctx.get_help())
        ctx.exit(0)

    if all_systems:
        system = None
        confirm_message = 'You are about to remove the settings for {} the systems. Are you sure?'.format(
            click.style("all", fg='red'))
        end_message = 'All systems have been removed.'
    else:
        confirm_message = 'You are about to remove the settings for the {} system. Are you sure?'.format(
            click.style(system, fg='cyan'))
        end_message = 'The {} system has been removed.'.format(click.style(system, fg='cyan'))

    if not confirm:
        click.secho("\nWARNING!", fg='red')
        click.confirm(confirm_message, abort=True)

    remove_config(system)
    click.echo(end_message)


@config.command(name='set')
@click.option('--system', default='default', help="The NETLAB+ system to modify the settings.")
@click.argument('settings', nargs=-1)
def set_value(system, settings):
    """ Set one or more settings for a specific system """
    current_config = load_config(system)

    new_settings = {}
    for setting in settings:
        key, value = setting.split('=')
        new_settings[key.lower()] = value

    new_config = {}
    new_config.update(current_config)
    new_config.update(new_settings)
    add_config(system, new_config)

    click.secho("Success!", fg='green')
    click.echo("Updated the config file with the following:\n")
    output(new_settings, headers=['Setting', 'New Value'])


@config.command()
@click.option('--system', default='default', help="The NETLAB+ system to get settings from.")
@click.option('--oneline', is_flag=True)
@click.argument('settings', nargs=-1)
def get(system, oneline, settings):
    """ Get the current value of one or more settings for a specific system """
    current_config = load_config(system)
    gathered_settings = []

    for setting in settings:
        try:
            current_setting_value = current_config[setting]
        except KeyError:
            # if the setting is not present in config.json, then ommit it from the results
            pass
        else:
            gathered_settings.append([setting, current_setting_value])

    if oneline:
        settings_string = " ".join(["=".join(setting) for setting in gathered_settings])
        click.echo(settings_string)
    else:
        click.echo('System: {}\n'.format(click.style(system, fg='cyan')))
        output(gathered_settings, headers=['Setting', 'Value'])


@config.command()
@click.option('--system', default='default', help="The NETLAB+ system to test connection to.")
def test(system):
    """ Test that the system settings can connect successfully to the server"""
    return asyncio.run(_async_test(system))


async def _async_test(system):
    try:
        async with NetlabClient(system) as netlab_client:
            results = await netlab_client.system_status_get()
    except Exception as e:
        print_exception(e)
        sys.exit(1)

    click.secho("Test connection successful!\n", fg='green')
    output(results)
