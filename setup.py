from setuptools import find_packages, setup

from henson_sentry import __version__

setup(
    name='Henson-Sentry',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'Henson',
        'raven',
    ],
    tests_require=[
        'tox',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
    ]
)
