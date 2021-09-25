import json
import os

# post pull and pre commit
from pathlib import Path

from shutil import copy

GIT_HOOKS_DIR = '.git/hooks/'
HOOKS = ['pre-commit', 'post-receive']
PARSED_SCRIPTS = './.parsed_scripts/'
DIRECTORY = './sqlscript/'


def parse():
    Path(PARSED_SCRIPTS).mkdir(parents=True, exist_ok=True)
    for filename in os.listdir(DIRECTORY):
        if filename.endswith(".json"):
            with open(os.path.join(DIRECTORY, filename)) as f:
                contents = json.loads(f.read())
            with open(PARSED_SCRIPTS + filename.replace('.json', '.sql'), 'w') as nf:
                nf.write(contents['properties']['content']['query'])


def serialise():
    for filename in os.listdir(DIRECTORY):
        if filename.endswith(".json"):
            with open(os.path.join(DIRECTORY, filename), 'r+') as f:
                contents = json.loads(f.read())
                with open(PARSED_SCRIPTS + filename.replace('.json', '.sql'), 'r') as nf:
                    contents2 = nf.read()

                if contents2 != contents['properties']['content']['query']:
                    contents['properties']['content']['query'] = contents2
                    f.seek(0)
                    f.write(json.dumps(contents, indent='\t'))


def remove_hooks():
    for f in HOOKS:
        os.remove(GIT_HOOKS_DIR + f)
