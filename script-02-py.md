# Домашнее задание к занятию «Использование Python для решения типовых DevOps-задач»
----------------

## Задание 1

Есть скрипт:

```python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```

### Вопросы:

| Вопрос  | Ответ |
| ------------- | ------------- |
| Какое значение будет присвоено переменной `c`?  | Выйдет ошибка, так как складывать целое и строку нельзя  |
| Как получить для переменной `c` значение 12?  | a = '1'  |
| Как получить для переменной `c` значение 3?  | b = 2 |

------

## Задание 2

Мы устроились на работу в компанию, где раньше уже был DevOps-инженер. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. 

Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```

### Ваш скрипт:

```python
#!/usr/bin/env python3

import os

PATH = r"C:\CODE\Netology\DevOps\devops-netology"
os.chdir(PATH)

bash_command = ["git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(os.path.join(PATH, prepare_result))
```

### Вывод скрипта при запуске во время тестирования:

```
C:\CODE\Netology\DevOps\devops-netology>python git_script.py
C:\CODE\Netology\DevOps\devops-netology\git_script.py
C:\CODE\Netology\DevOps\devops-netology\script-02-py.md

C:\CODE\Netology\DevOps\devops-netology>
```

------

## Задание 3

Доработать скрипт выше так, чтобы он не только мог проверять локальный репозиторий в текущей директории, но и умел воспринимать путь к репозиторию, который мы передаём, как входной параметр. Мы точно знаем, что начальство будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

### Ваш скрипт:

```python
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
```

### Вывод скрипта при запуске во время тестирования:

```
C:\CODE\Netology\DevOps\devops-netology>python git_script.py
Введите путь к локальному репозиторию: .\
.\git_script.py
.\script-02-py.md

C:\CODE\Netology\DevOps\devops-netology>python git_script.py .\
.\git_script.py
.\script-02-py.md

C:\CODE\Netology\DevOps\devops-netology>
```
### Вывод скрипта при запуске во время тестирования на Linux:
```
fedor@DESKTOP-FEKCCDN:/mnt/c/CODE/Netology/DevOps$ python3 devops-netology/git_script.py devops-netology
devops-netology/git_script.py
devops-netology/script-02-py.md
fedor@DESKTOP-FEKCCDN:/mnt/c/CODE/Netology/DevOps$ python3 devops-netology/git_script.py
Введите путь к локальному репозиторию: devops-netology
devops-netology/git_script.py
devops-netology/script-02-py.md
fedor@DESKTOP-FEKCCDN:/mnt/c/CODE/Netology/DevOps$
```
------

## Задание 4

Наша команда разрабатывает несколько веб-сервисов, доступных по HTTPS. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. 

Проблема в том, что отдел, занимающийся нашей инфраструктурой, очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS-имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. 

Мы хотим написать скрипт, который: 

- опрашивает веб-сервисы; 
- получает их IP; 
- выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. 

Также должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена — оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: `drive.google.com`, `mail.google.com`, `google.com`.

### Ваш скрипт:

```python
import os
import socket
import json

SERVICES = ["drive.google.com", "mail.google.com", "google.com"]
SERVICES_JSON = "services.json"

service_ips = {}
prev_ips = None

if os.access(SERVICES_JSON, os.R_OK):
    with open(SERVICES_JSON, "r", encoding = "utf-8") as f:
        prev_ips = json.load(f)

for service in SERVICES:
    try:
        serv_ip = socket.gethostbyname(service)
        print(service, "-", serv_ip)
        service_ips[service] = serv_ip
        if prev_ips and prev_ips.get(service) and prev_ips[service] != service_ips[service]:
            print(f"[ERROR] {service} IP mismatch: {prev_ips[service]} {service_ips[service]}")
    except:
        print(f'Can not gethostbyname("{service}")')

if not os.access(SERVICES_JSON, os.F_OK) or os.access(SERVICES_JSON, os.W_OK):
    with open(SERVICES_JSON, "w", encoding = "utf-8") as f:
        json.dump(service_ips, f)
else:
    print(f"Can not write to file {SERVICES_JSON}")
```

### Вывод скрипта при запуске во время тестирования:

```
C:\CODE\Netology\DevOps\devops-netology>python dns_script.py
drive.google.com - 108.177.14.194
[ERROR] drive.google.com IP mismatch: 74.125.205.194 108.177.14.194
mail.google.com - 74.125.205.19
[ERROR] mail.google.com IP mismatch: 74.125.205.17 74.125.205.19
google.com - 64.233.165.139
[ERROR] google.com IP mismatch: 64.233.165.102 64.233.165.139
```
