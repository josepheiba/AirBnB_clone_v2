#!/usr/bin/python3
""" a Fabric script that
- distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import env, put, run
from os.path import exists


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        filename = archive_path.split("/")[-1]
        foldername = "/data/web_static/releases/{}".format(filename.split(".")[0])
        run("mkdir -p {}".format(foldername))
        run("tar -xzf /tmp/{} -C {}".format(filename, foldername))

        run("rm /tmp/{}".format(filename))

        run("mv {}/web_static/* {}".format(foldername, foldername))

        run("rm -rf {}/web_static".format(foldername))

        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(foldername))

        return True

    except Exception as e:
        print(e)
        return False
