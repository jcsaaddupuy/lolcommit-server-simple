#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = open("requirements.txt").read()
test_requirements = open("requirements-tests.txt").read()

import version

setup(
    name='lolcommitss',
    version=version.APP_VERSION,
    description="",
    long_description=readme,
    author="Jean-Christophe Saad-Dupuy",
    author_email='jc.saaddupuy@fsfe.org',
    url='https://github.com/jcsaaddupuy/lolcommitss',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),


    # configure the default command line entry point.
    entry_points={
        'console_scripts': [
            'lolcommitss-manage = lolcommitss.manage:main',
        ]
    },



    include_package_data=True,
    package_data={
        'templates' : 'lolcommitss/apps/default/templates/*'
    },

    install_requires=requirements,
    license="WTFPL",
    zip_safe=False,
    keywords='lolcommitss',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
