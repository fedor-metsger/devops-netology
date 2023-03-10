

## Ответы к домашнему заданию к занятию
# «Файловые системы»

2. **Могут ли файлы, являющиеся жёсткой ссылкой на один объект, иметь разные права доступа и владельца? Почему?**

    Не могут, потому что это один объект с одним **inod**-ом, а права задаются в **inod**-е.

4. **Используя fdisk, разбейте первый диск на два раздела: 2 Гб и оставшееся пространство.**

    ```
    Changed type of partition 'Linux' to 'Linux raid autodetect'.

    Command (m for help): p
    Disk /dev/sdb: 2.56 GiB, 2735484928 bytes, 5342744 sectors
    Disk model: VBOX HARDDISK
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0x86d20edf

    Device     Boot   Start     End Sectors   Size Id Type
    /dev/sdb1          2048 4196351 4194304     2G fd Linux raid autodetect
    /dev/sdb2       4196352 5342743 1146392 559.8M fd Linux raid autodetect

    Command (m for help):
    ```

5. **Используя sfdisk, перенесите эту таблицу разделов на второй диск.**

    ```
    root@vagrant:/home/vagrant# sfdisk -d /dev/sdb > part_table
    root@vagrant:/home/vagrant# sfdisk /dev/sdc < part_table
    Checking that no-one is using this disk right now ... OK

    Disk /dev/sdc: 2.56 GiB, 2735484928 bytes, 5342744 sectors
    Disk model: VBOX HARDDISK
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes

    >>> Script header accepted.
    >>> Script header accepted.
    >>> Script header accepted.
    >>> Script header accepted.
    >>> Created a new DOS disklabel with disk identifier 0xf6b3e980.
    /dev/sdc1: Created a new partition 1 of type 'Linux raid autodetect' and of size 2 GiB.
    /dev/sdc2: Created a new partition 2 of type 'Linux raid autodetect' and of size 559.8 MiB.
    /dev/sdc3: Done.

    New situation:
    Disklabel type: dos
    Disk identifier: 0xf6b3e980

    Device     Boot   Start     End Sectors   Size Id Type
    /dev/sdc1          2048 4196351 4194304     2G fd Linux raid autodetect
    /dev/sdc2       4196352 5342743 1146392 559.8M fd Linux raid autodetect

    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.
    root@vagrant:/home/vagrant#
    ```

6. **Соберите mdadm RAID1 на паре разделов 2 Гб.**

7. **Соберите mdadm RAID0 на второй паре маленьких разделов.**

8. **Создайте два независимых PV на получившихся md-устройствах.**

9. **Создайте общую volume-group на этих двух PV.**

10. **Создайте LV размером 100 Мб, указав его расположение на PV с RAID0.**

11. **Создайте mkfs.ext4 ФС на получившемся LV.**

12. **Смонтируйте этот раздел в любую директорию, например, /tmp/new.**

13. **Поместите туда тестовый файл, например, wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz.**

14. **Прикрепите вывод lsblk.**

15. **Протестируйте целостность файла:**
    ```
    root@vagrant:~# gzip -t /tmp/new/test.gz
    root@vagrant:~# echo $?
    0
    ```

16. **Используя pvmove, переместите содержимое PV с RAID0 на RAID1.**

17. **Сделайте --fail на устройство в вашем RAID1 md.**

18. **Подтвердите выводом dmesg, что RAID1 работает в деградированном состоянии.**

19. **Протестируйте целостность файла — он должен быть доступен несмотря на «сбойный» диск:**
    ```
    root@vagrant:~# gzip -t /tmp/new/test.gz
    root@vagrant:~# echo $?
    0
    ```
