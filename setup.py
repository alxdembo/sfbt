from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    version='0.1',
    scripts=['bin/synatools'],
    url='https://github.com/alxdembo/synatools',
    description='The funniest joke in the world',
    long_description=readme(),
    author='Alex Dembo',
    packages=['synatools'],
)
