'''
Created on 5 Feb 2019

@author: simon
'''
import requests, sys
import os.path
from urllib.parse import urlparse
import argparse
import json
import logging

class K2InstallError(Exception):
    pass


logger = logging.getLogger('k2_cli')

scheme = ''
netloc = ''
path = ''

def get_application(url):
    response = requests.get(url)
    if response.status_code != 200:
        resp = json.loads(response.text)
        logger.error(resp['trace'])
        raise K2CliError(resp['error'])
    else:
        return json.loads(response.text)
    

def install(source, dest):
    global scheme
    global netloc
    global path
    
    uri = urlparse(source)
    
    scheme = uri.scheme
    netloc = uri.netloc
    path = uri.path
        
    response = requests.get(source)
    if response.status_code != 200:
        resp = json.loads(response.text)
        logger.error(resp['trace'])
        raise K2InstallError(resp['error'])
    
    content_type = response.headers.get('content-type')
    if content_type == 'application/k2-directory':
        write_directory(response, dest)
    elif content_type.split('/')[0] == 'text':
        write_file(response, dest)
    else:
        raise ValueError('{src} returned an unexpected content type: {type}'.format(src=source, type=response.content_type))
    
    
def write_directory(response, dest):

    if os.path.exists(dest):
        logger.warning('Installing to existing directory: {dest}'.format(dest=dest))
    else:
        logger.info('Installing directory: {dest}'.format(dest=dest))
    os.makedirs(dest, exist_ok=True)    
    index = json.loads(response.text)
    
    for key, value in index.items():
        if value and value[0] != '/':
            src = '{scheme}://{netloc}{path}?path={template}'.format(
                    scheme=scheme,
                    netloc=netloc,
                    path=path,
                    template=value
                )
        else:
            src = '{scheme}://{netloc}{path}'.format(
                    scheme=scheme,
                    netloc=netloc,
                    path=value
                )
        logger.debug('Install: {src} in {dest})'.format(src=src, dest=dest))
        if key == '.':
            install(src,  dest)
        else:
            install(src,  '/'.join([dest, key]))
            

def write_file(response, dest):
    dirname = os.path.dirname(dest)
    if not os.path.exists(dirname):
        logger.debug('Creating directory: {name}'.format(name=dirname))
        os.makedirs(dirname, exist_ok=True)
    if os.path.exists(dest):
        logger.warning('Replacing file: {file}'.format(file=dest))
    else:
        logger.info('Installing file: {file}'.format(file=dest))
    with open(dest, 'w') as fp:
        fp.write(response.text)
        
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='The source URL to install')
    parser.add_argument('dest', help='The location in which to install the generated source')
    args = parser.parse_args()
    
    logger.info('Installing {src} into {dest}'.format(src=args.source, dest=args.dest))
    install(args.source, args.dest)



