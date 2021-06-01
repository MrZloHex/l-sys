from setuptools import setup
from codecs import open


# Get the long description from the README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="l-sys",
    version="1.1.2",
    description="L-Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MrZloHex/l-sys",
    author="MrZloHex",
    author_email="zlo.alex.it@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["l_sys"],
    include_package_data=True,
)
