# Find all the currently modified lines with TODOs

main() {
    difiles | process_changed_files
}

process_changed_files() {
    while read filename; do
        get_changed_lines "$filename" \
            | filter_todo_lines \
            | handle_todo_line $filename
    done
}

get_changed_lines() {
    git diff HEAD $1 \
        | grep '^+' \
        | grep -v '^+++ ' \
        | sed -e 's/^+//'
}

handle_todo_line() {
    filename=$1
    while read line; do
        echo "$filename" "$line"
    done
}

filter_todo_lines() {
    while read line; do
        grep -i 'TODO[\(:]' <<< $line
    done
}

difiles () {
    git status --porcelain | awk '{print $2}'
}

main $*
