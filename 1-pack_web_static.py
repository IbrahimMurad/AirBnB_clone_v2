#!/usr/bin/python3
"""This is a fabfile used for packing web_static folder"""


def do_pack():
    """ Packes web_static into .tgz archive """

    from datetime import datetime
    current_moment = datetime.now()
    arch_name = "web_static_{}{}{}{}{}{}.tgz".format(
        current_moment.year,
        current_moment.month,
        current_moment.day,
        current_moment.hour,
        current_moment.minute,
        current_moment.second
    )
    local("tar -cvzf versions/{} web_static".format(arch_name))
