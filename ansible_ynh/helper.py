import argparse
import sys
import os
import subprocess
from pkg_resources import Requirement, resource_filename

"""YunoHost helper to run ansible roles"""


def get_playbook_filename():
    return os.path.join(
        resource_filename(Requirement.parse("ansible-yunohost"), "playbooks"),
        'ynh-app-operation.yml')


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation')
    parser.add_argument('app_name')
    parser.add_argument('vars')
    return parser.parse_args()


def main():
    args = parse_args()

    subprocess.check_call(['sudo', 'apt-get', 'install', '-y', 'ansible'])
    cmd = [
        'ansible-playbook',
        '-i', 'localhost,', '-c', 'local',
        '-e', 'app_name={} app_pkg_path={} operation={}'.format(
            args.app_name, os.getcwd(), args.operation),
        '-e', args.vars,
        get_playbook_filename()
    ]
    subprocess.check_call(cmd, stdout=sys.stdout, stderr=sys.stderr)


if __name__ == '__main__':
    main()
