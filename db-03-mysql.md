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

3. **Установите профилирование SET profiling = 1. Изучите вывод профилирования команд SHOW PROFILES;**

```
mysql> SET profiling = 1;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> SHOW PROFILES;
Empty set, 1 warning (0.00 sec)

mysql> SELECT * FROM orders;
+----+-----------------------+-------+
| id | title                 | price |
+----+-----------------------+-------+
|  1 | War and Peace         |   100 |
|  2 | My little pony        |   500 |
|  3 | Adventure mysql times |   300 |
|  4 | Server gravity falls  |   300 |
|  5 | Log gossips           |   123 |
+----+-----------------------+-------+
5 rows in set (0.01 sec)

mysql> SHOW PROFILES;
+----------+------------+----------------------+
| Query_ID | Duration   | Query                |
+----------+------------+----------------------+
|        1 | 0.00215475 | SELECT * FROM orders |
+----------+------------+----------------------+
1 row in set, 1 warning (0.00 sec)

mysql>
```

   **Исследуйте, какой engine используется в таблице БД test_db и приведите в ответе.**

   Ответ: **InnoDB**
  
```
mysql> SELECT table_name, engine
    ->   FROM information_schema.tables
    ->
    ->  WHERE table_schema = 'test_db';
+------------+--------+
| TABLE_NAME | ENGINE |
+------------+--------+
| orders     | InnoDB |
+------------+--------+
1 row in set (0.00 sec)

mysql>
```
   **Измените engine и приведите время выполнения и запрос на изменения из профайлера в ответе:**
   
   Ответ: Время выполнения:
   - На **MyISAM**: **0.00075700**
   - На **InnoDB**: **0.00215475**

```
mysql> ALTER TABLE orders ENGINE = MyISAM;
Query OK, 5 rows affected (0.05 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> SELECT table_name, engine
    ->   FROM information_schema.tables
    ->  WHERE table_schema = 'test_db';
+------------+--------+
| TABLE_NAME | ENGINE |
+------------+--------+
| orders     | MyISAM |
+------------+--------+
1 row in set (0.01 sec)

mysql> SELECT * FROM orders;
+----+-----------------------+-------+
| id | title                 | price |
+----+-----------------------+-------+
|  1 | War and Peace         |   100 |
|  2 | My little pony        |   500 |
|  3 | Adventure mysql times |   300 |
|  4 | Server gravity falls  |   300 |
|  5 | Log gossips           |   123 |
+----+-----------------------+-------+
5 rows in set (0.00 sec)

mysql> SHOW PROFILES;
+----------+------------+---------------------------------------------------------------------------------------------------------------------+
| Query_ID | Duration   | Query                                                                                                               |
+----------+------------+---------------------------------------------------------------------------------------------------------------------+
|        7 | 0.01065675 | show status like '%engine%'                                                                                         |
|        8 | 0.00022400 | status like '%engine%'                                                                                              |
|        9 | 0.00037650 | select DATABASE(), USER() limit 1                                                                                   |
|       10 | 0.00032200 | select @@character_set_client, @@character_set_connection, @@character_set_server, @@character_set_database limit 1 |
|       11 | 0.01766750 | SHOW TABLE STATUS WHERE name = 'orders'                                                                             |
|       12 | 0.00016350 | SHOW TABLE STATUS LIKE 'Engine' WHERE name = 'orders'                                                               |
|       13 | 0.01100825 | help 'show table status'                                                                                            |
|       14 | 0.01176850 | SHOW TABLE STATUS LIKE 'orders'                                                                                     |
|       15 | 0.00862725 | SELECT TABLE_NAME, ENGINE FROM information_schema.TABLES WHERE  TABLE_SCHEMA = 'dbname'                             |
|       16 | 0.00923525 | SELECT TABLE_NAME,        ENGINE FROM   information_schema.TABLES WHERE  TABLE_SCHEMA = 'test_db'                   |
|       17 | 0.00549525 | SELECT table_name, engine FROM information_schema.tables WHERE table_schema = 'test_db'                             |
|       18 | 0.00579725 | show engines                                                                                                        |
|       19 | 0.05594600 | ALTER TABLE orders ENGINE = MyISAM                                                                                  |
|       20 | 0.00903325 | SELECT table_name, engine FROM information_schema.tables  WHERE table_schema = 'test_db'                            |
|       21 | 0.00075700 | SELECT * FROM orders                                                                                                |
+----------+------------+---------------------------------------------------------------------------------------------------------------------+
15 rows in set, 1 warning (0.00 sec)

mysql>
```

4. **Изучите файл my.cnf в директории /etc/mysql.**
   **Измените его согласно ТЗ (движок InnoDB):**
   - скорость IO важнее сохранности данных;
   - нужна компрессия таблиц для экономии места на диске;
   - размер буффера с незакомиченными транзакциями 1 Мб;
   - буффер кеширования 30% от ОЗУ;
   - размер файла логов операций 100 Мб.
   
   **Приведите в ответе изменённый файл my.cnf.**
   
```
# For advice on how to change settings please see
# http://dev.mysql.com/doc/refman/8.0/en/server-configuration-defaults.html

[mysqld]

innodb_flush_method = O_DSYNC
innodb_file_per_table = 1
innodb_file_format="Barracuda"
innodb_log_buffer_size = 1M
innodb_buffer_pool_size = 300K
innodb_log_file_size = 100M

#
# Remove leading # and set to the amount of RAM for the most important data
# cache in MySQL. Start at 70% of total RAM for dedicated server, else 10%.
# innodb_buffer_pool_size = 128M
#
# Remove leading # to turn on a very important data integrity option: logging
# changes to the binary log between backups.
# log_bin
#
# Remove leading # to set options mainly useful for reporting servers.
# The server defaults are faster for transactions and fast SELECTs.
# Adjust sizes as needed, experiment to find the optimal values.
# join_buffer_size = 128M
# sort_buffer_size = 2M
# read_rnd_buffer_size = 2M

# Remove leading # to revert to previous value for default_authentication_plugin,
# this will increase compatibility with older clients. For background, see:
# https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_default_authentication_plugin
# default-authentication-plugin=mysql_native_password
skip-host-cache
skip-name-resolve
datadir=/var/lib/mysql
socket=/var/run/mysqld/mysqld.sock
secure-file-priv=/var/lib/mysql-files
user=mysql

pid-file=/var/run/mysqld/mysqld.pid
[client]
socket=/var/run/mysqld/mysqld.sock

!includedir /etc/mysql/conf.d/

```
