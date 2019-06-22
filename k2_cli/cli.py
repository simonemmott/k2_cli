import click
import os
import logging
import configuration
import logger
import k2_installer
from tkinter.test.support import destroy_default_root
        
logger.setup_logging()

logger = logging.getLogger('k2_cli')
info = logger.info
debug = logger.debug
warning = logger.warning
error = logger.error

base_url = 'http://localhost:8000'
install_dir = '.'

class K2CliError(Exception):
    pass

@click.group()
def k2():
    pass

@click.command()
@click.option('--k2_ide_url', default=None, help='The base URL of the k2 IDE service')
@click.option('--dest', default=None, help='The directory into which to install the application downloaded from the K2 IDE service')
@click.argument('application')
def install(application, k2_ide_url, dest):
    global base_url
    global install_dir
    
    if k2_ide_url:
        base_url = k2_ide_url
    else:
        try:
            base_url = configuration.config.get('DEFAULT', 'k2_ide_url')
        except:
            warning('Unable to identify the K2 IDE service base URL from configuration using {base}'.format(base=base_url))
            
    if dest:
        install_dir = dest
    else:
        try:
            install_dir = configuration.config.get('DEFAULT', 'install_dir')
        except:
            warning('Unable to identify the installation directory from configuration using {install}'.format(install=install_dir))
        
        
    app = k2_installer.get_application('{base_url}/k2_app/api/application/{id}'.format(base_url=base_url, id=application))
        
    info('Installing {application} with id: {id} from {base} into {dest}'.format(
            application=app['title'],
            id=app['id'],
            base=base_url,
            dest=install_dir
        )
    )
    
    try:
        k2_installer.install(
            '{base}/k2_app/src/{id}'.format(base=base_url, id=app['id']),
            install_dir                        
            )
        info('Successfully installed {name} in {dest}'.format(
            name=app['title'],
            dest=install_dir
            ))
    except Exception as err:
        error(err)
        error('Failed to install application {name}'.format(name=app['title']))
    
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


    