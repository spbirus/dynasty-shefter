from setuptools import setup

setup(
    name='schefter-bot',

    packages=['schefter-bot'],

    include_package_data=True,

    version='0.0.1',

    description='Schefter Dynasty GroupMe Bot',

    author='Sam Birus',

    author_email='burritophil@gmail.com',

    install_requires=['requests>=2.0.0,<3.0.0', 'ff_espn_api>=1.1.6', 'apscheduler>3.0.0'],

    url='https://github.com/spbirus/dynasty-shefter',

    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)