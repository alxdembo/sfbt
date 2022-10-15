from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    version='0.1',
    scripts=['bin/sfbt'],
    url='https://github.com/alxdembo/synatools',
    description='Step function build tool',
    long_description=readme(),
    author='Alex Dembo',
    packages=['sfbt'],
    install_requires=['dbt-core']
)
