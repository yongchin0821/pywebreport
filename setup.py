#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pywebreport",
    version="0.1.0",
    author="Yongchin",
    author_email="yongchin39@qq.com",
    license="MIT",
    description="Generates a static html report based on pytest framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["pytest", "unittest", "htmlreport", "reporter", "report", "pytest report"],
    url="https://github.com/yongchin0821/pywebreport",
    project_urls={
        "Bug Tracker": "https://github.com/yongchin0821/pywebreport/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
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
            "reporter = pywebreport.plugins.pytest.plugin",
        ],
    },
)
