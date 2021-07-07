import os
from setuptools import setup, find_packages


def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()


setup(
    name="algorithms",
    version="0.0.1",
    author="Marcin Baranek",
    author_email="baranekmarcin47@gmail.com",
    description="Python package with some algorithms",
    license="",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: MIT",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    keywords="permutation",
    url="https://github.com/MarcinBaranek/stopy",
    packages=find_packages(exclude=['algorithms']),
    long_description=read('README.md'),
    install_requiers=["numpy"],
    include_package_data=True,
    zip_safe=False
)
