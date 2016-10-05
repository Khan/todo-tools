# TODO Tools

Hey, do you like `TODO`s? Yeah, we all probably like them a little too much...
Why write actual code when you could just leave a `TODO`?

Well, fear no more about losing track of those desired code changes. This tool
is a git post-commit hook that warns you about `TODO`s that you left in your
code.

## Quickstart

```bash
$ pip install todo_tools
$ cd webapp
$ todo --register-git-hook .
$ git commit -a -m 'These are all of my todos'
Here's a list of TODOs you added in this commit:
------------------------------------------------
+ website.py | # TODO(zeb[2017-01-01]): Wish people happy new year
+ website.py | # TODO(zeb[2016-08-04]): Remove this when AB test ends
+ constants.jsx | // TODO: This should be done!
```

Now whenever you run `todo --check`, you'll be notified of past-due TODOs

If you want that to happen every time you start a shell, you can

```bash
$ todo --install-to-bashrc
```

Or

```bash
$ echo 'todo --check' >> ~/.bashrc
```

You can manually edit todos by looking in `~/.todo`.


## Installation

We have three different ways to install this.

Note, you *do not have to do this to use the full installation*. The manual
installation method works without cluttering your `$PATH`. If you don't care
about that, by all means make your life easier and use `pip` or `setuptools`.

### PyPI

**[Coming Soon]**

```bash
┬─[william@fillory:~/todo-tools]
╰─>$ pip install todo_tools --user
```

### By Hand

Clone this repository using `git clone`, and then run `./bin/todo -i <desired
installation repository root>` to install it as a post-commit hook. For example:

```bash
┬─[william@fillory:~/todo-tools]
╰─>$ git clone https://github.com/willzfarmer/todo-tools
┬─[william@fillory:~/todo-tools]
╰─>$ cd todo-tools
┬─[william@fillory:~/todo-tools]
╰─>$ ./bin/todo --register-git-hook ~/myawesomerepo
```

And it's enabled on that repository! Woo!

### Setuptools

```bash
┬─[william@fillory:~/todo-tools]
╰─>$ python setup.py install --user
┬─[william@fillory:~/todo-tools]
╰─>$ todo --install-to-bashrc
```
