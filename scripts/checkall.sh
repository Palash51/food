#! /bin/bash

python manage.py test \
    && python manage.py behave \
    && ./scripts/linters.sh \

exit $?
