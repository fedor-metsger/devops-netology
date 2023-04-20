# Домашнее задание к занятию 3. «MySQL»

1. **Используя Docker, поднимите инстанс MySQL (версию 8). Данные БД сохраните в volume.**
**Изучите бэкап БД и восстановитесь из него.**
**Перейдите в управляющую консоль mysql внутри контейнера.**
**Используя команду \h, получите список управляющих команд.**
**Найдите команду для выдачи статуса БД и приведите в ответе из её вывода версию сервера БД.**

    Ответ: **8.0.33 MySQL Community Server - GPL**
  
```
mysql> STATUS;
--------------
mysql  Ver 8.0.33 for Linux on x86_64 (MySQL Community Server - GPL)

Connection id:          14
Current database:       test_db
Current user:           root@localhost
SSL:                    Not in use
Current pager:          stdout
Using outfile:          ''
Using delimiter:        ;
Server version:         8.0.33 MySQL Community Server - GPL
Protocol version:       10
Connection:             Localhost via UNIX socket
Server characterset:    utf8mb4
Db     characterset:    utf8mb4
Client characterset:    latin1
Conn.  characterset:    latin1
UNIX socket:            /var/run/mysqld/mysqld.sock
Binary data as:         Hexadecimal
Uptime:                 1 hour 46 min 16 sec

Threads: 2  Questions: 287  Slow queries: 0  Opens: 484  Flush tables: 3  Open tables: 402  Queries per second avg: 0.045
--------------

mysql>
```

   **Подключитесь к восстановленной БД и получите список таблиц из этой БД.**
```
mysql> SHOW TABLES;
+-------------------+
| Tables_in_test_db |
+-------------------+
| orders            |
+-------------------+
1 row in set (0.01 sec)

mysql>
```
   **Приведите в ответе количество записей с price > 300.**
    
   Ответ: **1** запись.
    
```
mysql> SELECT COUNT(*)
    ->   FROM orders
    ->  WHERE PRICE > 300;
+----------+
| COUNT(*) |
+----------+
|        1 |
+----------+
1 row in set (0.00 sec)

mysql>
```
2. **Создайте пользователя test в БД c паролем test-pass, используя:**
   - плагин авторизации mysql_native_password
   - срок истечения пароля — 180 дней
   - количество попыток авторизации — 3
   - максимальное количество запросов в час — 100
   - аттрибуты пользователя:
   - Фамилия "Pretty"
   - Имя "James".
```
mysql>     CREATE USER 'test'
    -> IDENTIFIED WITH mysql_native_password BY 'test-pass'
    -> UERIES_PER_HOUR 100
  P      WITH MAX_QUERIES_PER_HOUR 100
    ->   PASSWORD EXPIRE INTERVAL 180 DAY FAILED_LOGIN_ATTEMPTS 3
    ->  ATTRIBUTE '{"fname": "James", "lname": "Pretty"}';
Query OK, 0 rows affected (0.01 sec)

mysql>
```
   
   **Предоставьте привелегии пользователю test на операции SELECT базы test_db.**
```
mysql> GRANT SELECT
    ->    ON test_db.*
    ->    TO 'test';
Query OK, 0 rows affected (0.01 sec)

mysql>   
```
   **Используя таблицу INFORMATION_SCHEMA.USER_ATTRIBUTES, получите данные по пользователю test и приведите в ответе к задаче.**
```
mysql> SELECT *
    ->   FROM INFORMATION_SCHEMA.USER_ATTRIBUTES
    ->  WHERE user = 'test';
+------+------+---------------------------------------+
| USER | HOST | ATTRIBUTE                             |
+------+------+---------------------------------------+
| test | %    | {"fname": "James", "lname": "Pretty"} |
+------+------+---------------------------------------+
1 row in set (0.00 sec)

mysql>
```


