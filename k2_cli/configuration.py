import os
import configparser
from importlib.resources import path
import sys
from pathlib import Path

def _default_config(config):
    config['DEFAULT'] = {
        'logging_config': 'logging.yaml',
        'logging_config_format': 'YAML',
    }
    
def find(name, search=None):
    if not name or name == '':
        raise ValueError('The name of the configuration file to be found must be supplied')
    if os.path.exists(name):
        return os.path.abspath(name)
    if search:
        if isinstance(search, str):
            search_paths = os.getenv(search, None)
            if search_paths:
                for search_path in search_paths.split(':'):
                    if os.path.exists(os.path.sep.join([search_path, name])):
                        return os.path.abspath(os.path.sep.join([search_path, name]))
        elif isinstance(search, list):
            for search_path in search:
                if os.path.exists(os.path.sep.join([search_path, name])):
                    return os.path.abspath(os.path.sep.join([search_path, name]))
    exec_path = Path(sys.executable).parent
    if (os.path.exists(os.path.sep.join([str(exec_path), name]))):
        return os.path.abspath(os.path.sep.join([str(exec_path), name]))
    if (os.path.exists(os.path.sep.join([str(exec_path.parent), name]))):
        return os.path.abspath(os.path.sep.join([str(exec_path.parent), name]))
    home = os.getenv('HOME', None)
    if (home and os.path.exists(os.path.sep.join([home, name]))):
        return os.path.abspath(os.path.sep.join([home, name]))
    
    raise FileNotFoundError('Unable to find a file named {file}'.format(file=name))
    
    
        
def read_config(name=None, env_key='K2_CLI_CFG'):
    config = configparser.ConfigParser()
    if name:
        config_name = name
    else:
        config_name = os.getenv(env_key, None)
    if not config_name:
        config_name = 'k2_cli.ini'       
            
    path = find(config_name)
    if os.path.exists(path):
        try:
            config.read(path)
        except Exception as e:
            print(e)
            print('Error in k2_cli configuration file: {file}. Using default configs'.format(file=path))
            _default_config(config)
    else:
        print('The configuration file: {file} does not exist. Using default configs'.format(file=path))
        _default_config(config)
    return config

config = read_config()

