# TODO(riley): Docstring.
#
# Draft.
while read line; do
    deadline="${line:0:10}"
    if [[ "$deadline" < "$(date --iso-8601)" ]]; then
       echo "You should have already done this one:"
       echo -e "$line\n"
    fi
done <~/.todos
