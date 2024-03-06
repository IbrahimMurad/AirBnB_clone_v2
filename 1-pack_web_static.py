#!/usr/bin/python3
"""This is a fabfile used for packing web_static folder"""
from fabric.api import local


def do_pack():
    """ Packes web_static into .tgz archive """

    from datetime import datetime
    import os
    current_moment = datetime.now()
    arch_name = "web_static_{}{:02}{:02}{:02}{:02}{:02}.tgz".format(
        current_moment.year,
        current_moment.month,
        current_moment.day,
        current_moment.hour,
        current_moment.minute,
        current_moment.second
    )
    arch_path = "versions/{}".format(arch_name)
    try:
        print("Packing web_static to {}".format(arch_path))
        if not os.path.exists("versions"):
            os.makedirs("versions")
        local("tar -cvzf {} web_static".format(arch_path), capture=False)
        return arch_path
    except Exception:
        return None
