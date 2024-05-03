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
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to /data/web_static/releases/ directory
        filename = archive_path.split("/")[-1]
        foldername = "/data/web_static/releases/{}".format(filename.split(".")[0])
        run("mkdir -p {}".format(foldername))
        run("tar -xzf /tmp/{} -C {}".format(filename, foldername))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(filename))

        # Move the uncompressed contents to appropriate location
        run("mv {}/web_static/* {}".format(foldername, foldername))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(foldername))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(foldername))

        return True

    except Exception as e:
        print(e)
        return False
