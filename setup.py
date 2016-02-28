from __future__ import print_function

from setuptools import setup, find_packages


setup(name='dram',
      version='0.0.1.dev',
      description='Keeping your Package Manager Packaged',
      long_description='',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
      ],
      keywords='shell macports homebrew software dependencies package manager',
      url='https://github.com/storborg/dram',
      author='Scott Torborg',
      author_email='storborg@gmail.com',
      license='MIT',
      packages=find_packages(),
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False,
      scripts=['dram.sh'],
     )