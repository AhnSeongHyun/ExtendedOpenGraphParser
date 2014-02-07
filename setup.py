from setuptools import setup, find_packages

version = '0.2'

setup(name='ExtendedOpenGraph',

      version=version,
      description="A module of parsing the open graph protocol and extracing the summary of the web page.",
      long_description=open("pip_desc.txt").read() + "\n",
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python',
      'Topic :: Text Processing :: Markup :: HTML',
      'Topic :: Software Development :: Libraries :: Python Modules',
      ], 
      keywords='opengraph protocol facebook',
      author='SeongHyun.Ahn',
      author_email='sh84.ahn@gmail.com',
      url='https://github.com/AhnSeongHyun/ExtendedOpenGraphParser',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'beautifulsoup4',
          'opengraph'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      
      )