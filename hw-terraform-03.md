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
