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
