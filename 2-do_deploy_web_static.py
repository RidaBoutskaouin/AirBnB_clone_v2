#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,
using the function do_deploy """

from fabric.api import *
from os import path

env.hosts = ["52.205.104.225", "54.208.233.216"]


def do_deploy(archive_path):
    """Function that distributes an archive to your web servers,
    using the function do_deploy"""

    if path.exists(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1]
        file_name_no_ext = file_name.split(".")[0]
        path_r = "/data/web_static/releases/"
        path_current = "/data/web_static/current"
        run("mkdir -p {}{}/".format(path_r, file_name_no_ext))
        run(
            "tar -xzf /tmp/{} -C {}{}/".format(
                file_name, path_r, file_name_no_ext
            )
        )
        run("rm /tmp/{}".format(file_name))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path_r, file_name_no_ext))
        run("rm -rf {}{}/web_static".format(path_r, file_name_no_ext))
        run("rm -rf {}".format(path_current))
        run("ln -s {}{}/ {}".format(path_r, file_name_no_ext, path_current))
        return True
    except:
        return False
