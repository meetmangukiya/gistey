from setuptools import setup

with open('requirements.txt') as req:
    dependencies = req.read().splitlines()

with open('README.rst') as readme:
    long_description = readme.read()

if __name__ == "__main__":
    setup(
        name='gistey',
        version="0.1.0",
        description="Make GitHub gists from cmdline/terminal",
        long_description=long_description,
        author="Meet Mangukiya",
        author_email="meetmangukiya98@gmail.com",
        maintainer="Meet Mangukiya",
        maintainer_email=("meetmangukiya98@gmail.com", ),
        url="http://meetmangukiya.github.io",
        install_requires=dependencies,
        license='MIT',
        packages=['gistey'],
        entry_points = {
            'console_scripts': [
                'gistey=gistey.gistey:main'
            ]
        }
    )
