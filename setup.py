# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name="polygon_session",
    packages=["polygon_session"],
    version="0.0.1",
    description="A requests session manager for requests that handles authentication.",
    long_description="It is a polygon.io session adaptor for the requests library that handles authentication.",
    author="Adam DePrince (adamdeprince)",
    author_email="adam.deprince@gmail.com",
    url="https://github.com/adamdeprince/polygon_session",
    maintainer="Adam DePrince (adamdeprince)",
    maintainer_email="adam.deprince@gmail.com",
    install_requires=[
        "requires"
    ],
    keywords=["polygon.io", "requires"],
    license="The MIT License (MIT)",
    license_files=["LICENSE"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={
        "Bug Reports": "https://github.com/adamdeprince/polygon_session/issues",
        "Source": "https://github.com/adamdeprince/polygon_session",
    },
)
