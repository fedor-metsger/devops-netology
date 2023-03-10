

## Ответы к домашнему заданию к занятию
# «Операционные системы. Лекция 2»

2. **Изучите опции node_exporter и вывод /metrics по умолчанию.
Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.**

    Я бы  использовал следующие опции:
    - node_cpu_seconds_total{cpu=\<номер CPU\>,mode="idle"}
    - node_cpu_seconds_total{cpu=\<номер CPU\>,mode="system"}
    - node_cpu_seconds_total{cpu=\<номер CPU\>,mode="user"}
    
    - node_memory_MemTotal_bytes
    - node_memory_MemFree_bytes
    - node_memory_MemAvailable_bytes
    - node_memory_MemBuffers_bytes
    
    - node_disk_info
    - node_disk_read_time_seconds_total
    - node_disk_read_bytes_total 
    - node_disk_reads_completed_total
    - node_disk_write_time_seconds_total
    - node_disk_written_bytes_total
    - node_disk_writes_completed_total
    
    - node_filesystem_size_bytes
    - node_filesystem_free_bytes
    
    - node_network_info
    - node_network_receive_bytes_total
    - node_network_receive_drop_total
    - node_network_receive_errs_total
    - node_network_receive_packets_total
    - node_network_transmit_bytes_total
    - node_network_transmit_colls_total
    - node_network_transmit_errs_total
    - node_network_transmit_drop_total
    - node_network_transmit_queue_length
    - node_network_transmit_packets_total
    
4. **Можно ли по выводу dmesg понять, осознаёт ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?**

    Можно. Например по строчке:
    ```
    [    0.000000] DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006
    ```

5. **Как настроен sysctl fs.nr_open на системе по умолчанию? Определите, что означает этот параметр.
Какой другой существующий лимит не позволит достичь такого числа (ulimit --help)?**

    Параметр обозначает максимальное количество открытых процессом файлов.

    ```
    root@vagrant:/lib/systemd/system# sysctl fs.nr_open
    fs.nr_open = 1048576
    ```
    
    Есть другой лимит, который задаётся шеллом на порождаемые им процессы. Он значительно меньше:
    ```
    root@vagrant:/lib/systemd/system# ulimit -n
    1024
    ```

6. **Запустите любой долгоживущий процесс (не ls, который отработает мгновенно, а, например, sleep 1h)
в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через nsenter.**

    ```
    root@vagrant:/lib/systemd/system# unshare -f --pid --mount-proc sleep 1h
    ...
    vagrant@vagrant:~$ ps -ef | grep sleep
    root        1711    1375  0 04:40 pts/1    00:00:00 unshare -f --pid --mount-proc sleep 1h
    root        1712    1711  0 04:40 pts/1    00:00:00 sleep 1h
    vagrant     1768    1755  0 04:41 pts/0    00:00:00 grep --color=auto sleep
    vagrant@vagrant:~$ sudo nsenter --target 1712 --pid --mount
    root@vagrant:/# ps -ef
    UID          PID    PPID  C STIME TTY          TIME CMD
    root           1       0  0 04:40 pts/1    00:00:00 sleep 1h
    root           2       0  0 04:42 pts/0    00:00:00 -bash   
    root          13       2  0 04:42 pts/0    00:00:00 ps -ef
    root@vagrant:/#
    ```

7. **Найдите информацию о том, что такое :(){ :|:& };:.
    Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 (это важно, поведение в других ОС не проверялось).
    Некоторое время всё будет плохо, после чего (спустя минуты) — ОС должна стабилизироваться.
    Вызов dmesg расскажет, какой механизм помог автоматической стабилизации.
    Как настроен этот механизм по умолчанию, и как изменить число процессов, которое можно создать в сессии?**

    ```
    vagrant@vagrant:~$ dmesg | tail -3
    [   18.961603] 03:27:57.144547 main     vbglR3GuestCtrlDetectPeekGetCancelSupport: Supported (#1)
    [ 4613.858202] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-4.scope
    [ 4628.071411] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-6.scope
    vagrant@vagrant:~$
    ```
    **systemd** создаёт для каждого пользователя **cgroup**, и все процессы этого пользователя входят в эту группу.
    **cgroup** - это механизм линукс, позволяющий ограничивать потребление ресурсов, таких как количество процессов,
    количество времени ЦПУ, потребление ОЗУ итд. Это более современный механизм, чем **ulimit**.
    По умолчанию ограничение на максимальное количество процессов пользователя выставлено в 33% от общесистемного:
    ```
    vagrant@vagrant:~$ sysctl kernel.threads-max
    kernel.threads-max = 7383
    vagrant@vagrant:~$ systemctl status user-1000.slice
    user-1000.slice - User Slice of UID 1000
       Loaded: loaded
      Drop-In: /usr/lib/systemd/system/user-.slice.d
               └─10-defaults.conf
       Active: active since Fri 2023-03-10 03:28:27 UTC; 5h 15min ago
         Docs: man:user@.service(5)
        Tasks: 17 (limit: 2436)
    ```
    
    Ограничение в 33% задаётся в файле **/usr/lib/systemd/system/user-.slice.d/10-defaults.conf**:
    ```
    vagrant@vagrant:~$ cat /usr/lib/systemd/system/user-.slice.d/10-defaults.conf
    #  SPDX-License-Identifier: LGPL-2.1+
    #
    #  This file is part of systemd.
    #
    #  systemd is free software; you can redistribute it and/or modify it
    #  under the terms of the GNU Lesser General Public License as published by
    #  the Free Software Foundation; either version 2.1 of the License, or
    #  (at your option) any later version.

    [Unit]
    Description=User Slice of UID %j
    Documentation=man:user@.service(5)
    After=systemd-user-sessions.service
    StopWhenUnneeded=yes

    [Slice]
    TasksMax=33%
    vagrant@vagrant:~$
    ```
