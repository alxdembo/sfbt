Synatools
--------

Makes work with Synapse SQL scripts more convenient:

1) Allows editing SQL scripts in an actual IDE of choice
2) Creates readable Pull requests
3) Helps with Git operations that are not available in the Synapse Studio, such as Merge

To use, navigate to the project repository and type::

    pip install synatools
    synatools add-hooks

This will do following:

1) add a post-receive hook to parse received scripts and to put those into .parsed_scripts directory
2) add a pre-commit hook to serialise the script back into the original format

Alternatively, synatools parse and serialise commands can be used to perform the mentioned operations manually

To remove hooks, type::

    synatools remove-hooks

