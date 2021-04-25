#!/usr/bin/env bash
 
rm -rf build dist
python3 setup.py clean sdist bdist_wheel upload -r pypi