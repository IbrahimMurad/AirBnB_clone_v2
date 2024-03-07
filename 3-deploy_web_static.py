#!/usr/bin/python3
"""
This is a fabfile used for packing web_static folder
"""
from fabric.api import local, put, run, env
env.hosts = ['100.25.170.65', '54.172.165.136']

def do_pack():
    """ Packes web_static into .tgz archive """

    from datetime import datetime
    import os
    current_moment = datetime.now()
    no_extension = "web_static_{}{:02}{:02}{:02}{:02}{:02}".format(
        current_moment.year,
        current_moment.month,
        current_moment.day,
        current_moment.hour,
        current_moment.minute,
        current_moment.second
    )
    arch_name = no_extension + ".tgz"
    arch_path = "versions/{}".format(arch_name)
    try:
        print("Packing web_static to {}".format(arch_path))
        if not os.path.exists("versions"):
            os.makedirs("versions")
        local("tar -cvzf {} web_static".format(arch_path), capture=False)
        releases = "/data/web_static/releases/"
        full_path = releases + no_extension
        put(arch_path, '/tmp/', use_sudo=True)
        run("mkdir -p {}/".format(full_path))
        run("tar -xzf /tmp/{} -C {}/".format(arch_name, full_path))
        run("rm /tmp/{}".format(arch_name))
        run("mv {0}/web_static/* {0}/".format(full_path))
        run("rm -rf {}/web_static".format(full_path))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/ /data/web_static/current".format(full_path))
        return True
    except Exception:
        return None
