from setuptools import setup
from setuptools import find_packages


setup(name='junos-collector',
      version='1.0.0',
      description='Junos simple collector',
      author='Syed Ridzuan',
      author_email='syridzuan@gmail.com',
      url='https://github.com/syedridzuan/junos-collector',
      download_url='https://github.com/syedridzuan/junos-collector/tarball/1.0.0',
      license='MIT',
      install_requires=['paramiko'],
      packages=find_packages())