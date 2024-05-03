#!/usr/bin/python3
""" a Fabric script that
- generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    local("mkdir -p versions")
    
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(time_stamp)
    
    command = "tar -cvzf {} web_static".format(archive_name)
    result = local(command)
    
    if result.failed:
        return None
    return archive_name
