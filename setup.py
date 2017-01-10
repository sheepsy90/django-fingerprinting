# -*- coding: utf-8 -*-
import os.path
from distutils.core import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='django-fingerprinting',
    version='1.0.0',
    keywords='django staticfiles',
    author=u'Sheepsy90 <sheepsy90@gmail.com>',
    packages=['django_fingerprinting'],
    url='https://github.com/sheepsy90/django-fingerprinting',
    license='see LICENCE',
    description='Replace names of static files and resources that are accessed from templates',
    long_description=read('README.md'),
    requires=[
        'Django',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ]
)
