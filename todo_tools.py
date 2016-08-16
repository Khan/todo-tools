#!/usr/bin/env python

"""
 _____ ___  ____   ___    _____           _
|_   _/ _ \|  _ \ / _ \  |_   _|__   ___ | |___
  | || | | | | | | | | |   | |/ _ \ / _ \| / __|
  | || |_| | |_| | |_| |   | | (_) | (_) | \__ \
  |_| \___/|____/ \___/    |_|\___/ \___/|_|___/


# Setup

For each repository you want to log TODO's, run

./todo-tools.py -i ~/myawesomerepo

"""

from __future__ import print_function


import argparse
from datetime import datetime as dt
import os
import re
import sys
import shutil
import time

from fabulous import color
import git


def main():
    args = get_args()

    if sys.version_info[0] == 2:
        input = raw_input

    if args.install and os.path.isdir(os.path.join(args.install, '.git')):
        # TODO: copy instance of running file to given directory
        shutil.copy('./todo_tools.py', os.path.join(args.install,
                    '.git/hooks/post-commit'))
    elif args.check:
        run_as_checker(args)
    else:
        sys.stdin = open('/dev/tty')
        run_as_hook(args.file)


def run_as_checker(args):
    outstanding = []
    with open(args.file, 'r') as todofile:
        for line in todofile.readlines():
            if dt.today() > dt.strptime(line[:10], '%Y-%m-%d'):
                outstanding.append(line)
    if outstanding:
        print(color.bold(color.red(
            'Warning! You should have already done this!:\n'
            '--------------------------------------------')))
        for todo in outstanding:
            print(todo)


def run_as_hook(filename, commitA=None, commitB=None, skip=False):
    """
    filename: str
    commitA: str
    commitB: str
    skip: bool

    commitA and commitB exist /solely/ for profiling and testing
    """
    # Initialize new repo (called from git hook so this directory works)
    repo = git.Repo('.')

    if commitA is not None and commitB is not None:
        previous_commit = repo.commit(commitB)
        current_commit = repo.commit(commitA)
    else:
        previous_commit = repo.commit('HEAD~1')
        current_commit = repo.commit('HEAD')
    # Get specific changes in each file
    todos = []
    potential_todos = []
    for filediff in previous_commit.diff(current_commit, create_patch=True):
        # Find all modified lines in file
        for line in str(filediff).split('\n'):
            if re.match('^\+', line) and re.match('^\+\+\+', line) is None:
                clean_line =  re.sub('^\+ *', '', line)
                if check_is_todo(clean_line):
                    todos.append((filediff.b_path, clean_line))
                elif check_is_potential_todo(clean_line):
                    potential_todos.append((filediff.b_path, clean_line))
    if todos:
        print(color.bold(color.yellow(
            "Here's a list of TODOs you added in this commit:\n"
            "------------------------------------------------")))
        with open(filename, 'a') as todofile:
            for todo in todos:
                print('+ {} | {}'.format(*todo))
                check_date_and_save(todofile, todo[0], todo[1])
    if potential_todos:  # TODO: test
        print(color.bold(color.yellow(
            "These might be TODOs.  Did you mean to do them?\n"
            "-----------------------------------------------")))
        with open(filename, 'a') as todofile:
            for todo in potential_todos:
                if skip:
                    choice = 'n'
                else:
                    choice = input('+ {} | {} (y/N) '.format(*todo))
                if choice.lower() == 'y':
                    check_date_and_save(todofile, todo[0], todo[1])
    print('')


def check_date_and_save(todofile, filename, line):
    # This matches "TODO(name[YYYY-MM-DD]): do stuff"
    date_match = re.search('TODO\([^\)\[]*\[(.*)\]\):?\ *(.*)', line)
    if date_match:
        date = date_match.group(1)
        todofile.write('{}  |  {}  |  {}\n'.format(date, filename, line))


def check_is_todo(line):
    return re.search('[#(//)] ?[Tt][Oo][Dd][Oo][:\(]', line) is not None


def check_is_potential_todo(line):
    return re.search('TODO', line) is not None


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str,
                        default=os.path.join(os.path.expanduser('~/.todo')),
                        help=('What file to use as our todo file.'))
    parser.add_argument('-i', '--install', type=str, default=None,
                        help=('Install post-commit hook to git repository. '
                              'Run from root of this repository.'))
    parser.add_argument('-c', '--check', action='store_true', default=False,
            help=('Check outstanding TODOs and alert '
                  'if any are overdue'))
    args = parser.parse_args()
    # create the todo file if it doesn't exist
    args.file = os.path.abspath(args.file)
    if not os.path.isfile(args.file):
        open(args.file, 'w').close()
    return args


if __name__ == '__main__':
    sys.exit(main())
