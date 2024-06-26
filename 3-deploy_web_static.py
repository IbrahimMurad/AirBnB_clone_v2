#!/usr/bin/python3
"""
creates and distributes an archive to your web servers,
using the function deploy
"""
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


def deploy():
    """ Packes web_static into .tgz archive """

    arch_path = do_pack()
    if arch_path is None:
        return False
    else:
        return do_deploy(arch_path)
