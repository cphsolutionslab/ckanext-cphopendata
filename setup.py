from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-cphopendata',
    version=version,
    description="Theme for cph.opendata.dk",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Henrik Aagaard Jorgensen',
    author_email='haj@cphsolutionslab.dk',
    url='http://cph.opendata.dk',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.cphopendata'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        cphopendata=ckanext.cphopendata.plugin:CPHOpenDataPlugin
    ''',
)
