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
    
2. **Повторите задание 1 в браузере, используя консоль разработчика F12**

3. **Какой IP-адрес у вас в интернете?**

4. **Какому провайдеру принадлежит ваш IP-адрес? Какой автономной системе AS? Воспользуйтесь утилитой whois.**

5. **Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой traceroute.**

6. **Повторите задание 5 в утилите mtr. На каком участке наибольшая задержка — delay?**

7. **Какие DNS-сервера отвечают за доменное имя dns.google? Какие A-записи? Воспользуйтесь утилитой dig.**

8. **Проверьте PTR записи для IP-адресов из задания 7. Какое доменное имя привязано к IP? Воспользуйтесь утилитой dig.**
