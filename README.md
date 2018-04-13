# git-branch-chooser

`git-branch-chooser` is a simple CLI tool to help you switch branches, choosing from recently used branches.

## Installation

1. clone
2. add the `bin` directory to your PATH
3. (Optional) `alias gitbr=git-branch-chooser.py` or `alias gb=git-branch-chooser.py`

## Usage

```console
andy@addepar:~$ cd ~/src/AMP
andy@addepar:~$ gb
[0]: andy/proposal2
[1]: andy/proposal3
[2]: master
[3]: andy/portfolio-construction-model
[4]: andy/pdj-cleanup
[5]: andy/pdj-minor
Which branch?
```

Type the number of the branch and it will be checked out

```console
Which branch? 2

Checking out master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
```

## How does it work?

It looks through your `reflog` looking for things that look like branch names.  Then it lets you choose from the last 5.
