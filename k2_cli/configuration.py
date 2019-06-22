import os
import configparser

def _default_config(config):
    config['DEFAULT'] = {
        'logging_config': 'logging.yaml',
        'logging_config_format': 'YAML',
    }
        
def read_config(default_path='k2_cli.ini', env_key='K2_CLI_CFG'):
    config = configparser.ConfigParser()
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
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

