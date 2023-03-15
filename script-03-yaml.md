# Домашнее задание к занятию «Языки разметки JSON и YAML»

### 1. Мы выгрузили JSON, который получили через API-запрос к нашему сервису:

```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
###  Нужно найти и исправить все ошибки, которые допускает наш сервис.

### Ваш скрипт:

```
    { "info":"Sample JSON output from our service",
        "elements":[
            { "name":"first",
            "type":"server",
            "ip":"71.75.XX.XX"
            },
            { "name":"second",
            "type":"proxy",
            "ip":"71.78.22.43"
            }
        ]
    }
```

---

### 2. В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML-файлов, описывающих наши сервисы. 

Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. 

Формат записи YAML по одному сервису: `- имя сервиса: его IP`. 

Если в момент исполнения скрипта меняется IP у сервиса — он должен так же поменяться в YAML и JSON-файле.

### Ваш скрипт:

```python
import os
import socket
import json
import yaml

SERVICES = ["drive.google.com", "mail.google.com", "google.com"]
SERVICES_JSON = "services.json"
SERVICES_YAML = "services.yaml"

service_ips = {}
yaml_ips = []
prev_ips = None

if os.access(SERVICES_JSON, os.R_OK):
    with open(SERVICES_JSON, "r", encoding = "utf-8") as f:
        prev_ips = json.load(f)

for service in SERVICES:
    try:
        serv_ip = socket.gethostbyname(service)
        print(service, "-", serv_ip)
        service_ips[service] = serv_ip
        yaml_ips.append({service: serv_ip})
        if prev_ips and prev_ips.get(service) and prev_ips[service] != service_ips[service]:
            print(f"[ERROR] {service} IP mismatch: {prev_ips[service]} {service_ips[service]}")
    except:
        print(f'Can not gethostbyname("{service}")')

if not os.access(SERVICES_JSON, os.F_OK) or os.access(SERVICES_JSON, os.W_OK):
    with open(SERVICES_JSON, "w", encoding = "utf-8") as f:
        json.dump(yaml_ips, f)
else:
    print(f"Can not write to file {SERVICES_JSON}")

if not os.access(SERVICES_YAML, os.F_OK) or os.access(SERVICES_YAML, os.W_OK):
    with open(SERVICES_YAML, "w", encoding = "utf-8") as f:
        f.write(yaml.dump(yaml_ips))
else:
    print(f"Can not write to file {SERVICES_YAML}")
```

### Вывод скрипта при запуске во время тестирования:

```
C:\CODE\Netology\DevOps\devops-netology>python dns_script.py
drive.google.com - 108.177.14.194
mail.google.com - 74.125.205.18
[ERROR] mail.google.com IP mismatch: 74.125.205.17 74.125.205.18
google.com - 64.233.165.101
```

### JSON-файл(ы), который(е) записал ваш скрипт:

```json
[{"drive.google.com": "108.177.14.194"}, {"mail.google.com": "74.125.205.18"}, {"google.com": "64.233.165.101"}]
```

### YAML-файл(ы), который(е) записал ваш скрипт:

```yaml
- drive.google.com: 108.177.14.194
- mail.google.com: 74.125.205.18
- google.com: 64.233.165.101
```
