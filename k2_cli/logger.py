import os
import yaml
import json
import logging
import logging.config
import configuration

def setup_logging(path=None, default_level=logging.INFO, env_key='LOG_CFG'):
    config_path = None
    if path:
        config_path = path
    if not config_path:
        config_path = os.getenv(env_key, None)
    if not config_path:
        config_path = configuration.config.get('DEFAULT', 'logging_config')
    if not config_path:
        config_path = 'logging.yaml'
        
    config_path = configuration.find(config_path)
    
    config_format = configuration.config.get('DEFAULT', 'logging_config_format')
    if not config_format:
        config_format = 'YAML'
        
    if os.path.exists(config_path):
        with open(config_path, 'rt') as f:
            try:
                if config_format.upper() == 'YAML':
                    logging.config.dictConfig(yaml.safe_load(f.read()))
                elif config_format.upper() == 'JSON':
                    logging.config.dictConfig(json.loads(f.read()))  
            except Exception as e:
                print(e)
                print('Error in logging configuration file: {file} Using default configs'.format(file=config_path))
                logging.basicConfig(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        print('Failed to load logging configuration file: {file} Using default configs'.format(file=config_path))
