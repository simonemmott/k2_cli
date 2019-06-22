import click

@click.group()
def k2():
    pass

@click.command()
@click.argument('application')
def install(application):
    click.echo('Install {application}!'.format(application=application))
    
k2.add_command(install)
    
@click.group()
def app():
    pass

k2.add_command(app)

@click.command()
def list():
    click.echo('Application List')
app.add_command(list)

if __name__ == '__main__':
    k2()


    