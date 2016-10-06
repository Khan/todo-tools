#!/usr/bin/env python


from __future__ import print_function

import os
from datetime import datetime as dt
import re


# Make sure libraries are installed
from fabulous import color
import git


def run_as_checker(args):
    """Check for outstanding TODOs"""
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
            print(todo[:-1])


def run_as_hook(filename, commitA=None, commitB=None):
    """
    Runs in "hook" mode, called solely by git.

    filename: str
    commitA: str
    commitB: str

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
                clean_line = re.sub('^\+ *', '', line)
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
            "\n"
            "These might be TODOs.  Did you mean to do them?\n"
            "-----------------------------------------------")))
        with open(filename, 'a') as todofile:
            for todo in potential_todos:
                print('+ {} | {}'.format(*todo))
                check_date_and_save(todofile, todo[0], todo[1])
    print('')


def check_date_and_save(todofile, filename, line):
    """If the todo is a dated todo, save it to file"""
    # This matches "TODO(name[YYYY-MM-DD]): do stuff"
    date_match = re.search('TODO\([^\)\[]*\[(.*)\]\):?\ *(.*)', line)
    if date_match:
        date = date_match.group(1)
        todofile.write('{}  |  {}  |  {}\n'.format(date, filename, line))


def check_is_todo(line):
    """Check to see if line contains any type of todo"""
    return re.search('[#(//)] ?[Tt][Oo][Dd][Oo][:\(]', line) is not None


def check_is_potential_todo(line):
    """Check to see if 'TODO' is mentioned in the line"""
    return re.search('TODO', line) is not None


def add_line_to_file_if_not_exists(filename, search_str, insert_str):
    """Add a line to a file if it's not already there"""
    already_installed = False
    if os.path.isfile(filename):
        with open(filename, 'r') as ofile:
            for line in ofile.readlines():
                if re.search(search_str, line):
                    already_installed = True
    else:
        already_installed = False
    if not already_installed:
        with open(filename, 'a') as ofile:
            ofile.write(insert_str)
    return None
