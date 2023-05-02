#!/usr/bin/env python

from setuptools import setup

requirements = []  # add Python dependencies here
# e.g., requirements = ["PyYAML"]

setup(
    name='awx-custom-credential-plugin-example',
    version='0.1',
    author='Ansible, Inc.',
    author_email='info@ansible.com',
    description='',
    long_description='',
    license='Apache License 2.0',
    keywords='ansible',
    url='http://github.com/tuxonfire/awx-custom-credential-plugin-example',
    packages=['awx_custom_credential_plugin_example'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=requirements,
    entry_points = {
        'awx.credential_plugins': [
            'dynamic_plugin = awx_custom_credential_plugin_example:dynamic_plugin',
        ]
    }
)
