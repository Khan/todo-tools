# TODO Tools

Have you ever come across this in your codebase:
```
# TODO(person-who-left-the-company-2-years-ago): Definitely remove this by Y2K
```

TODO Tools is here to help.


## What is it?

 1. A git post-commit hook to check for new TODOs
    - If they match the format `TODO(username[YYYY-MM-DD]): Message`, add them
      to your `~/.todo` file
    - Regardless of format, give the committer a summary of all TODOs they are
      committing.  Maybe they meant to actually do them in this commit.
 2. A `~/.todo`-file auditor, looking for past-due TODOs and printing reminders
 3. A utility to install the git-hook and auditor


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

Now whenever you run `todo --check`, you'll be notified of past-due TODOs:

```bash
$ todo --check
Warning! You should have already done this!:
--------------------------------------------
2016-08-04  |  website.py  |  # TODO(zeb[2016-08-04]): Remove this when AB test ends
```

If you want that to happen every time you start a shell, you can

```bash
$ todo --install-to-bashrc
```

Or

```bash
$ echo 'todo --check' >> ~/.bashrc
```

You can manually edit todos by looking in `~/.todo`.
