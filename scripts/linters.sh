#! /bin/bash

computed=$(find ./base -maxdepth 1 -mindepth 1 -type d | paste -sd ":" -)
PYTHONPATH="$computed" pylint account, orders && flake8 .

exit $?
