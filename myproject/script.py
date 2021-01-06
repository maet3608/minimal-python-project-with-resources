"""
Shows how to add command line script capability

Note the definition of the entry point in setup.py:
entry_points={'console_scripts': ['mycmd=%s.script:cmd' % myproject.__name__]}

usage: mycmd [-h] [-l | -s filename | -v]

mycmd example

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            list all resource files
  -s filename, --show filename
                        show resource file content
  -v, --version         show program's version number and exit
"""

import myproject


def resnames():
    from pkg_resources import resource_listdir
    return resource_listdir(myproject.__name__, myproject._resourcedir)


def list_resources():
    for resname in resnames():
        print(resname)


def show_resource(resname):
    from pkg_resources import resource_string
    assert resname in resnames()
    data = resource_string(myproject.__name__, myproject._resourcedir + resname)
    print(data.decode())


def cmd():
    from argparse import ArgumentParser
    parser = ArgumentParser(description='mycmd example')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', '--list', action='store_true',
                       help="list all resource files")
    group.add_argument('-s', '--show', type=str, metavar='filename',
                       help="show resource file content")
    group.add_argument('-v', '--version', action='version',
                       version=myproject.__version__)

    args = parser.parse_args()
    if args.list:
        list_resources()
    if args.show:
        show_resource(args.show)
