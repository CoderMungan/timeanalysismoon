from setuptools import setup, find_packages

setup(
    name='timeanalysismoon',
    version='0.1',
    packages=find_packages(),
    author='CoderMungan',
    author_email='codermungan@gmail.com',
    description='A time analysis decorator for Python functions',
    long_description='A decorator that measures and prints the execution time of a function.',
    url='https://github.com/CoderMungan/timeanalysismoon',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
)