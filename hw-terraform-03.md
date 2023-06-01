# Домашнее задание к занятию «Управляющие конструкции в коде Terraform»

1. **Приложите скриншот входящих правил "Группы безопасности" в ЛК Yandex Cloud или скриншот отказа в предоставлении доступа к preview версии.**

    Ответ:
    
![](Capture28.png)

4. **Выполните код. Приложите скриншот получившегося файла.**

```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ter-homeworks/03/src$ cat hosts.cfg 
[webservers]
web-1   ansible_host=158.160.59.128 
web-2   ansible_host=51.250.7.197 

[databases]
main   ansible_host=158.160.96.57 
replica   ansible_host=158.160.38.247 

[storage]
storage   ansible_host=158.160.52.129 
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ter-homeworks/03/src$
```
5. **Приложите скриншот вывода команды terrafrom output**

```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ter-homeworks/03/src$ terraform output
VMInfo = [
  {
    "fqdn" = "fhm5kja3f8hnbsl0brf7.auto.internal"
    "id" = "fhm5kja3f8hnbsl0brf7"
    "name" = "web-1"
  },
  {
    "fqdn" = "fhm2djgk9ds6tdl69nbg.auto.internal"
    "id" = "fhm2djgk9ds6tdl69nbg"
    "name" = "web-2"
  },
  {
    "fqdn" = "fhmhlmi2fujqtautqshr.auto.internal"
    "id" = "fhmhlmi2fujqtautqshr"
    "name" = "main"
  },
  {
    "fqdn" = "fhm378lv203ah80crpcs.auto.internal"
    "id" = "fhm378lv203ah80crpcs"
    "name" = "replica"
  },
  {
    "fqdn" = "fhmaoc02cq0mnes7233a.auto.internal"
    "id" = "fhmaoc02cq0mnes7233a"
    "name" = "storage"
  },
]
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ter-homeworks/03/src$
```
