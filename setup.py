#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="today",
    version="0.2",
    description="today's date",
    author="Sven Rodriguez",
    author_email="svenbmr@gmail.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "today = today.today:today",
            "dateof = today.today:dateof",
        ]
    },
)
