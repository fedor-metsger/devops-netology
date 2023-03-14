#!/usr/bin/python3

import os
import sys

if len(sys.argv) > 1:
    PATH=sys.argv[1]
else:
    PATH=input("Введите путь к локальному репозиторию: ")
#PATH = r"C:\CODE\Netology\DevOps\devops-netology"
os.chdir(PATH)

bash_command = ["git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(os.path.join(PATH, prepare_result))