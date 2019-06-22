import click
import os
import logging
import configuration
import logger
        
logger.setup_logging()

logger = logging.getLogger('k2_cli')
info = logger.info
debug = logger.debug


class K2CliError(Exception):
    pass

@click.group()
def k2():
    pass

@click.command()
@click.argument('application')
def install(application):
    info('Installing {application}'.format(application=application))
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


    