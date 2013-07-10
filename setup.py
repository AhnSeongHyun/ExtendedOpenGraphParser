from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ExtendedOpenGraph',
      version=version,
      description="A module to parse the Open Graph Protocol",
      long_description=open("README.rst").read() + "\n",
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python',
      'Topic :: Text Processing :: Markup :: HTML',
      'Topic :: Software Development :: Libraries :: Python Modules',
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='opengraph protocol facebook',
      author='AhnSeongHyun',
      author_email='sh84.ahn@gmail.com',
      url='https://github.com/AhnSeongHyun/ExtendedOpenGraphParser',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'beautifulsoup4'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )