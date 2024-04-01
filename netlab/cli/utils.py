import json
import socket
import sys
import ssl

import click
from ..errors.common import AuthenticationError, InvalidConfig
from tabulate import tabulate


def print_exception(exception: Exception):
    if isinstance(exception, InvalidConfig):
        click.secho("{}: {}".format(type(exception).__name__, exception), fg='red')
        click.secho("Check your config.json file for errors.")
    elif isinstance(exception, json.JSONDecodeError):
        click.secho("{}: {}".format(type(exception).__name__, exception), fg='red')
        click.secho("Your config.json file has syntax errors and cannot be decoded.")
    elif isinstance(exception, AuthenticationError):
        click.secho("{}: {}".format(type(exception).__name__, exception), fg='red')
        click.secho("Check your API key for problems. Make sure you are using the correct user, token, and source "
                    "IP address. Make sure your API key is active.")
    elif isinstance(exception, socket.error):
        click.secho("{}: {}".format(type(exception).__name__, exception), fg='red')
        click.secho("Problem connecting to the Remote API socket. Check that the Remote API is enabled. "
                    "Wait one minute and try again. Also ensure the host setting is correct.")
    elif isinstance(exception, ssl.CertificateError):
        click.secho("{}: {}".format(type(exception).__name__, exception), fg='red')
        click.secho("Problem with host ssl certificate. Check to make sure ssl is configured correctly.")
    else:
        click.secho("{}: {}".format(type(exception).__name__, exception), fg='red')
        click.secho("Please conntact NDG support.")


def output(data, tablefmt='pipe', headers=(), **kwargs):
    """ Helper function to output data in tables. Accepts tabulate and click.secho options. """
    try:
        click.secho(tabulate(data.items(), tablefmt=tablefmt, headers=headers), **kwargs)
    except AttributeError:
        click.secho(tabulate(data, tablefmt=tablefmt, headers=headers), **kwargs)


def resolve_enum(enum, value, param):
    error = False
    if '.' in value:
        # User used full name.  (ex `AccountType.INSTRUCTOR`)
        try:
            name, value = value.split('.')
        except ValueError:
            click.secho("Enum, {}, in improper format.".format(enum.__name__), fg='red')
            error = True
        if name != enum.__name__:
            click.secho("Enum, {}, does not match the expected enum, {}.".format(name, enum.__name__), fg='red')
            error = True
    try:
        return enum[value]
    except KeyError:
        # Not a key
        pass
    try:
        return enum(value)
    except ValueError:
        # also not a value
        click.secho("Enum, {}, does not have a key or value {}.".format(enum.__name__, value), fg='red')
        error = True
    if error:
        click.secho("Parameter, {}, takes a {} and has the following possible values.".format(param, enum.__name__))
        for member in enum.__members__:
            print('  - ', member)
        sys.exit(1)
