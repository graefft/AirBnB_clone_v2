#!/usr/bin/python3
'''Fabric'''


import os
from fabric.api import env, put, run


env.hosts = ['35.237.137.208', '34.74.82.54']
env.user = 'ubuntu'


def do_deploy(archive_path):
    '''Distributes an archive to web servers'''
    if not os.path.exists(archive_path):
        return False

    base = os.path.basename(archive_path)
    name = archive_path.split('.')[0]
    directory = '/data/web_static/releases/'
    run('mkdir -p {}{}'.format(name))
    run('tar -xzf /tmp/{} -C {}{}'.format(base,
                                          directory,
                                          name))
    run('rm -rf /tmp/' + base)
    run('rm -rf /data/web_static/current')
    run('ln -sf {}{} /data/web_static/current'.format(directory,
                                                      name))
    run('service nginx restart')

    return True
