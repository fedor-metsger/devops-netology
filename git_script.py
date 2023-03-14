#!/usr/bin/env python3

import os

os.chdir(r"C:\CODE\Netology\DevOps\devops-netology")
bash_command = ["git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = os.pathresult.replace('\tmodified:   ', '')
        print(prepare_result)
        break