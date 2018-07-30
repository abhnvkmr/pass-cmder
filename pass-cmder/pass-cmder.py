import click

@click.group()
def pass_cmder():
    click.echo("Welcome to Password Commander")
 

@pass_cmder.command()
@click.argument('website')
@click.argument('key')
@click.argument('password', required=False)
def add(website, key, password):
    """Add a new credential to the store"""
    if password is None:
        password = input('Enter the password for ' + key + " at " + website)
    data = {
        'service': website,
        'key': key,
        'password': password
    }
    click.echo('Hello')


@pass_cmder.command()
@click.argument('website')
@click.option('--all', default=False)
def remove(website, should_remove_all):
    pass


if __name__ == '__main__':
    pass_cmder()
