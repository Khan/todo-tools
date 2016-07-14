# TODO: docstring
main() {
    difiles \
        | grab_changed_lines
}

grab_changed_lines() {
    while read filename; do
        echo $filename
        git diff HEAD $filename \
            | grep '^+' \
            | grep -v '^+++ ' \
            | sed -e 's/^+//'
    done
}

difiles () {
    git status --porcelain | awk '{print $2}'
}

main $*
