import argparse
import sys
import os
import subprocess

"""YunoHost helper to run ansible roles"""


PLAYBOOK_PATH = '/usr/share/ansible-yunohost/playbooks/ynh-app-operation.yml'


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest='operation')

    parser_install = subparsers.add_parser('install')
    parser_upgrade = subparsers.add_parser('upgrade')
    parser_remove = subparsers.add_parser('remove')

    for i in parser_install, parser_upgrade, parser_remove:
        i.add_argument('app_name')

    parser_install.add_argument('vars')

    for i in parser_upgrade, parser_remove:
        parser_upgrade.set_defaults(vars=None)

    return parser.parse_args()


def main():
    args = parse_args()

    subprocess.check_call(['sudo', 'apt-get', 'install', '-y', 'ansible'])
    cmd = [
        'ansible-playbook',
        '-i', 'localhost,', '-c', 'local',
        '-e', 'app_name={} app_pkg_path={} operation={}'.format(
            args.app_name, os.getcwd(), args.operation),
        PLAYBOOK_PATH
    ]
    if args.vars is not None:
        cmd += ['-e', args.vars]

    subprocess.check_call(cmd, stdout=sys.stdout, stderr=sys.stderr)


if __name__ == '__main__':
    main()
