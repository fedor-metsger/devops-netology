# Домашнее задание к занятию 3. «MySQL»

1. **Используя Docker, поднимите инстанс MySQL (версию 8). Данные БД сохраните в volume.**
**Изучите бэкап БД и восстановитесь из него.**
**Перейдите в управляющую консоль mysql внутри контейнера.**
**Используя команду \h, получите список управляющих команд.**
**Найдите команду для выдачи статуса БД и приведите в ответе из её вывода версию сервера БД.**

    Ответ: **8.0.33 MySQL Community Server - GPL**
  
```
mysql> status;
--------------
mysql  Ver 8.0.33 for Linux on x86_64 (MySQL Community Server - GPL)

Connection id:          12
Current database:       mysql
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
Uptime:                 38 min 42 sec

Threads: 2  Questions: 173  Slow queries: 0  Opens: 302  Flush tables: 3  Open tables: 220  Queries per second avg: 0.074
--------------

mysql>
```

   **Подключитесь к восстановленной БД и получите список таблиц из этой БД.**
```
mysql> SHOW TABLES;
+------------------------------------------------------+
| Tables_in_mysql                                      |
+------------------------------------------------------+
| columns_priv                                         |
| component                                            |
| db                                                   |
| default_roles                                        |
| engine_cost                                          |
| func                                                 |
| general_log                                          |
| global_grants                                        |
| gtid_executed                                        |
| help_category                                        |
| help_keyword                                         |
| help_relation                                        |
| help_topic                                           |
| innodb_index_stats                                   |
| innodb_table_stats                                   |
| ndb_binlog_index                                     |
| orders                                               |
| password_history                                     |
| plugin                                               |
| procs_priv                                           |
| proxies_priv                                         |
| replication_asynchronous_connection_failover         |
| replication_asynchronous_connection_failover_managed |
| replication_group_configuration_version              |
| replication_group_member_actions                     |
| role_edges                                           |
| server_cost                                          |
| servers                                              |
| slave_master_info                                    |
| slave_relay_log_info                                 |
| slave_worker_info                                    |
| slow_log                                             |
| tables_priv                                          |
| time_zone                                            |
| time_zone_leap_second                                |
| time_zone_name                                       |
| time_zone_transition                                 |
| time_zone_transition_type                            |
| user                                                 |
+------------------------------------------------------+
39 rows in set (0.00 sec)

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

