#!/usr/bin/python3
"""Fabric script module"""
from fabric.api import *
import paramiko
import time
import os

env.hosts = ['3.90.84.182', '54.227.198.43']
env.user = 'ubuntu'


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    try:
        local("mkdir -p versions")
        archive_path = 'versions/web_static_{}.tgz'.format(
                time.strftime('%Y%m%d%H%M%S'))
        results = local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except Exception:
        return None

def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False

    archive_file = archive_path[9:]
    release_version = '/data/web_static/releases/{}'.format(archive_file[:-4])

    put(archive_path, '/tmp/')
    run('mkdir -p {}'.format(release_version))
    run('tar -xzf /tmp/{} -C {}'.format(archive_file, release_version))
    run('rm /tmp/{}'.format(archive_file))
    run('mv {}/web_static/* {}'.format(release_version, release_version))
    run('rm -rf /data/web_static/releases/web_static')
    run('rm -rf /data/web_static/current')
    run('ln -s {} /data/web_static/current'.format(release_version))

    print('New version deployed!')
    return True

def deploy():
    """Create and distributes an archive to web servers"""
    try:
        path = do_pack()
        return do_deploy(path)
    except Exception:
        return False
