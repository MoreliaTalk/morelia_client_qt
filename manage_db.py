"""
    Copyright (c) 2020 - present NekrodNIK, Stepan Skriabin, rus-ai and other.
    Look at the file AUTHORS.md(located at the root of the project) to get the full list.

    This file is part of Morelia Server.

    Morelia Server is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Morelia Server is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with Morelia Server. If not, see <https://www.gnu.org/licenses/>.
"""

from time import process_time
import click

from modules.database.clientdb import ClientDb


@click.command()
@click.option("--db",
              type=click.Choice(["create", "delete"]),
              help='Create database and tables. '
                   'Delete all tables with data.')
@click.option('--show',
              type=click.Choice(["flow", "messages"]),
              help='Show all flow ordered by last message time. '
                   'Show all messages in specified flow (need --flowid)')
@click.option('--user',
              type=click.Choice(["add", "delete"]),
              help='Create or delete user record in the database. '
                   '(need --uuid --username)')
@click.option('--flow',
              type=click.Choice(["add", "delete"]),
              help='Create or delete flow record in the database. '
                   '(need --uuid --title)')
@click.option('--message',
              type=click.Choice(["add", "delete"]),
              help='Create or delete message record in the database. '
                   '(need --uuid --text --time --flowid --userid)')
@click.option('--uuid',
              help='uuid for adding or deleting user, flow, message.')
@click.option('--username',
              help='username for adding user.')
@click.option('--title',
              help='title for adding flow.')
@click.option('--text',
              help='text for adding message.')
@click.option('--time',
              help='time for adding message.')
@click.option('--flowid',
              help='flowid for adding message.')
@click.option('--userid',
              help='userid for adding message.')
@click.option('--config',
              type=click.Choice(["get", "set", "delete"]),
              help='Get, set or delete configuration parameter. '
                   '(need --param --value)')
@click.option('--param',
              help='Parameter name to set< get or delete in config.')
@click.option('--value',
              help='Parameter value to set in config.')
def main(db, show, user, flow, message, uuid, username, title, text,
         time, flowid, userid, config, param, value):
    clientDb = ClientDb()
    if db == "create":
        start_time = process_time()
        clientDb.create_db()
        click.echo(f'Database structure is created at: '
                   f'{process_time() - start_time} sec.')
    elif db == "delete":
        start_time = process_time()
        clientDb.delete_tables()
        click.echo(f'Database table is dropped at: '
                   f'{process_time() - start_time} sec.')
    if user == "add":
        if uuid and username:
            start_time = process_time()
            clientDb.add_user(uuid, username)
            click.echo(f'User added at: '
                       f'{process_time() - start_time} sec.')
        else:
            click.echo(f'Both uuid and login must be specified.')
    if flow == "add":
        if uuid and title:
            start_time = process_time()
            clientDb.add_flow(uuid, title)
            click.echo(f'Flow added at: '
                       f'{process_time() - start_time} sec.')
        else:
            click.echo(f'Both uuid and title must be specified for flow.')
    if message == "add":
        if uuid and text and time and userid and flowid:
            start_time = process_time()
            clientDb.add_message(uuid, text, int(time), userid, flowid)
            click.echo(f'Message added at: '
                       f'{process_time() - start_time} sec.')
        else:
            click.echo(f'All text, time, userid and flowid must be specified for flow.')
    if show == "flow":
        start_time = process_time()
        for line in clientDb.list_flow():
            click.echo(line)
        click.echo(f'Select flow list at: '
                   f'{process_time() - start_time} sec.')
    elif show == "messages":
        if flowid:
            start_time = process_time()
            for line in clientDb.list_messages(flowid):
                click.echo(line)
            click.echo(f'Select message list at: '
                       f'{process_time() - start_time} sec.')
        else:
            click.echo(f'Flowid must be specified for flow.')
    if config == "get":
        if param:
            click.echo(f'{param}={clientDb.get_param(param, "[Value not set]")}')
        else:
            click.echo(f'Param name must be specified for get it.')
    elif config == "set":
        if param and value:
            clientDb.set_param(param, value)
        else:
            click.echo(f'Param name and Value must be specified for set it.')
    elif config == "delete":
        if param:
            clientDb.delete_param(param)
        else:
            click.echo(f'Param name must be specified for delete it.')


if __name__ == "__main__":
    main()
