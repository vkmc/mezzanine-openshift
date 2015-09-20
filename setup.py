#!/usr/bin/env python

from setuptools import setup

setup(
    name='mezzanine-openshift',
    version='1.3',
    description='Mezzanine configured for deployment on OpenShift.',
    author='Victoria Martinez de la Cruz',
    author_email='victoria@vmartinezdelacruz.com',
    url='http://vmartinezdelacruz.com/',
    install_requires=[
        'mezzanine==4.0.1',
    ],
)
