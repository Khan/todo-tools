#!/bin/bash

# Save a TODO to the tracker if it has a deadline.
#
# Basic usage:
#
#     $ save_todo.sh ~/hygene/goals "TODO(riley[10 days]): Wash your hair."
#
FILENAME=$1
TODO=$2
DATE_PATTERN="TODO\([^\)\[]*\[(.*)\]\):?\ *(.*)"

shopt -s nocasematch
if [[ $TODO =~ $DATE_PATTERN ]]; then
    DATE="${BASH_REMATCH[1]}"
    MSG="${BASH_REMATCH[2]}"
    echo -e $(date --iso-8601 --date "$DATE")"\t|\t$FILENAME\t|\t$MSG" >> ~/.todos
fi
