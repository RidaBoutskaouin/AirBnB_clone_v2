#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,
using the function do_deploy """

from fabric.api import *
from os import path

env.hosts = ["52.205.104.225", "54.208.233.216"]
env.user = "ubuntu"


def do_pack():
    """Function to generate .tgz archive from web_static folder."""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    try:
        local("tar -cvzf {} web_static".format(file))
        return file
    except:
        return None


def do_deploy(archive_path):
    """Function to distribute an archive to web servers."""
    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        return True
    except:
        return False
