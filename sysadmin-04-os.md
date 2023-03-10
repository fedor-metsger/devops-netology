

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

6. **Запустите любой долгоживущий процесс (не ls, который отработает мгновенно, а, например, sleep 1h)
в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через nsenter.**

7. **Найдите информацию о том, что такое :(){ :|:& };:.
Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 (это важно, поведение в других ОС не проверялось).
Некоторое время всё будет плохо, после чего (спустя минуты) — ОС должна стабилизироваться.
Вызов dmesg расскажет, какой механизм помог автоматической стабилизации.
Как настроен этот механизм по умолчанию, и как изменить число процессов, которое можно создать в сессии?**

