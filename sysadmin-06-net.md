## Ответы к домашнему заданию к занятию
# «Компьютерные сети. Лекция 1»

1. **Подключитесь утилитой telnet к сайту stackoverflow.com. Отправьте HTTP-запрос. В ответе укажите полученный HTTP-код и поясните, что он означает.**
    ```
    fedor@DESKTOP-FEKCCDN:~$ telnet stackoverflow.com 80
    Trying 151.101.193.69...
    Connected to stackoverflow.com.
    Escape character is '^]'.
    GET /questions HTTP/1.0

    HTTP/1.1 500 Domain Not Found
    Connection: close
    Content-Length: 228
    Server: Varnish
    Retry-After: 0
    content-type: text/html
    Cache-Control: private, no-cache
    X-Served-By: cache-fra-eddf8230125-FRA
    Accept-Ranges: bytes
    Date: Sat, 11 Mar 2023 07:31:58 GMT
    Via: 1.1 varnish


    <html>
    <head>
    <title>Fastly error: unknown domain </title>
    </head>
    <body>
    <p>Fastly error: unknown domain: . Please check that this domain has been added to a service.</p>
    <p>Details: cache-fra-eddf8230125-FRA</p></body></html>Connection closed by foreign host.
    fedor@DESKTOP-FEKCCDN:~$
    ```
  
    Код ответа: **500**. В RFC написано, что он обозначает::
    ```
    500 Internal Server Error

    The server encountered an unexpected condition which prevented it
    from fulfilling the request.
    ```
    
    Но в заголовке ответа сервера почему то написано **`500 Domain Not Found`** и **`Fastly error: unknown domain`**
    
2. **Повторите задание 1 в браузере, используя консоль разработчика F12. укажите в ответе полученный HTTP-код**

    Код ответа: **200**:
    ![This is an image](Capture01.PNG)
    
    **Проверьте время загрузки страницы и определите, какой запрос обрабатывался дольше всего**
    
    Дольше всего обрабатывался первый запрос, **287** миллисекунд:
    ![This is an image](Capture02.PNG)

3. **Какой IP-адрес у вас в интернете?**

    ```
    fedor@DESKTOP-FEKCCDN:~$ curl ifconfig.me
    79.164.46.76
    fedor@DESKTOP-FEKCCDN:~$
    ```

4. **Какому провайдеру принадлежит ваш IP-адрес? Какой автономной системе AS? Воспользуйтесь утилитой whois.**

    Провайдер: **Neo-CNT, Russian Central Telegraph, Moscow**:

    ```
    fedor@DESKTOP-FEKCCDN:~$ whois 79.164.46.76
    % This is the RIPE Database query service.
    % The objects are in RPSL format.
    %
    % The RIPE Database is subject to Terms and Conditions.
    % See http://www.ripe.net/db/support/db-terms-conditions.pdf

    % Note: this output has been filtered.
    %       To receive output for a database update, use the "-B" flag.

    % Information related to '79.164.32.0 - 79.164.63.255'

    % Abuse contact for '79.164.32.0 - 79.164.63.255' is 'abuse@cnt.ru'

    inetnum:        79.164.32.0 - 79.164.63.255
    netname:        Neo-CNT
    descr:          Russian Central Telegraph, Moscow
    country:        RU
    admin-c:        VYK9-RIPE
    admin-c:        AAP43-RIPE
    tech-c:         VYK9-RIPE
    status:         ASSIGNED PA
    remarks:        INFRA-AW
    mnt-by:         CNT-MNT
    created:        2011-03-30T14:09:55Z
    last-modified:  2011-03-30T14:09:55Z
    source:         RIPE # Filtered

    person:         Alexey A Petrov
    address:        7, Tverskaya st.,
    address:        Central Telegraph, Moscow,
    address:        125375, Russia
    phone:          +7 495 504 3825
    nic-hdl:        AAP43-RIPE
    mnt-by:         CNT-MNT
    remarks:        Network Administrator
    created:        2004-06-17T13:15:46Z
    last-modified:  2017-08-25T12:15:16Z
    source:         RIPE # Filtered

    person:         Victor Y. Kovalenko
    address:        Central Telegraph
    address:        7, Tverskaya st.
    address:        103375, Moscow, Russia
    phone:          +7 495 504 4414
    nic-hdl:        VYK9-RIPE
    mnt-by:         CNT-MNT
    remarks:        Network Administrator
    created:        1970-01-01T00:00:00Z
    last-modified:  2013-10-22T07:57:07Z
    source:         RIPE # Filtered

    % Information related to '79.164.0.0/16AS8615'

    route:          79.164.0.0/16
    descr:          CNT-network BLOCK
    origin:         AS8615
    mnt-by:         CNT-MNT
    created:        2013-12-17T07:03:34Z
    last-modified:  2013-12-17T07:03:34Z
    source:         RIPE

    % This query was served by the RIPE Database Query Service version 1.106 (ABERDEEN)
    ```

5. **Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой traceroute.**

    Через сети: 213.85.208.254 [AS8615], 188.254.54.237 [AS12389], 72.14.197.6 [AS15169], 108.170.225.44 [AS15169],
    108.170.250.113 [AS15169], 108.170.250.66 [AS15169], 72.14.234.20 [AS15169], 142.250.238.214 [AS15169],
    72.14.234.54 [AS15169], 142.251.238.72 [AS15169], 142.251.237.148 [AS15169], 72.14.232.86 [AS15169],
    73.142.250.56.13 [AS15169], 74.125.253.147 [AS15169], 172.253.51.187 [AS15169], 8.8.8.8 [AS15169/AS263411]

    ```
    fedor@DESKTOP-FEKCCDN:~$ traceroute -An 8.8.8.8
    traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
     1  172.23.128.1 [*]  0.689 ms  0.478 ms  0.462 ms
     2  192.168.1.1 [*]  86.388 ms  87.128 ms  87.049 ms
     3  10.182.64.1 [*]  89.487 ms  88.489 ms  88.424 ms
     4  213.85.208.254 [AS8615]  88.887 ms  88.723 ms  88.608 ms
     5  188.254.54.237 [AS12389]  186.202 ms  89.333 ms  186.079 ms
     6  * * *
     7  72.14.197.6 [AS15169]  7.217 ms  11.250 ms  11.164 ms
     8  * * *
     9  108.170.225.44 [AS15169]  7.104 ms 108.170.250.129 [AS15169]  96.875 ms 172.253.69.174 [AS15169]  95.501 ms
    10  108.170.250.113 [AS15169]  95.423 ms 108.170.250.66 [AS15169]  93.726 ms  92.429 ms
    11  72.14.234.20 [AS15169]  188.297 ms 142.250.238.214 [AS15169]  101.437 ms 72.14.234.54 [AS15169]  101.338 ms
    12  142.251.238.72 [AS15169]  100.394 ms 142.251.237.148 [AS15169]  100.256 ms 72.14.232.86 [AS15169]  100.149 ms
    13  142.250.56.13 [AS15169]  100.010 ms 74.125.253.147 [AS15169]  99.934 ms 172.253.51.187 [AS15169]  100.922 ms
    14  * * *
    15  * * *
    16  * * *
    17  * * *
    18  * * *
    19  * * *
    20  8.8.8.8 [AS15169/AS263411]  111.511 ms * *
    fedor@DESKTOP-FEKCCDN:~$
    ```

6. **Повторите задание 5 в утилите mtr. На каком участке наибольшая задержка — delay?**

    Поля **delay** найти не удалось, но поле **Pings Avg** имеет самое высокое значение в одиннадцатой строке,
    в **AS15169, GOOGLE**
    ```
                                                            My traceroute  [v0.95]
    DESKTOP-FEKCCDN (172.23.140.245) -> 8.8.8.8 (8.8.8.8)                                                  2023-03-11T13:25:58+0300
    Keys:  Help   Display mode   Restart statistics   Order of fields   quit
                                                                                           Packets               Pings
     Host                                                                                Loss%   Snt   Last   Avg  Best  Wrst StDev
     1. AS???    172.23.128.1                                                             0.0%   148    1.8   1.3   0.3   4.6   0.6
     2. AS???    192.168.1.1                                                              0.7%   148    4.2  11.6   1.3 430.8  50.6
     3. AS???    10.182.64.1                                                              0.0%   148    8.8  20.0   3.6 645.7  68.4
     4. AS8615   213.85.208.254                                                           0.0%   148    6.0  17.4   4.6 599.6  61.2
     5. AS12389  188.254.54.237                                                           0.0%   148   21.3  20.2   4.7 552.2  54.2
     6. AS12389  185.140.148.155                                                          9.5%   148   13.1  20.8   4.2 505.4  53.6
     7. AS15169  72.14.197.6                                                              0.0%   148   10.3  17.3   5.4 458.9  43.3
     8. AS15169  142.251.53.69                                                            0.0%   148   10.8  15.2   5.0 411.7  36.8
     9. AS15169  108.170.250.113                                                          8.8%   148    8.3  15.6   4.9 363.8  31.7
    10. AS15169  72.14.234.20                                                             1.4%   148   22.0  25.2  16.9 326.9  25.8
    11. AS15169  72.14.232.190                                                            1.4%   148   24.7  27.1  20.1 285.9  21.9
    12. AS15169  172.253.51.243                                                           1.4%   148   23.3  24.7  18.2 238.8  18.2
    13. (waiting for reply)
    14. (waiting for reply)
    15. (waiting for reply)
    16. (waiting for reply)
    17. (waiting for reply)
    18. (waiting for reply)
    19. (waiting for reply)
    20. (waiting for reply)
    21. (waiting for reply)
    22. AS15169  8.8.8.8                                                                  0.7%   147   19.2  31.7  16.3 546.3  64.7
    ```

7. **Какие DNS-сервера отвечают за доменное имя dns.google? Какие A-записи? Воспользуйтесь утилитой dig.**

    Ответ: Сервера **ns1.zdns.google**, **ns2.zdns.google**, **ns3.zdns.google**, **ns4.zdns.google**.

    ```
    fedor@DESKTOP-FEKCCDN:~$ dig @8.8.8.8 dns.google NS

    ; <<>> DiG 9.18.1-1ubuntu1.3-Ubuntu <<>> @8.8.8.8 dns.google NS
    ; (1 server found)
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 39093
    ;; flags: qr rd ra ad; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 512
    ;; QUESTION SECTION:
    ;dns.google.                    IN      NS

    ;; ANSWER SECTION:
    dns.google.             20319   IN      NS      ns3.zdns.google.
    dns.google.             20319   IN      NS      ns4.zdns.google.
    dns.google.             20319   IN      NS      ns1.zdns.google.
    dns.google.             20319   IN      NS      ns2.zdns.google.

    ;; Query time: 20 msec
    ;; SERVER: 8.8.8.8#53(8.8.8.8) (UDP)
    ;; WHEN: Sat Mar 11 13:43:29 MSK 2023
    ;; MSG SIZE  rcvd: 116

    fedor@DESKTOP-FEKCCDN:~$
    ```
    
    A-записи:
    ```
    fedor@DESKTOP-FEKCCDN:~$ dig @8.8.8.8 dns.google A

    ; <<>> DiG 9.18.1-1ubuntu1.3-Ubuntu <<>> @8.8.8.8 dns.google A
    ; (1 server found)
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 56777
    ;; flags: qr rd ra ad; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 512
    ;; QUESTION SECTION:
    ;dns.google.                    IN      A

    ;; ANSWER SECTION:
    dns.google.             786     IN      A       8.8.4.4
    dns.google.             786     IN      A       8.8.8.8

    ;; Query time: 20 msec
    ;; SERVER: 8.8.8.8#53(8.8.8.8) (UDP)
    ;; WHEN: Sat Mar 11 13:55:30 MSK 2023
    ;; MSG SIZE  rcvd: 71
    ```
    
8. **Проверьте PTR записи для IP-адресов из задания 7. Какое доменное имя привязано к IP? Воспользуйтесь утилитой dig.**

    Вывод для первого сервера. Адрес **216.239.32.114**, имя **ns1.zdns.google**:

    ```
    fedor@DESKTOP-FEKCCDN:~$ dig @8.8.8.8 ns1.zdns.google

    ; <<>> DiG 9.18.1-1ubuntu1.3-Ubuntu <<>> @8.8.8.8 ns1.zdns.google
    ; (1 server found)
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 43343
    ;; flags: qr rd ra ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 512
    ;; QUESTION SECTION:
    ;ns1.zdns.google.               IN      A

    ;; ANSWER SECTION:
    ns1.zdns.google.        20617   IN      A       216.239.32.114

    ;; Query time: 20 msec
    ;; SERVER: 8.8.8.8#53(8.8.8.8) (UDP)
    ;; WHEN: Sat Mar 11 13:59:07 MSK 2023
    ;; MSG SIZE  rcvd: 60

    fedor@DESKTOP-FEKCCDN:~$ dig @8.8.8.8 -x 216.239.32.114

    ; <<>> DiG 9.18.1-1ubuntu1.3-Ubuntu <<>> @8.8.8.8 -x 216.239.32.114
    ; (1 server found)
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 4867
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 512
    ;; QUESTION SECTION:
    ;114.32.239.216.in-addr.arpa.   IN      PTR

    ;; ANSWER SECTION:
    114.32.239.216.in-addr.arpa. 21328 IN   PTR     ns1.zdns.google.

    ;; Query time: 20 msec
    ;; SERVER: 8.8.8.8#53(8.8.8.8) (UDP)
    ;; WHEN: Sat Mar 11 13:59:15 MSK 2023
    ;; MSG SIZE  rcvd: 85

    fedor@DESKTOP-FEKCCDN:~$
    ```
    
    Остальные сервера:  
        **ns2.zdns.google** -> **216.239.34.114**  
        **ns3.zdns.google** -> **216.239.36.114**  
        **ns4.zdns.google** -> **216.239.38.114**  
        
    ```
     ...
    ;; ANSWER SECTION:
    ns2.zdns.google.        21282   IN      A       216.239.34.114
    ...
    ;; ANSWER SECTION:
    114.34.239.216.in-addr.arpa. 16772 IN   PTR     ns2.zdns.google.
    ...
    ;; ANSWER SECTION:
    ns3.zdns.google.        21282   IN      A       216.239.36.114
    ...
    ;; ANSWER SECTION:
    114.36.239.216.in-addr.arpa. 16772 IN   PTR     ns3.zdns.google.   
    ...
    ;; ANSWER SECTION:
    ns4.zdns.google.        21282   IN      A       216.239.38.114
    ...
    ;; ANSWER SECTION:
    114.38.239.216.in-addr.arpa. 16772 IN   PTR     ns4.zdns.google.
    ```
