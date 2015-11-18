from setuptools import setup

setup(
    name='ansible-yunohost',
    license='WTFPL',
    author='Jocelyn Delalande',
    author_email='jocelyn@crapouillou.net',
    url='https://github.com/JocelynDelalande/ansible-yunohost/',
    packages=['ansible_ynh'],
    entry_points={
        'console_scripts': [
            'ynh_ansible_operation = ansible_ynh.helper:main'
        ],
    },
    data_files=[
        ('/usr/share/ansible-yunohost/playbooks/',
         ['playbooks/ynh-app-operation.yml']),
        ('/usr/share/ansible-yunohost/playbooks/library/',
         ['playbooks/library/ynh_app'])
    ],
)
