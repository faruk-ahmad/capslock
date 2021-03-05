import codecs
import setuptools


setuptools.setup(
    name="capslock",
    version="1.0.6",
    author="Faruk Ahmad",
    author_email="faruk.csebrur@gmail.com",
    description="A utility python library for writing certain tasks in python easily & elegantly.",
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/faruk-ahmad/capslock",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'matplotlib'],
    python_requires='>=3.5',
    
)
