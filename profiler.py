#!/usr/bin/env python

"""
Profile the TODO-tools
"""

import sys
import os
import io
import statistics
import argparse
import time
import git
import seaborn
import tqdm
import matplotlib.pyplot as plt

import todo_tools


def main():
    args = get_args()
    olddir = os.getcwd()

    os.chdir(args.repo)

    repo = git.Repo('.')

    actualstdout = sys.stdout
    sys.stdout = io.StringIO()

    times = []
    for i in tqdm.tqdm(range(1000)):
        localtimes = []
        for j in range(5):
            stime = time.time()
            todo_tools.run_as_hook(os.path.join(os.path.expanduser('~/.todo')),
                                    'HEAD~{}'.format(i), 'HEAD~{}'.format(i + 1),
                                    skip=True)
            localtimes.append(time.time() - stime)
        times.append(statistics.mean(localtimes))

    sys.stdout = actualstdout

    os.chdir(olddir)

    plt.hist(times, bins=20)
    plt.savefig('./profile_hist.png')



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--repo', default=None, type=str,
                        help='Repo to run on.')
    args = parser.parse_args()

    if args.repo is None:
        args.repo = input('Please select a repo> ')
    return args


if __name__ == '__main__':
    sys.exit(main())
