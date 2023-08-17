from setuptools import find_packages, setup

setup(
    name = 'sorter',
    version = '0.1.0',
    packages = find_packages(),
    include_package_data = True,
    package_data={"": ["*.json"]},
    entry_points = {
        'console_scripts': ['sorter=sorter:sort'],
    }
)