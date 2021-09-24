import json
import os

# post pull and pre commit
import shutil
from shutil import copy

GIT_HOOKS_DIR = '.git/hooks/'
HOOKS = ['pre-commit', 'post-receive']


def parse():
    print('parsing, lol')
    return 1
    directory = './sqlscript/'
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            print(os.path.join(directory, filename))
            with open(os.path.join(directory, filename)) as f:
                contents = json.loads(f.read())
                with open('./parsed_scripts/' + filename.replace('.json', '.sql'), 'w') as nf:
                    nf.write(contents['properties']['content']['query'])


def serialise():
    print('serialising lol')


def print_help(q):
    print('yolo', q)


# todo this overwrites hooks
def add_hooks():
    for f in HOOKS:

        copy(f, GIT_HOOKS_DIR + f)


def remove_hooks():
    for f in HOOKS:
        os.remove(GIT_HOOKS_DIR + f)
