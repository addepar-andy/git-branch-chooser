#!/usr/bin/env python2

from __future__ import print_function
import subprocess
import re

FROM_RE = re.compile(r' from ([^\s]+)')
TO_RE = re.compile(r' to ([^\s]+)')

LIMIT = 5

def main():
    lines = subprocess.check_output(['git', 'reflog']).split('\n')
    branches = []
    for line in lines:
        if 'checkout:' not in line:
            continue
        for RE in (FROM_RE, TO_RE):
            m = RE.search(line)
            if m:
                branch = m.group(1)
                if branch not in branches:
                    branches.append(branch)
        if len(branches) > LIMIT:
            break

    for i, branch in enumerate(branches):
        print("[{}]: {}".format(i, branch))

    choice = int(raw_input('Which branch? '))
    branch = branches[choice]
    print()
    print('Checking out ' + branch)
    subprocess.check_call(['git', 'checkout', branch])

if __name__ == '__main__':
    main()