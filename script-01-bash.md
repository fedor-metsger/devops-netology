# Домашнее задание к занятию «Командная оболочка Bash: Практические навыки»

------

## Задание 1

Есть скрипт:

```bash
a=1
b=2
c=a+b
d=$a+$b
e=$(($a+$b))
```

Какие значения переменным c, d, e будут присвоены? Почему?

| Переменная  | Значение | Обоснование |
| ------------- | ------------- | ------------- |
| `c`  | a+b  | Для обращения к переменной нужно перед именем ставить знак **$** |
| `d`  | 1+2  | По умолчанию все переменные обрабатываются как строки |
| `e`  | 3 | Двойные скобки указывают на необходимость выполнения арифметических операций 

----

## Задание 2

На нашем локальном сервере упал сервис, и мы написали скрипт, который постоянно проверяет его доступность, записывая дату проверок до тех пор, пока сервис не станет доступным. После чего скрипт должен завершиться. 

В скрипте допущена ошибка, из-за которой выполнение не может завершиться, при этом место на жёстком диске постоянно уменьшается. Что необходимо сделать, чтобы его исправить:

```bash
while ((1==1)
do
	curl https://localhost:4757
	if (($? != 0))
	then
		date >> curl.log
	fi
done
```

### Ваш скрипт:

```
while ((1==1))
do
        curl https://localhost:4757
        if (($? == 0))
        then
                break
        fi
        date >> curl.log
done
```

---

## Задание 3

Необходимо написать скрипт, который проверяет доступность трёх IP: `192.168.0.1`, `173.194.222.113`, `87.250.250.242` по `80` порту и записывает результат в файл `log`. Проверять доступность необходимо пять раз для каждого узла.

### Ваш скрипт:

```
for i in {1..5}; do
        IP_ADDR=192.168.0.1
        curl --connect-timeout 1 https://$IP_ADDR:80
        if (($? != 0)); then
                echo $IP_ADDR is not available | tee -a log
        fi
        IP_ADDR=173.194.222.113
        curl --connect-timeout 1 https://$IP_ADDR:80
        if (($? != 0)); then
                echo $IP_ADDR is not available | tee -a log
        fi
        IP_ADDR=87.250.250.242
        curl --connect-timeout 1 https://$IP_ADDR:80
        if (($? != 0)); then
                echo $IP_ADDR is not available | tee -a log
        fi
done
```

---
## Задание 4

Необходимо дописать скрипт из предыдущего задания так, чтобы он выполнялся до тех пор, пока один из узлов не окажется недоступным. Если любой из узлов недоступен — IP этого узла пишется в файл error, скрипт прерывается.

### Ваш скрипт:

```
while ((1 == 1)); do
        IP_ADDR=192.168.0.1
        curl --connect-timeout 1 https://$IP_ADDR:80
        if (($? != 0)); then
                echo $IP_ADDR is not available | tee -a log
                echo $IP_ADDR | tee -a error
                break
        fi
        IP_ADDR=173.194.222.113
        curl --connect-timeout 1 https://$IP_ADDR:80
        if (($? != 0)); then
                echo $IP_ADDR is not available | tee -a log
                echo $IP_ADDR | tee -a error
                break
        fi
        IP_ADDR=87.250.250.242
        curl --connect-timeout 1 https://$IP_ADDR:80
        if (($? != 0)); then
                echo $IP_ADDR is not available | tee -a log
                echo $IP_ADDR | tee -a error
                break
        fi
done
```

---

