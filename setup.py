#!/usr/bin/env python

# Custom install process
# https://blog.niteoweb.com/setuptools-run-custom-code-in-setup-py/

from setuptools import setup
from setuptools.command.install import install

import os
import re


class CustomInstallCommand(install):
    """Customized setuptools install command - Adds todo to .bashrc """
    def run(self):
        bashrcfilename = os.path.join(os.path.expanduser('~/.bashrc'))
        already_installed = False
        if os.path.isfile(bashrcfilename):
            with open(bashrcfilename, 'r') as bashrcfile:
                for line in bashrcfile.readlines():
                    if re.search('todo -c', line):
                        already_installed = True
        else:
            already_installed = False
        if not already_installed:
            with open(bashrcfilename, 'a') as bashrcfile:
                bashrcfile.write('\ntodo -c\n')

        install.run(self)


setup(name='TODO-Tools',
        version='1.0',
        description='Tools to manage git TODOs',
        license='Apache',
        packages=['todo_tools'],
        scripts=['bin/todo'],
        cmdclass={
            'install': CustomInstallCommand,
        })
