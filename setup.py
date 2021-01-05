from setuptools import setup, find_packages

import myproject

setup(
    name=myproject.__name__,
    version=myproject.__version__,
    url='https://github.com/maet3608/minimal-python-project-with-resources',
    author='Author name',
    author_email='author@gmail.com',
    description='Template for a Python project with resources',
    install_requires=[],  # e.g. ['numpy >= 1.11.1', 'matplotlib >= 1.5.1']
    packages=find_packages(),
    package_data={myproject.__name__: ['data/*.txt', 'data/*.json']}
)