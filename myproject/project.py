"""
In the following an example on how to handle resource data.

Note the line in setup.py that specifies the resource data
    package_data={myproject.__name__: [
        myproject._resourcedir + '*.txt',
        myproject._resourcedir + '*.json']},

"""

import myproject


def print_resource_info():
    from pkg_resources import (resource_filename, resource_exists,
                               resource_isdir, resource_listdir)
    prj = myproject.__name__
    dir = myproject._resourcedir
    resname = dir + 'mydata.txt'

    print('isdir', resource_isdir(prj, dir))
    print('dir', resource_listdir(prj, dir))
    print('filepath:', resource_filename(prj, resname))
    print('exists', resource_exists(prj, resname))


def load_text_data():
    from pkg_resources import resource_string
    # resource_string actually returns binary data and needs decode()!
    resname = myproject._resourcedir + 'mydata.txt'
    data = resource_string(myproject.__name__, resname)
    return data.decode()


def load_text_stream():
    from pkg_resources import resource_stream
    resname = myproject._resourcedir + 'mydata.txt'
    data = resource_stream(myproject.__name__, resname)
    # resource_stream returns binary data and needs decode() for text data
    for line in data:
        yield line.decode().strip()  # strip new line


def load_json_data():
    import json
    from pkg_resources import resource_stream
    resname = myproject._resourcedir + 'mydata.json'
    return json.load(resource_stream(myproject.__name__, resname))


def load_all_resources():
    from pkg_resources import resource_listdir, resource_string
    dir = myproject._resourcedir
    for resname in resource_listdir(myproject.__name__, dir):
        data = resource_string(myproject.__name__, dir + resname)
        yield data.decode()


if __name__ == '__main__':
    print_resource_info()

    print('-' * 80)
    print(load_text_data())

    print('-' * 80)
    print([line for line in load_text_stream()])

    print('-' * 80)
    print(load_json_data())
