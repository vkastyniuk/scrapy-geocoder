#!/usr/bin/env python
from setuptools import setup

setup(
    name='scrapy-geocoder',
    version='0.1.0',
    url='https://github.com/vkastyniuk/scrapy-geocoder',
    description='A scrapy pipeline to resolve item geo coordinates by address',
    long_description=open('README.md').read(),
    author='Viachaslau Kastyniuk',
    maintainer='Viachaslau Kastyniuk',
    maintainer_email='viachaslau.kastyniuk@gmail.com',
    license='BSD',
    packages=['scrapy_geocoder'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    requires=['scrapy', 'geocoder', 'six'],
)
