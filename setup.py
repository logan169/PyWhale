#!/usr/bin/env python

from setuptools import setup

setup(name='pywhale',
      version='0.1',
      description='python wrapper for Whaleclub.co exchange platform API',
      url='https://github.com/logan169/PyWhale',
      author='Logan Schwartz',
      author_email='logan1691987@gmail.com',
      license='GPLv3',
      python_requires='>=3',
      classifiers=[
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Intended Audience :: Financial and Insurance Industry',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Topic :: Office/Business',
            'Topic :: Office/Business :: Financial'
      ],
      keywords='python python3 whaleclub crypto pywhale trade trading api bitcoin wrapper',
      packages=['pywhale'],
      install_requires=['requests', 'statistics'],
zip_safe=False)
