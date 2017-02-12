from distutils.core import setup

setup(
    # Application name:
    name="The Monitor",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="V3ckt0r",
    author_email="",

    # Packages
    packages=["Themonitor"],

    # Include additional files into the package
    include_package_data=True,

    entry_points={
            'console_scripts': [
                'themonitor = Themonitor.themonitor:main',
            ]
    },

    # Details
    url="https://github.com/V3ckt0r/TheMonitor",

    #
    license="LICENSE.txt",
    description="The Monitor that looks into the soul.",

    long_description=open("DESCRIPTION.rst").read(),

    # Dependent packages (distributions)
    install_requires=[
        "",
    ],
)
