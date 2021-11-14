from distutils.core import setup
from setuptools import find_packages
setup(name='ow77aham',
      version='1.0',
      author='DSSS',
      author_email='quirin.bufler@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets'])