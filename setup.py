from setuptools import setup, find_packages

setup(
    name = "mergepic",
    version = "1.0",
    keywords = ("image", "merge"),
    description = "image merge",
    long_description = "Provide a dictionary contains several images, row, every image scale (or padding), output merge result.",

    author = "xys",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires =['numpy>=1.8', 'opencv>=4.2'],
    entry_points={'console_scripts': [
        'ent = mergepic.merge:main',
    ]},
)
