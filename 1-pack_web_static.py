#!/usr/bin/python3
'''script that generates a .tgz archive from the contents of the web_static'''
from fabric.api import local
from datetime import datetime


def do_pack():
    '''Generates a .tgz archive from the contents of the web_static'''
    try:
    	source_dir = 'web_static'
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        output_filename = 'web_static_{}.tgz'.formate(timestamp)
        local('mkdir -p versions')
        check = local('tar -cvzf versons/{} {}'.format(output_filename, source_dir))
        return 'versions/{}'.format(output_filename)
    except Exception:
        return None
