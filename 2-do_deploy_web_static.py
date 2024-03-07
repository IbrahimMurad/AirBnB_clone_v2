#!/usr/bin/python3
"""This is a fabfile used for distributes an archive to my web servers"""
import os
from fabric.api import put, run, env


env.hosts = ['100.25.170.65', '54.172.165.136']


def do_deploy(archive_path):
    """ distributes the .tgz archive of my web static\
 to my web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        # path strings
        releases = "/data/web_static/releases"
        arch_name = archive_path.split('/')[-1].split('.')[0]
        full_path = "{}/{}".format(releases, arch_name)

        # transfering the archive to the servers
        put(local_path=archive_path, remote_path='/tmp/')

        # unpacking the archive in a new folder with the same name
        run("mkdir -p {}/".format(full_path))
        run("tar -xzf /tmp/{}.tgz -C {}/".format(arch_name, full_path))

        # deleting the the archive
        run("rm /tmp/{}.tgz".format(arch_name))

        # moving the content of web_static in the new folder
        run("mv {0}/web_static/* {0}/".format(full_path))
        run("rm -rf {}/web_static".format(full_path))

        # redirecting the symlink of current to the new folder
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(full_path))

        print("New version deployed!")
        return True
    except Exception:
        return False
