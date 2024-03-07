#!/usr/bin/python3
"""
This is a fabfile used for distributes an archive to my web servers
"""

from os.path import exists
from fabric.api import put, run, env
env.hosts = ['100.25.170.65', '54.172.165.136']


def do_deploy(archive_path):
    """ distributes the .tgz archive of my web static\
 to my web servers"""

    if exists(archive_path) is False:
        return False

    try:
        # path strings
        releases = "/data/web_static/releases/"
        arch_name = archive_path.split("/")[-1]
        no_extension = arch_name.split(".")[0]
        full_path = releases + no_extension
        put(archive_path, '/tmp/')
        run("mkdir -p {}/".format(full_path))
        run("tar -xzf /tmp/{} -C {}/".format(arch_name, full_path))
        run("rm /tmp/{}".format(arch_name))
        run("mv {0}/web_static/* {0}/".format(full_path))
        run("rm -rf {}/web_static".format(full_path))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/ /data/web_static/current".format(full_path))
        return True
    except:
        return False
