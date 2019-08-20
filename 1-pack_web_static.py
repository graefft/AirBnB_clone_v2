#!/usr/bin/env python3
'''Generates .tgz archive from contents of web_static folder'''
from datetime import datetime
from fabric.api import local
import tarfile


def do_pack():
    '''packs repo into archive'''
    local('mkdir -p versions')
    date = datetime.now()
    name = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(date.hour,
                                                         date.month,
                                                         date.day,
                                                         date.hour,
                                                         date.minute,
                                                         date.second)
    command = local('tar -cvzf ' + name + ' ./web_static')
    if command.succeeded:
        return name
    else:
        return None
