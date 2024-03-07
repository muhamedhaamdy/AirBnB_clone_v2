#!/usr/bin/python3
'''script that generates a .tgz archive from the contents of the web_static'''
from fabric.api import *
from datetime import datetime


def do_pack():
    '''Generates a .tgz archive from the contents of the web_static'''
    try:
        local('mkdir -p versions')
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        output_path = 'versions/web_static_{}.tgz'.formate(timestamp)
        check = local('tar -cvzf {} web_static'.format(output_path))
        return output_path
    except Exception:
        return None
