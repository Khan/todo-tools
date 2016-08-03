# TODO Tools

Hey, do you like `TODO`s? Yeah, we all probably like them a little too much... Why write actual code when you could just
leave a `TODO`?

Well, fear no more about losing track of those desired code changes. This tool is a git post-commit hook that warns you
about `TODO`s that you left in your code.

## Installation

Clone this repository using `git clone`, and then run `todo_tools.py -i <desired installation repository root>` to
install it as a post-commit hook. For example:

```bash
git clone https://github.com/willzfarmer/todo-tools
cd todo-tools
./todo-tools.py -i ~/myawesomerepo
```

And it's enabled on that repository! Woo!
