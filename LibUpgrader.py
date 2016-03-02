#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import pip
import platform

from subprocess import call


class LibUpgrader(object):

    @staticmethod
    def on_server():
        if platform.system() == "Linux":
            return True
        else:
            return False

    @staticmethod
    def upgrade_libraries():
        for dist in pip.get_installed_distributions():
            if LibUpgrader.on_server:
                call("pip3.4 install --upgrade " + dist.project_name, shell=True)
            else:
                call("pip install --upgrade " + dist.project_name, shell=True)

if __name__ == '__main__':
    LibUpgrader.upgrade_libraries()
