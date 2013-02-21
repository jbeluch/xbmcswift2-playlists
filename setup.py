import os
from setuptools import setup, find_packages


setup(
    name = 'xbmcswift2_playlists',
    version = '0.1.0-dev',
    author = 'Jonathan Beluch',
    author_email = 'web@jonathanbeluch.com',
    #description = 'A micro framework for rapid development of XBMC plugins.',
    license = "GPL3",
    #keywords = "example documentation tutorial",
    #url = 'https://github.com/jbeluch/xbmcswift2',
    #packages=find_packages(),
    #include_package_data=True,
    long_description=__doc__,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
    ],
)
