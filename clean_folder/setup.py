from setuptools import setup

setup(
   name='clean_folder',
   version='0.0.1',
   description='A useful module - student work',
   url='https://github.com/chabanchuk/sort',
   author='Serhii Chabanchuk',
   author_email='chabanchuk@gmail.com',
   license='MIT',
   packages=['clean_folder'],
   install_requires = [],
   entry_points={'console_sсripts': ['clean-folder=clean_folder.clean:main']}
)