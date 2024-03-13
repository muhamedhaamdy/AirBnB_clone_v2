#!/usr/bin/python3
'''
Fabric script that distributes an archive to your web servers,
using the function do_deploy
'''
import fabric.api import *
env.hosts = ['3.90.84.182', '54.227.198.43']


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    try:
        put(archive_path, '/tmp')
        tokns archive_path.split('/')
        abs_path = tokns.split('.')
        releases = '/data/web_static/releases/{}'.format(abs_path[0])
        run('mkdir -p {}'.format(releases))
        run('tar -xzf tmp/{}.tgz -C {}'.format(abs_path[0], releases))
        run('rm -rf /tmp/{}.tgz'.format(abs_path[0]))
        run('mv {}/web_static/* {} '.format(releases, releases))
        run('rm -rf {}/web_static'.format(releases))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(releases))
        return True
    except Exception:
        return False
