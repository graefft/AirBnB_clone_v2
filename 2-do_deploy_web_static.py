#!/usr/bin/python3
'''Fabric script to deploy web_static on server'''


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
    no_ext = name.split('/')[1]

    directory = '/data/web_static/releases/'
    result = put(archive_path, "/tmp/".format(name))
    if result.failed:
        return False

    run('mkdir -p {}{}/'.format(directory, no_ext))
    run('tar -xzf /tmp/{} -C {}{}/'.format(base,
                                           directory,
                                           no_ext))
    run('rm /tmp/' + base)
    run('mv {}{}/web_static/* {}{}/'.format(directory,
                                            no_ext,
                                            directory,
                                            no_ext))
    run('rm -rf {}{}/web_static'.format(directory,
                                        no_ext))
    run('rm -rf /data/web_static/current')
    run('ln -sf {}{}/ /data/web_static/current'.format(directory,
                                                       name))
    print('New version deployed!')
    return True
