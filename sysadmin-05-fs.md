

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
    ```
    root@vagrant:/home/vagrant# mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sd[bc]1
    mdadm: Note: this array has metadata at the start and
        may not be suitable as a boot device.  If you plan to
        store '/boot' on this device please ensure that
        your boot-loader understands md/v1.x metadata, or use
        --metadata=0.90
    Continue creating array? y
    mdadm: Defaulting to version 1.2 metadata
    mdadm: array /dev/md0 started.
    root@vagrant:/home/vagrant# cat /proc/mdstat
    Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10]
    md0 : active raid1 sdc1[1] sdb1[0]
        2094080 blocks super 1.2 [2/2] [UU]
        [=============>.......]  resync = 66.5% (1394496/2094080) finish=0.0min speed=232416K/sec

    unused devices: <none>
    root@vagrant:/home/vagrant#
    ```

7. **Соберите mdadm RAID0 на второй паре маленьких разделов.**
    ```
    root@vagrant:/home/vagrant# mdadm --create /dev/md1 --level=0 --raid-devices=2 /dev/sd[bc]2
    mdadm: Defaulting to version 1.2 metadata
    mdadm: array /dev/md1 started.
    root@vagrant:/home/vagrant# cat /proc/mdstat
        Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10]
    md1 : active raid0 sdc2[1] sdb2[0]
        1141760 blocks super 1.2 512k chunks

    md0 : active raid1 sdc1[1] sdb1[0]
        2094080 blocks super 1.2 [2/2] [UU]

    unused devices: <none>
    root@vagrant:/home/vagrant#
    ```

8. **Создайте два независимых PV на получившихся md-устройствах.**
    ```
    root@vagrant:/home/vagrant# pvcreate /dev/md0
        Physical volume "/dev/md0" successfully created.
    root@vagrant:/home/vagrant# pvcreate /dev/md1
        Physical volume "/dev/md1" successfully created.
    root@vagrant:/home/vagrant#
    ```

9. **Создайте общую volume-group на этих двух PV.**
    ```
    root@vagrant:/home/vagrant# vgcreate vg_test /dev/md0 /dev/md1
        Volume group "vg_test" successfully created
    root@vagrant:/home/vagrant# vgdisplay vg_test
        --- Volume group ---
        VG Name               vg_test
        System ID
        Format                lvm2
        Metadata Areas        2
        Metadata Sequence No  1
        VG Access             read/write
        VG Status             resizable
        MAX LV                0
        Cur LV                0
        Open LV               0
        Max PV                0
        Cur PV                2
        Act PV                2
        VG Size               3.08 GiB
        PE Size               4.00 MiB
        Total PE              789
        Alloc PE / Size       0 / 0
        Free  PE / Size       789 / 3.08 GiB
        VG UUID               pWDqTd-XaE2-SyDB-XF0L-JsKV-sPWN-RUBAa6

    root@vagrant:/home/vagrant#
    ```

10. **Создайте LV размером 100 Мб, указав его расположение на PV с RAID0.**
    ```
    root@vagrant:/home/vagrant# lvcreate -L 100m vg_test -n lv_raid0 /dev/md1
        Logical volume "lv_raid0" created.
    root@vagrant:/home/vagrant# lvdisplay vg_test
        --- Logical volume ---
        LV Path                /dev/vg_test/lv_raid0
        LV Name                lv_raid0
        VG Name                vg_test
        LV UUID                0Gw93m-eeNi-uNX3-WEg1-10vH-QEMP-E5TjQv
        LV Write Access        read/write
        LV Creation host, time vagrant, 2023-03-10 13:09:16 +0000
        LV Status              available
        # open                 0
        LV Size                100.00 MiB
        Current LE             25
        Segments               1
        Allocation             inherit
        Read ahead sectors     auto
        - currently set to     4096
        Block device           253:1
    root@vagrant:/home/vagrant#
    ```

11. **Создайте mkfs.ext4 ФС на получившемся LV.**
    ```
    root@vagrant:/home/vagrant# mkfs.ext4 /dev/vg_test/lv_raid0
    mke2fs 1.45.5 (07-Jan-2020)
    Creating filesystem with 25600 4k blocks and 25600 inodes

    Allocating group tables: done
    Writing inode tables: done
    Creating journal (1024 blocks): done
    Writing superblocks and filesystem accounting information: done

    root@vagrant:/home/vagrant#
    ```

12. **Смонтируйте этот раздел в любую директорию, например, /tmp/new.**
    ```
    root@vagrant:/home/vagrant# mkdir /tmp/new
    root@vagrant:/home/vagrant# mount /dev/vg_test/lv_raid0 /tmp/new
    ```

13. **Поместите туда тестовый файл, например, wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz.**
    ```
    root@vagrant:/home/vagrant# wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz
    --2023-03-10 13:13:30--  https://mirror.yandex.ru/ubuntu/ls-lR.gz
    Resolving mirror.yandex.ru (mirror.yandex.ru)... 213.180.204.183, 2a02:6b8::183
    Connecting to mirror.yandex.ru (mirror.yandex.ru)|213.180.204.183|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 24622334 (23M) [application/octet-stream]
    Saving to: ‘/tmp/new/test.gz’

    /tmp/new/test.gz                      100%[======================================================================>]  23.48M  2.51MB/s    in 7.5s

    2023-03-10 13:13:38 (3.11 MB/s) - ‘/tmp/new/test.gz’ saved [24622334/24622334]

    root@vagrant:/home/vagrant#
    ```

14. **Прикрепите вывод lsblk.**
    ```
    root@vagrant:/home/vagrant# lsblk
    NAME                      MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
    loop0                       7:0    0  67.8M  1 loop  /snap/lxd/22753
    loop1                       7:1    0    62M  1 loop  /snap/core20/1611
    loop3                       7:3    0  49.9M  1 loop  /snap/snapd/18357
    loop4                       7:4    0  63.3M  1 loop  /snap/core20/1828
    loop5                       7:5    0  91.9M  1 loop  /snap/lxd/24061
    sda                         8:0    0    64G  0 disk
    ├─sda1                      8:1    0     1M  0 part
    ├─sda2                      8:2    0     2G  0 part  /boot
    └─sda3                      8:3    0    62G  0 part
        └─ubuntu--vg-ubuntu--lv 253:0  0    31G  0 lvm   /
    sdb                         8:16   0   2.6G  0 disk
    ├─sdb1                      8:17   0     2G  0 part
    │ └─md0                     9:0    0     2G  0 raid1
    └─sdb2                      8:18   0 559.8M  0 part
        └─md1                   9:1    0   1.1G  0 raid0
            └─vg_test-lv_raid0  253:1  0   100M  0 lvm   /tmp/new
    sdc                         8:32   0   2.6G  0 disk
    ├─sdc1                      8:33   0     2G  0 part
    │ └─md0                     9:0    0     2G  0 raid1
    └─sdc2                      8:34   0 559.8M  0 part
        └─md1                   9:1    0   1.1G  0 raid0
            └─vg_test-lv_raid0  253:1  0   100M  0 lvm   /tmp/new
    root@vagrant:/home/vagrant#
    ```

15. **Протестируйте целостность файла:**
    ```
    root@vagrant:~# gzip -t /tmp/new/test.gz
    root@vagrant:~# echo $?
    0
    ```

    Вывод:
    ```
    root@vagrant:/home/vagrant# gzip -t /tmp/new/test.gz
    root@vagrant:/home/vagrant# echo $?
    0
    root@vagrant:/home/vagrant#
    ```

16. **Используя pvmove, переместите содержимое PV с RAID0 на RAID1.**
    ```
    root@vagrant:/home/vagrant# pvmove /dev/md1 -n lv_raid0 /dev/md0
        /dev/md1: Moved: 16.00%
        /dev/md1: Moved: 100.00%
    root@vagrant:/home/vagrant#
    ```

17. **Сделайте --fail на устройство в вашем RAID1 md.**
    ```
    root@vagrant:/home/vagrant# cat /proc/mdstat
    Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10]
    md1 : active raid0 sdc2[1] sdb2[0]
        1141760 blocks super 1.2 512k chunks

    md0 : active raid1 sdc1[1] sdb1[0]
        2094080 blocks super 1.2 [2/2] [UU]

    unused devices: <none>
    root@vagrant:/home/vagrant#  mdadm /dev/md0 --fail /dev/sdb1
    mdadm: set /dev/sdb1 faulty in /dev/md0
    root@vagrant:/home/vagrant# cat /proc/mdstat
    Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10]
    md1 : active raid0 sdc2[1] sdb2[0]
        1141760 blocks super 1.2 512k chunks

    md0 : active raid1 sdc1[1] sdb1[0](F)
        2094080 blocks super 1.2 [2/1] [_U]

    unused devices: <none>
    root@vagrant:/home/vagrant#
    ```

18. **Подтвердите выводом dmesg, что RAID1 работает в деградированном состоянии.**
    ```
    [ 2384.628812] md/raid1:md0: Disk failure on sdb1, disabling device.
                   md/raid1:md0: Operation continuing on 1 devices.
    ```

19. **Протестируйте целостность файла — он должен быть доступен несмотря на «сбойный» диск:**
    ```
    root@vagrant:~# gzip -t /tmp/new/test.gz
    root@vagrant:~# echo $?
    0
    ```

    Вывод:
    ```
    root@vagrant:/home/vagrant# gzip -t /tmp/new/test.gz
    root@vagrant:/home/vagrant# echo $?
    0
    root@vagrant:/home/vagrant#
    ```
