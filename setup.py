import os
import sys
from setuptools import setup, find_packages
from setuptools.command.bdist_egg import bdist_egg as _bdist_egg


class bdist_egg(_bdist_egg):

    user_options = _bdist_egg.user_options + [('country=', None, 'countries you want to include')]

    def initialize_options(self):
        _bdist_egg.initialize_options(self)
        self.country = None


setup_kwargs = {
        'name': 'locode',
        'version': '0.1',
        'packages': find_packages(),
        'zip_safe': False,
        'cmdclass': {'bdist_egg': bdist_egg},
        'package_dir': {'locode': 'locode'}
        }


if not any('--country' in x for x in sys.argv):
    setup_kwargs['package_data'] = {'': ['*.json']}
else:
    setup_kwargs['package_data'] = {}
    for country in sys.argv[1:]:
        if '--country' in country:
            country = country.replace('--country=', '')
            setup_kwargs['package_data'][country] = [os.path.join(country, '*.json')]

setup(**setup_kwargs)
