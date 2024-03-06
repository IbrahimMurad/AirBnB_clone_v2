#!/usr/bin/python3
"""This is a fabfile used for distributes an archive to my web servers"""
from fabric.api import put, run, env


env.hosts = ['100.25.170.165', '54.172.165.136']
env.user = 'ubuntu'
env.ssh_config_path = '~/.ssh/school'


def do_deploy(archive_path):
    """ distributes the .tgz archive of my web static\
 to my web servers"""

    import os
    if not os.path.exists(archive_path):
        return False

    try:
        # path strings
        releases = "/data/web_static/releases"
        _, arch_name = arch_name.rsplit('/', 1).partition('.')[0]

        # transfering the archive to the servers
        put(local_path=archive_path, remote_path='/tmp/')

        # unpacking the archive in a new folder with the same name
        run("mkdir -p {}/{}/".format(releases, arch_name))
        run("tar -xzf /tmp/{0}.tgz -C {}/{}/".format(
            releases, arch_name
        ))

        # deleting the the archive
        run("rm /tmp/{}.tgz".format(arch_name))

        # moving the content of web_static in the new folder
        run("mv {0}/{1}/web_static/* {0}/{1}/".format(releases, arch_name))
        run("rm -rf {}/{}/web_static".format(releases, arch_name))

        # redirecting the symlink of current to the new folder
        run("rm -rf /data/web_static/current")
        run("ln -s {}/{}/ /data/web_static/current".format(
            releases, arch_name
        ))

        print("New version deployed!")
        return True

    except Exception:
        return False
