#!/usr/bin/python3
'''script that generates a .tgz archive from the contents of the web_static'''
from fabric.api import *
import time


def do_pack():
    '''Generates a .tgz archive from the contents of the web_static'''
    try:
        local('mkdir -p versions')
        archive_path = 'versions/web_static_{}.tgz'.format(
                time.strftime('%Y%m%d%H%M%S'))
        local('tar -cvzf {} web_static'.format(output_path))
        return output_path
    except Exception:
        return None
