from setuptools import setup, find_packages

setup(
    name = "mergepic",
    version = "1.0",
    keywords = ("image", "merge"),
    description = "image merge",
    long_description = "Provide a dictionary contains several images, row, every image scale (or padding), output merge result.",
    license = "MIT Licence",

    author = "xys",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires =[],
)
