# Домашнее задание к занятию 5. «Elasticsearch»

1. **В ответе приведите:**
  - **текст Dockerfile-манифеста,**
```
vagrant@server1:~/Netology/DevOps/hw_elastic$ cat Dockerfile

FROM centos:7

RUN yum install wget perl-Digest-SHA -y

RUN groupadd -r elasticsearch && \
    useradd -r -d /home/elasticsearch -g elasticsearch elasticsearch

RUN mkdir /var/lib/elasticsearch && \
    chown elasticsearch:elasticsearch /var/lib/elasticsearch
RUN mkdir /var/log/elasticsearch && \
    chown elasticsearch:elasticsearch /var/log/elasticsearch
RUN mkdir /home/elasticsearch && \
    chown -R elasticsearch:elasticsearch /home/elasticsearch

USER elasticsearch

WORKDIR /home/elasticsearch

COPY ./elasticsearch-8.7.0-linux-x86_64.tar.gz /home/elasticsearch
RUN tar xzvf ./elasticsearch-8.7.0-linux-x86_64.tar.gz
COPY ./elasticsearch.yml ./elasticsearch-8.7.0/config

EXPOSE 9200

ENTRYPOINT ./elasticsearch-8.7.0/bin/elasticsearch
vagrant@server1:~/Netology/DevOps/hw_elastic$
```
   - **ссылку на образ в репозитории dockerhub,**

   **[https://hub.docker.com/repository/docker/femetsger/elastic-docker](https://hub.docker.com/repository/docker/femetsger/elastic-docker)**


   - **ответ Elasticsearch на запрос пути / в json-виде.**

```
{
  "name" : "netology_test",
  "cluster_name" : "test_cluster",
  "cluster_uuid" : "tfcZA3MiSRu4e7wrC5VB0w",
  "version" : {
    "number" : "8.7.0",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "09520b59b6bc1057340b55750186466ea715e30e",
    "build_date" : "2023-03-27T16:31:09.816451435Z",
    "build_snapshot" : false,
    "lucene_version" : "9.5.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

2. **Получите список индексов и их статусов, используя API, и приведите в ответе на задание.**
```
{
    "ind-1": {
        "aliases": {},
        "mappings": {},
        "settings": {
            "index": {
                "routing": {
                    "allocation": {
                        "include": {
                            "_tier_preference": "data_content"
                        }
                    }
                },
                "number_of_shards": "1",
                "provided_name": "ind-1",
                "creation_date": "1682778441700",
                "number_of_replicas": "0",
                "uuid": "664WdcZDQwCTmhBpz6zOFA",
                "version": {
                    "created": "8070099"
                }
            }
        }
    },
    "ind-2": {
        "aliases": {},
        "mappings": {},
        "settings": {
            "index": {
                "routing": {
                    "allocation": {
                        "include": {
                            "_tier_preference": "data_content"
                        }
                    }
                },
                "number_of_shards": "2",
                "provided_name": "ind-2",
                "creation_date": "1682778586781",
                "number_of_replicas": "1",
                "uuid": "cyzBEa3sRMCs4Z1sjJt7_g",
                "version": {
                    "created": "8070099"
                }
            }
        }
    },
    "ind-3": {
        "aliases": {},
        "mappings": {},
        "settings": {
            "index": {
                "routing": {
                    "allocation": {
                        "include": {
                            "_tier_preference": "data_content"
                        }
                    }
                },
                "number_of_shards": "4",
                "provided_name": "ind-3",
                "creation_date": "1682778664940",
                "number_of_replicas": "2",
                "uuid": "Wuduwaq2SbWH1F24R-QU0w",
                "version": {
                    "created": "8070099"
                }
            }
        }
    }
}
```
Статусы индексов:
```
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   ind-1 664WdcZDQwCTmhBpz6zOFA   1   0          0            0       225b           225b
yellow open   ind-3 Wuduwaq2SbWH1F24R-QU0w   4   2          0            0       900b           900b
yellow open   ind-2 cyzBEa3sRMCs4Z1sjJt7_g   2   1          0            0       450b           450b
```

   **Получите состояние кластера Elasticsearch, используя API.**
```
{
    "cluster_name": "test_cluster",
    "status": "yellow",
    "timed_out": false,
    "number_of_nodes": 1,
    "number_of_data_nodes": 1,
    "active_primary_shards": 8,
    "active_shards": 8,
    "relocating_shards": 0,
    "initializing_shards": 0,
    "unassigned_shards": 10,
    "delayed_unassigned_shards": 0,
    "number_of_pending_tasks": 0,
    "number_of_in_flight_fetch": 0,
    "task_max_waiting_in_queue_millis": 0,
    "active_shards_percent_as_number": 44.44444444444444
}
```
  
   **Как вы думаете, почему часть индексов и кластер находятся в состоянии yellow?**

Ответ: Я думаю. статусы индексов связаны с количеством реплик. Так как в кластере всего один узел,
все реплики вынуждены размещаться на нём. И если реплик больше 0, то статус индекса становится **жёлтый**.  
А так как в кластере есть жёлтые индексы, то и сам кластер становится жёлтым.

3. **Создайте директорию {путь до корневой директории с Elasticsearch в образе}/snapshots.**
   **Используя API, зарегистрируйте эту директорию как snapshot repository c именем netology_backup.**
   **Приведите в ответе запрос API и результат вызова API для создания репозитория.**
```
wget --no-check-certificate --method=PUT --body-data='
{
    "type": "fs",
    "settings": {
        "location": "snapshots"
    }
}' https://elastic:mw6JKF23CKKtBCAbf9md@192.168.1.43:9200/_snapshot/netology_backup
```
   Ответ:
```
{
    "acknowledged": true
}
```
   **Создайте индекс test с 0 реплик и 1 шардом и приведите в ответе список индексов.**
```
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test  XuV9ustxTfC8m763ffPGNw   1   0          0            0       225b           225b
```

   **Создайте snapshot состояния кластера Elasticsearch.**
   **Приведите в ответе список файлов в директории со snapshot.**
```
total 36
-rw-r--r-- 1 elasticsearch elasticsearch   841 Apr 29 16:27 index-0
-rw-r--r-- 1 elasticsearch elasticsearch     8 Apr 29 16:27 index.latest
drwxr-xr-x 4 elasticsearch elasticsearch  4096 Apr 29 16:27 indices
-rw-r--r-- 1 elasticsearch elasticsearch 18898 Apr 29 16:27 meta-J1QQORlNQQKbHWmZc4Jn1A.dat
-rw-r--r-- 1 elasticsearch elasticsearch   350 Apr 29 16:27 snap-J1QQORlNQQKbHWmZc4Jn1A.dat
bash-4.2$
```

   **Удалите индекс test и создайте индекс test-2. Приведите в ответе список индексов.**
```
health status index  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test-2 N0Py4b_pSVyi3K5iiQpXsw   1   0          0            0       225b           225b
```
   **Восстановите состояние кластера Elasticsearch из snapshot, созданного ранее.**
   **Приведите в ответе запрос к API восстановления и итоговый список индексов.**
```
wget --no-check-certificate --method=PUT https://192.168.1.43:9200/_snapshot/netology_backup/test_snapshot/_restore
```
   Ответ:
```
{
    "accepted": true
}
```
   Список индексов:
```
health status index  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test-2 N0Py4b_pSVyi3K5iiQpXsw   1   0          0            0       225b           225b
green  open   test   kYuak2MOSGC2ESg6BFvAGQ   1   0          0            0       225b           225b
```
