#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


setup(
    name="pywebreport",
    version="0.0.1",
    author="Yongchin",
    author_email="yongchin39@qq.com",
    license="MIT",
    url="https://github.com/prashanth-sams/pytest-html-reporter",
    description="Generates a static html report based on pytest framework",
    keywords=["pytest", "py.test", "html", "reporter", "report"],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=["pytest"],
    classifiers=[
        "Framework :: Pytest",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "pytest11": [
            "reporter = plugins.pytest.plugin",
        ],
    },
)
