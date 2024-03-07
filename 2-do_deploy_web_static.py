#!/usr/bin/python3
"""This is a fabfile used for distributes an archive to my web servers"""
from fabric.api import put, run, env


env.hosts = ['100.25.170.65', '54.172.165.136']
env.user = 'ubuntu'
env.ssh_config_path = '~/.ssh/school'


def do_deploy(archive_path):
    """ distributes the .tgz archive of my web static\
 to my web servers"""

    import os
    if not os.path.isfile(archive_path):
        return False

    # path strings
    releases = "/data/web_static/releases"
    arch_name = archive_path.rsplit('/', 1)[1].split('.')[0]

    # transfering the archive to the servers
    if put(local_path=archive_path, remote_path='/tmp/').failed:
        return False

    # unpacking the archive in a new folder with the same name
    if run("rm -r {0}/{1}/".format(releases, arch_name)).failed:
        return False
    if run("mkdir -p {0}/{1}/".format(releases, arch_name)).failed:
        return False
    if run("tar -xzf /tmp/{1}.tgz -C {0}/{1}/".format(
       releases, arch_name)).failed:
        return False

    # deleting the the archive
    if run("rm /tmp/{}.tgz".format(arch_name)).failed:
        return False

    # moving the content of web_static in the new folder
    if run("mv {0}/{1}/web_static/* {0}/{1}/".format(
       releases, arch_name)).failed:
        return False
    if run("rm -rf {0}/{1}/web_static".format(releases, arch_name)).failed:
        return False

    # redirecting the symlink of current to the new folder
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s {0}/{1}/ /data/web_static/current".format(
        releases, arch_name
    )).failed:
        return False

    print("New version deployed!")
    return True
