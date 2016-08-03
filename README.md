# TODO Tools

Hey, do you like `TODO`s? Yeah, we all probably like them a little too much... Why write actual code when you could just
leave a `TODO`?

Well, fear no more about losing track of those desired code changes. This tool is a git post-commit hook that warns you
about `TODO`s that you left in your code.

## Example (How do you mean?)

```
Here's a list of TODOs you added in this commit:
------------------------------------------------
+ todo_tools.py | # TODO(@zeb[2016-08-04]): pls check if werks
+ todo_tools.py | # TODO(@zeb[2015-08-04]): This should fail
+ todo_tools.py | # TODO: copy instance of running file to given directory
+ todo_tools.py | # TODO: consolidate saving
+ todo_tools.py | if potential_todos:  # TODO: test
+ todo_tools.py | print('')  # print newline for prettiness # TODO: ask user
These might be TODOs.  Did you mean to do them?
-----------------------------------------------
+ README.md | # TODO Tools (y/N) 
+ README.md | Hey, do you like `TODO`s? Yeah, we all probably like them a little too much... Why write actual code when you could just (y/N) 
+ README.md | leave a `TODO`? (y/N) 
+ README.md | about `TODO`s that you left in your code. (y/N) 
```

## Installation

Clone this repository using `git clone`, and then run `todo_tools.py -i <desired installation repository root>` to
install it as a post-commit hook. For example:

```bash
git clone https://github.com/willzfarmer/todo-tools
cd todo-tools
./todo-tools.py -i ~/myawesomerepo
```

And it's enabled on that repository! Woo!
