# minimal-python-project-with-resources

Template for a minimal python project with resource files and
command line interface (entry point).

A nice introduction on how to write setup.py for resource data can be found 
[here](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/).

More information on support for command line scrips (entry points) can be
found [here](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html).


## Installation

```
cd minimal-python-project-with-resources
python setup.py install
```


## Command line

```
λ mycmd -h
usage: mycmd [-h] [-l | -s filename | -v]

mycmd example

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            list all resource files
  -s filename, --show filename
                        show resource file content
  -v, --version         show program's version number and exit
```

Example usage

```
$ mycmd --list
mydata.json
mydata.txt
```


```
$ mycmd --show mydata.txt
This is some
example data.
```