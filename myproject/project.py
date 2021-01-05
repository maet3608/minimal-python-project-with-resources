"""
In the following examples on how to handle resource data.

Note the line in setup.py that specifies the resource data
  package_data={'myproject': ['data/*.txt', 'data/*.json']}

Do not use resource_filename() and the returned filename to load
resource data directly, since they may or may not be stored in an egg/zip file!
Use resource_stream() or resource_string() instead.
"""

import myproject


def print_resource_info():
    from pkg_resources import (resource_filename, resource_exists,
                               resource_isdir, resource_listdir)

    resname, datadir = 'data/mydata.txt', 'data/'
    print('isdir', resource_isdir(myproject.__name__, datadir))
    print('dir', resource_listdir(myproject.__name__, datadir))
    print('filepath:', resource_filename(myproject.__name__, resname))
    print('exists', resource_exists(myproject.__name__, resname))


def load_text_data():
    from pkg_resources import resource_string
    # resource_string actually returns binary data and needs decode()!
    data = resource_string(myproject.__name__, 'data/mydata.txt')
    return data.decode()


def load_text_stream():
    from pkg_resources import resource_stream
    data = resource_stream(myproject.__name__, 'data/mydata.txt')
    # resource_stream returns binary data and needs decode() for text data
    for line in data:
        yield line.decode().strip()  # strip new line


def load_json_data():
    import json
    from pkg_resources import resource_stream
    return json.load(resource_stream(myproject.__name__, 'data/mydata.json'))


def load_all_resources():
    from pkg_resources import resource_listdir, resource_string

    datadir = 'data/'
    for resname in resource_listdir(myproject.__name__, datadir):
        data = resource_string(myproject.__name__, datadir + resname)
        yield data.decode()


if __name__ == '__main__':
    print_resource_info()

    print('-' * 80)
    print(load_text_data())

    print('-' * 80)
    print([line for line in load_text_stream()])

    print('-' * 80)
    print(load_json_data())
