## Ответы к домашнему заданию к занятию
# «Компьютерные сети. Лекция 3»

1. **Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP.**
    ```
    route-views>show ip route 79.164.46.76/32
                                          ^
    % Invalid input detected at '^' marker.
    
    route-views>show ip route 79.164.46.76
    Routing entry for 79.164.0.0/16
        Known via "bgp 6447", distance 20, metric 0
        Tag 3303, type external
        Last update from 217.192.89.50 7w0d ago
        Routing Descriptor Blocks:
        * 217.192.89.50, from 217.192.89.50, 7w0d ago
            Route metric is 0, traffic share count is 1
            AS Hops 3
            Route tag 3303
            MPLS label: none
    route-views>show bgp 79.164.46.76
    BGP routing table entry for 79.164.0.0/16, version 2653821085
    Paths: (20 available, best #20, table default)
        Not advertised to any peer
        Refresh Epoch 1
        3356 12389 8615
            4.68.4.46 from 4.68.4.46 (4.69.184.201)
                Origin IGP, metric 0, localpref 100, valid, external
                Community: 3356:2 3356:22 3356:100 3356:123 3356:501 3356:903 3356:2065
                path 7FE0171601D0 RPKI State not found
                 rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        6939 12389 8615
            64.71.137.241 from 64.71.137.241 (216.218.253.53)
                Origin IGP, localpref 100, valid, external
                path 7FE0DF807BB0 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        3267 12389 8615
            194.85.40.15 from 194.85.40.15 (185.141.126.1)
                Origin IGP, metric 0, localpref 100, valid, external
                path 7FE0AED39960 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        7018 3356 12389 8615
            12.0.1.63 from 12.0.1.63 (12.0.1.63)
                Origin IGP, localpref 100, valid, external
                Community: 7018:5000 7018:37232
                path 7FE0139DE9D0 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        49788 12552 12389 8615
            91.218.184.60 from 91.218.184.60 (91.218.184.60)
                Origin IGP, localpref 100, valid, external
                Community: 12552:12000 12552:12100 12552:12101 12552:22000
                Extended Community: 0x43:100:1
                path 7FE150FB6E40 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        3549 3356 12389 8615
            208.51.134.254 from 208.51.134.254 (67.16.168.191)
                Origin IGP, metric 0, localpref 100, valid, external
                Community: 3356:2 3356:22 3356:100 3356:123 3356:501 3356:903 3356:2065 3549:2581 3549:30840
                path 7FE1246FB090 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
            20912 3257 1299 12389 8615
                212.66.96.126 from 212.66.96.126 (212.66.96.126)
                Origin IGP, localpref 100, valid, external
                Community: 3257:8066 3257:30055 3257:50001 3257:53900 3257:53902 20912:65004
                path 7FE17DA36448 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        101 3356 12389 8615
            209.124.176.223 from 209.124.176.223 (209.124.176.223)
                Origin IGP, localpref 100, valid, external
                Community: 101:20100 101:20110 101:22100 3356:2 3356:22 3356:100 3356:123 3356:501 3356:903 3356:2065
                Extended Community: RT:101:22100
                path 7FE171B8A5E8 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        852 3356 12389 8615
            154.11.12.212 from 154.11.12.212 (96.1.209.43)
                Origin IGP, metric 0, localpref 100, valid, external
                path 7FE121E13218 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        20130 6939 12389 8615
            140.192.8.16 from 140.192.8.16 (140.192.8.16)
                Origin IGP, localpref 100, valid, external
                path 7FE08D3CABE8 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        57866 3356 12389 8615
            37.139.139.17 from 37.139.139.17 (37.139.139.17)
                Origin IGP, metric 0, localpref 100, valid, external
                Community: 3356:2 3356:22 3356:100 3356:123 3356:501 3356:903 3356:2065 57866:100 65100:3356 65103:1 65104:31
                unknown transitive attribute: flag 0xE0 type 0x20 length 0x30
                    value 0000 E20A 0000 0064 0000 0D1C 0000 E20A
                          0000 0065 0000 0064 0000 E20A 0000 0067
                          0000 0001 0000 E20A 0000 0068 0000 001F

                path 7FE0128FEFE8 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        1351 6939 12389 8615
            132.198.255.253 from 132.198.255.253 (132.198.255.253)
                Origin IGP, localpref 100, valid, external
                path 7FE0DDFD6808 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        3333 1103 12389 8615
            193.0.0.56 from 193.0.0.56 (193.0.0.56)
                Origin IGP, localpref 100, valid, external
                path 7FE1119FAB08 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        3257 3356 12389 8615
            89.149.178.10 from 89.149.178.10 (213.200.83.26)
                Origin IGP, metric 10, localpref 100, valid, external
                Community: 3257:8794 3257:30043 3257:50001 3257:54900 3257:54901
                path 7FE0D707FE08 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        3561 3910 3356 12389 8615
            206.24.210.80 from 206.24.210.80 (206.24.210.80)
                Origin IGP, localpref 100, valid, external
                path 7FE09BFCEE20 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        2497 12389 8615
            202.232.0.2 from 202.232.0.2 (58.138.96.254)
                Origin IGP, localpref 100, valid, external
                path 7FE16AFE4E68 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        8283 1299 12389 8615
            94.142.247.3 from 94.142.247.3 (94.142.247.3)
                Origin IGP, metric 0, localpref 100, valid, external
                 Community: 1299:30000 8283:1 8283:101
                unknown transitive attribute: flag 0xE0 type 0x20 length 0x18
                    value 0000 205B 0000 0000 0000 0001 0000 205B
                          0000 0005 0000 0001
                path 7FE0BDEC9A28 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        19214 174 12389 8615
            208.74.64.40 from 208.74.64.40 (208.74.64.40)
                Origin IGP, localpref 100, valid, external
                Community: 174:21101 174:22005
                path 7FE00F881228 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        4901 6079 1299 12389 8615
            162.250.137.254 from 162.250.137.254 (162.250.137.254)
                Origin IGP, localpref 100, valid, external
                Community: 65000:10100 65000:10300 65000:10400
                path 7FE15D3147C0 RPKI State not found
                rx pathid: 0, tx pathid: 0
        Refresh Epoch 1
        3303 12389 8615
            217.192.89.50 from 217.192.89.50 (138.187.128.158)
                Origin IGP, localpref 100, valid, external, best
                Community: 3303:1004 3303:1006 3303:1030 3303:3056
                path 7FE11D54BFC8 RPKI State not found
                rx pathid: 0, tx pathid: 0x0
    route-views>
    ```
    
    
2. **Создайте dummy-интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.**
    ```
    root@vagrant:/home/vagrant# cat /etc/modprobe.d/dummy.conf
    options dummy numdummies=2
    root@vagrant:/home/vagrant# ip link add name dummy0 type dummy
    root@vagrant:/home/vagrant# ip link add name dummy1 type dummy
    root@vagrant:/home/vagrant# ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
            valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
            valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
        link/ether 08:00:27:59:cb:31 brd ff:ff:ff:ff:ff:ff
        inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic eth0
            valid_lft 85651sec preferred_lft 85651sec
        inet6 fe80::a00:27ff:fe59:cb31/64 scope link
            valid_lft forever preferred_lft forever
    3: dummy0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN group default qlen 1000
        link/ether 56:99:22:a7:21:e6 brd ff:ff:ff:ff:ff:ff
    4: dummy1: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN group default qlen 1000
        link/ether a6:29:b9:bf:99:76 brd ff:ff:ff:ff:ff:ff
    root@vagrant:/home/vagrant#
    ```

3. **Проверьте открытые TCP-порты в Ubuntu. Какие протоколы и приложения используют эти порты? Приведите несколько примеров.**

    Ответ: Открыты порты **80**, **22**. Приложения **apache2**, **sshd**
    ```
    fedor@DESKTOP-FEKCCDN:~$ netstat -lt --numeric-ports
    Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
    tcp6       0      0 [::]:80                 [::]:*                  LISTEN
    tcp6       0      0 [::]:22                 [::]:*                  LISTEN
    fedor@DESKTOP-FEKCCDN:~$ netstat -lt
    Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State
    tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN
    tcp6       0      0 [::]:http               [::]:*                  LISTEN
    tcp6       0      0 [::]:ssh                [::]:*                  LISTEN
    fedor@DESKTOP-FEKCCDN:~$
    ```

4. **Проверьте используемые UDP-сокеты в Ubuntu. Какие протоколы и приложения используют эти порты?**

    У меня не было никакого софта, который слушал бы UDP порты, поэтому я запустил **netcat**:

    ```
    fedor@DESKTOP-FEKCCDN:/etc/cups$ sudo netcat -ul localhost 1000
    ...
    fedor@DESKTOP-FEKCCDN:~$ netstat -lu
    Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State
    udp        0      0 localhost:1000          0.0.0.0:*
    fedor@DESKTOP-FEKCCDN:~$ ss -au
    State          Recv-Q          Send-Q                   Local Address:Port                   Peer Address:Port         Process
    UNCONN         0               0                            127.0.0.1:1000                        0.0.0.0:*
    fedor@DESKTOP-FEKCCDN:~$
    ```

5. **Используя diagrams.net, создайте L3-диаграмму вашей домашней сети или любой другой сети, с которой вы работали.**


