import os

from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.

    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.

    Args:
        nothing

    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='hyspexutil',
    version='0.1.0',
    author='Chris Waigl',
    author_email='cwaigl@alaska.edu',
    description='Analysis of 1m HySpex data aquired 2019+ at UAF',
    python_requires='>=3',
    license='MIT',
    url='',
    packages=find_packages(),
    long_description=readme(),
)