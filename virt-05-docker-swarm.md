# Домашнее задание к занятию 5. «Оркестрация кластером Docker контейнеров на примере Docker Swarm»


### 1. Дайте письменые ответы на вопросы:
### В чём отличие режимов работы сервисов в Docker Swarm-кластере: replication и global?

В режиме **global** одна реблика сервиса запускается на каждом узле. Число реплик равно числу узлов.
В режиме **replication** запускается необходимое число реплик, безотносительно к количеству узлов.

### Какой алгоритм выбора лидера используется в Docker Swarm-кластере?

Используется **Raft consensus Algorithm**. Этот алгоримт позволяет нескольким узлам работать сплочённой группой при условии отказа некоторых её членов.
Алгоритм позволяет выдержать отказ **N-1/2** узлов (где **N** - максимальное количество узлов)

### Что такое Overlay Network?

**Overlay network** — это виртуальная сеть, работающая поверх другой сети. Устройства в этой сети "не знают", что они находятся в оверлее.
Примером такой сети являются традиционные VPN-сети, работающие через Интернет.
В **docker**-e используется для связи между собой контейнеров, работающих на разных узлах.

### 2. Создайте ваш первый Docker Swarm-кластер в Яндекс Облаке. Чтобы получить зачёт, предоставьте скриншот из терминала (консоли) с выводом команды: `docker node ls`

Ответ:
```
[root@node01 centos]# docker node ls
ID                            HOSTNAME             STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
e411bahxh6d86i38z3ql7b4pl *   node01.netology.yc   Ready     Active         Leader           23.0.2
cbf54qszds3o7gehlk1xvk9ze     node02.netology.yc   Ready     Active         Reachable        23.0.2
0s7z5ztmtls9iabgvs0wvowoz     node03.netology.yc   Ready     Active         Reachable        23.0.2
15x5xf33m0kgpeti1qjfjmg2r     node04.netology.yc   Ready     Active                          23.0.2
iw1by9ivgkh5ayzl5s3xinvox     node05.netology.yc   Ready     Active                          23.0.2
xvrr0khmu8hlv51koyn37uplj     node06.netology.yc   Ready     Active                          23.0.2
[root@node01 centos]#
```
### 3. Создайте ваш первый, готовый к боевой эксплуатации кластер мониторинга, состоящий из стека микросервисов. Чтобы получить зачёт, предоставьте скриншот из терминала (консоли), с выводом команды:
```docker service ls```
### 4. Выполните на лидере Docker Swarm-кластера команду, указанную ниже, и дайте письменное описание её функционала — что она делает и зачем нужна (см.документацию: https://docs.docker.com/engine/swarm/swarm_manager_locking/)
```docker swarm update --autolock=true):```

