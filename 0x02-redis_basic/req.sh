#!/usr/bin/env bash
# This should help automate the process of:
# 1. making all `.py` files in current folder executable
# 2. checking code standard with pycodestyle

chmod u+x *.py

# check first argument for pycodestyle
pycodestyle "$1"
