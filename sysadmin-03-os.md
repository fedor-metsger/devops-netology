

## Ответы к домашнему заданию к занятию
# «Операционные системы. Лекция 1»

  Я уже имею установленную Ubuntu 22.04, поэтому задание выполнил на ней.

1. **Какой системный вызов делает команда cd?**

    Вызывает **chdir**. Вырезка из **strace**:
    ```
    newfstatat(AT_FDCWD, "/tmp", {st_mode=S_IFDIR|S_ISVTX|0777, st_size=4096, ...}, 0) = 0
    chdir("/tmp")
    ```

2. **Попробуйте использовать команду file на объекты разных типов в файловой системе.**
    ```
    fedor@DESKTOP-FEKCCDN:~$ file /bin/bash
    /bin/bash: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,        BuildID[sha1]=33a5554034feb2af38e8c75872058883b2988bc5, for GNU/Linux 3.2.0, stripped
    fedor@DESKTOP-FEKCCDN:~$ file /etc/hosts
    /etc/hosts: ASCII text
    fedor@DESKTOP-FEKCCDN:~$ file __main__.py
    __main__.py: Python script, ASCII text executable
    fedor@DESKTOP-FEKCCDN:~$
    ```
    
    База данных команды файл находится в **/usr/lib/file/magic.mgc**:
    ```
    openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3
    
    ...
    
    vagrant@vagrant:~$ ls -l /usr/share/misc/magic.mgc
    lrwxrwxrwx 1 root root 24 Jan 16  2020 /usr/share/misc/magic.mgc -> ../../lib/file/magic.mgc
    vagrant@vagrant:~$ ls -l /usr/lib/file/magic.mgc
    -rw-r--r-- 1 root root 5811536 Jan 16  2020 /usr/lib/file/magic.mgc
    vagrant@vagrant:~$
    ```

3. **Предположим, приложение пишет лог в текстовый файл. Этот файл оказался удалён (deleted в lsof), но сказать сигналом приложению переоткрыть файлы или просто перезапустить приложение возможности нет. Так как приложение продолжает писать в удалённый файл, место на диске постепенно заканчивается. Основываясь на знаниях о перенаправлении потоков, предложите способ обнуления открытого удалённого файла, чтобы освободить место на файловой системе.**

    С помощью команды **`cat /dev/null > /proc/\<PID\>/fd/\<дескриптор\>`** можно обнулить удалённый файл:
    ```
    vagrant@vagrant:~$ dd if=/dev/zero of=bigfile bs=1000000 count=100
    100+0 records in
    100+0 records out
    100000000 bytes (100 MB, 95 MiB) copied, 0.187829 s, 532 MB/s
    vagrant@vagrant:~$ df -k .
    Filesystem                        1K-blocks    Used Available Use% Mounted on
    /dev/mapper/ubuntu--vg-ubuntu--lv  31811408 4402860  25767076  15% /
    vagrant@vagrant:~$ ls -l /proc/self/fd
    total 0
    lrwx------ 1 vagrant vagrant 64 Mar  9 16:44 0 -> /dev/pts/1
    lrwx------ 1 vagrant vagrant 64 Mar  9 16:44 1 -> /dev/pts/1
    lrwx------ 1 vagrant vagrant 64 Mar  9 16:44 2 -> /dev/pts/1
    lr-x------ 1 vagrant vagrant 64 Mar  9 16:44 3 -> /proc/48963/fd
    vagrant@vagrant:~$ exec 3<bigfile
    vagrant@vagrant:~$ ls -l /proc/self/fd
    total 0
    lrwx------ 1 vagrant vagrant 64 Mar  9 16:44 0 -> /dev/pts/1
    lrwx------ 1 vagrant vagrant 64 Mar  9 16:44 1 -> /dev/pts/1
    lrwx------ 1 vagrant vagrant 64 Mar  9 16:44 2 -> /dev/pts/1
    lr-x------ 1 vagrant vagrant 64 Mar  9 16:44 3 -> /home/vagrant/bigfile
    lr-x------ 1 vagrant vagrant 64 Mar  9 16:44 4 -> /proc/48964/fd
    vagrant@vagrant:~$ rm /home/vagrant/bigfile
    vagrant@vagrant:~$ df -k .
    Filesystem                        1K-blocks    Used Available Use% Mounted on
    /dev/mapper/ubuntu--vg-ubuntu--lv  31811408 4402860  25767076  15% /
    vagrant@vagrant:~$ cat /dev/null > /proc/self/fd/3
    vagrant@vagrant:~$ df -k .
    Filesystem                        1K-blocks    Used Available Use% Mounted on
    /dev/mapper/ubuntu--vg-ubuntu--lv  31811408 4305200  25864736  15% /
    vagrant@vagrant:~$
    ```
4. **Занимают ли зомби-процессы ресурсы в ОС (CPU, RAM, IO)?**

    Нет. Зомби процесс это только запись в таблице процессов о завершившемся процессе. Ресурсов он не занимает.

5. **В IO Visor BCC есть утилита opensnoop:**
    ```
    root@vagrant:~# dpkg -L bpfcc-tools | grep sbin/opensnoop
    /usr/sbin/opensnoop-bpfcc
    ```
    
    **На какие файлы вы увидели вызовы группы open за первую секунду работы утилиты? Воспользуйтесь пакетом bpfcc-tools для Ubuntu 20.04. Дополнительные сведения по установке по ссылке.**
    
    В первую секунду идут обращения к:
    - динамическим библиотекам
    - файлам связанным с **locale**
    - различные python файлы из каталога **/usr/lib/python3.8**
    Потом начинается работа с **kernel-headers**

 6. **Какой системный вызов использует uname -a? Приведите цитату из man по этому системному вызову, где описывается альтернативное местоположение в /proc и где можно узнать версию ядра и релиз ОС.**

    Системный вызов **uname**:
    ```
    uname({sysname="Linux", nodename="DESKTOP-FEKCCDN", ...}) = 0
    newfstatat(1, "", {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0), ...}, AT_EMPTY_PATH) = 0
    uname({sysname="Linux", nodename="DESKTOP-FEKCCDN", ...}) = 0
    uname({sysname="Linux", nodename="DESKTOP-FEKCCDN", ...}) = 0
    write(1, "Linux DESKTOP-FEKCCDN 5.10.16.3-"..., 122Linux DESKTOP-FEKCCDN 5.10.16.3-microsoft-standard-WSL2 #1 SMP Fri Apr 2 22:23:49 UTC
    ```
    
    Цитата из **man uname**:
    ```
    Part of the utsname information is also accessible via
    /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}.
    ```

 7. **Чем отличается последовательность команд через ; и через && в bash? Например:**
    ```
    root@netology1:~# test -d /tmp/some_dir; echo Hi
    Hi
    root@netology1:~# test -d /tmp/some_dir && echo Hi
    root@netology1
    ```
    
    Команды, разделённые точкой с запятой будут выполняться по очереди в любом случае. Команда, стоящая после **&&**
    будет выполнена только тогда, когда предыдущая завершилась успешно.
    
    **Есть ли смысл использовать в bash &&, если применить set -e?**
    
    Есть. В случае если команда перед **&&** завершится с ошибкой, шелл не завершит работу, даже если установлено **set -e**

 8. **Из каких опций состоит режим bash set -euxo pipefail, и почему его хорошо было бы использовать в сценариях?**
    
    Состоит из опций:  
    **-e** Завершаться с ошибкой после любой команды, завершившейся с ошибкой  
    **-u** Завершаться с ошибкой, если используется не установленная переменная  
    **-x** Выводить PS4 перед выполнением очередной команды    
    **-o pipefail** Результатом выполнения составной команды с пайплайном будет результат последней команды, завершившейся с ошибкой.  
    Я думаю эти параметры полезны для большего контроля над происходящим в скрипте, так как позволяют выявить больше ошибок в процессе исполнения.
    

 9. **Используя -o stat для ps, определите, какой наиболее часто встречающийся статус у процессов в системе. В man ps изучите (/PROCESS STATE CODES), что значат дополнительные к основной заглавной букве статуса процессов. Его можно не учитывать при расчёте (считать S, Ss или Ssl равнозначными).**

    Наиболее часто встречающийся статус - **S** - **sleep**
    ```
    PID STAT
       1 Sl
       9 S
    1029 Ss
    1646 Ss
    1647 S
    1648 Ss
    2091 Ss
    2092 R
    2093 Ss
    2278 S+
    2286 S+
    2294 R+
    ```
    
