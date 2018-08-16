#!/usr/bin/env python

import os
import sys

# setup the environment
# make sure to source scripts/env.sh or scripts/common.sh
SETTINGS = 'foood.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = SETTINGS


def cmd(txt):
    os.system(txt)


def actions(cmds):
    for c in cmds:
        cmd(c)


def start():
    actions([
        'dropdb food',
        'sleep 1',
        'createdb food',
        './manage.py migrate',
        './manage.py createsuperuser --username=admin --email=sa@me.org',
    ])


def run_sample_data(module='config_ritcco_empty'):
    print('> Bootstrapping with: {}'.format(module))
    cmd('python data/input/{}.py'.format(module))


def main():
    start()

    try:
        run_sample_data(sys.argv[1])
    except IndexError:
        run_sample_data()


if __name__ == '__main__':
    main()
