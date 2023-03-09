
## Ответы к домашнему заданию к занятию
# «Работа в терминале. Лекция 2»

  Я уже имею установленную Ubuntu 22.04, поэтому задание выполнил на ней.
  
  1. **Какого типа команда cd? Попробуйте объяснить, почему она именно такого типа; опишите ход своих мыслей, если считаете что она могла бы быть другого типа.**
  
     **cd** это встроенная команда шелла. Она служит для смены текущей рабочей директории. Её нельзя выполнить в виде внешнего исполняемого файла,
     так как внешний процесс может сменить рабочую директорию для себя, но не для другого процесса. Соответственно шелл должен сам менять свою рабочую директорию.

  2. **Какая альтернатива без pipe команде grep <some_string> <some_file> | wc -l? man grep поможет в ответе на этот вопрос. Ознакомьтесь с документом о других подобных некорректных вариантах использования pipe.**

     grep имеет опцию -c, которая позволяет подсчитать число строк с совпадением.  
     Можно написать **grep -c <some_string> <some_file>**
     
  3. **Какой процесс с PID 1 является родителем для всех процессов в вашей виртуальной машине Ubuntu 20.04?**

     Процесс **init**

  4. **Как будет выглядеть команда, которая перенаправит вывод stderr ls на другую сессию терминала?**

     `ls 2> /dev/pts/<номер сессии>`

  5. **Получится ли одновременно передать команде файл на stdin и вывести ее stdout в другой файл? Приведите работающий пример.**
  
     Можно:
     ```
     root@DESKTOP-FEKCCDN:/home/fedor# cat > /tmp/file1
     qwe
     asd
     zxc
     root@DESKTOP-FEKCCDN:/home/fedor# cat < /tmp/file1 > /tmp/file2
     root@DESKTOP-FEKCCDN:/home/fedor# cat /tmp/file2
     qwe
     asd
     zxc
     ```

  6. **Получится ли вывести находясь в графическом режиме данные из PTY в какой-либо из эмуляторов TTY? Сможете ли вы наблюдать выводимые данные?**

     Получится, можно наблююать, если переключиться на этот TTY

  7. **Выполните команду bash 5>&1. К чему она приведет? Что будет, если вы выполните echo netology > /proc/$$/fd/5? Почему так происходит?**

     Первая команда запустит новый **bash**. Вывод в файловый дескриптор **5** будет перенаправлен на стандартный вывод, как правило на терминал.
     При попытке записи в него, будет происходить вывод в стандартный поток вывода:
     ```
     fedor@DESKTOP-FEKCCDN:~$ ls -l /proc/self/fd/
     total 0
     lrwx------ 1 fedor fedor 64 Mar  9 11:02 0 -> /dev/pts/0
     lrwx------ 1 fedor fedor 64 Mar  9 11:02 1 -> /dev/pts/0
     lrwx------ 1 fedor fedor 64 Mar  9 11:02 2 -> /dev/pts/0
     lr-x------ 1 fedor fedor 64 Mar  9 11:02 3 -> /proc/294/fd
     fedor@DESKTOP-FEKCCDN:~$ bash 5>&1
     fedor@DESKTOP-FEKCCDN:~$ ls -l /proc/self/fd
     total 0
     lrwx------ 1 fedor fedor 64 Mar  9 11:02 0 -> /dev/pts/0
     lrwx------ 1 fedor fedor 64 Mar  9 11:02 1 -> /dev/pts/0
     lrwx------ 1 fedor fedor 64 Mar  9 11:02 2 -> /dev/pts/0
     lr-x------ 1 fedor fedor 64 Mar  9 11:02 3 -> /proc/301/fd
     lrwx------ 1 fedor fedor 64 Mar  9 11:02 5 -> /dev/pts/0
     fedor@DESKTOP-FEKCCDN:~$ echo qweasdzxc >&5
     qweasdzxc
     fedor@DESKTOP-FEKCCDN:~$
     ```
     Вторая команда завршится с ошибкой **"No such file or directory"**, так как как файл 5 скорее всего не открыт. Если же его открыть,
     то тогда при записи в него ошибки не будет.
     ```
     fedor@DESKTOP-FEKCCDN:~$ ls -l /proc/self/fd/
     total 0
     lrwx------ 1 fedor fedor 64 Mar  9 11:09 0 -> /dev/pts/0
     lrwx------ 1 fedor fedor 64 Mar  9 11:09 1 -> /dev/pts/0
     lrwx------ 1 fedor fedor 64 Mar  9 11:09 2 -> /dev/pts/0
     lr-x------ 1 fedor fedor 64 Mar  9 11:09 3 -> /proc/306/fd
     fedor@DESKTOP-FEKCCDN:~$ echo Netology > /proc/$$/fd/5
     -bash: /proc/10/fd/5: No such file or directory
     fedor@DESKTOP-FEKCCDN:~$ exec 5>&1
     fedor@DESKTOP-FEKCCDN:~$ ls -l /proc/self/fd/
     total 0
     lrwx------ 1 fedor fedor 64 Mar  9 11:09 0 -> /dev/pts/0
     lrwx------ 1 fedor fedor 64 Mar  9 11:09 1 -> /dev/pts/0
     lrwx------ 1 fedor fedor 64 Mar  9 11:09 2 -> /dev/pts/0
     lr-x------ 1 fedor fedor 64 Mar  9 11:09 3 -> /proc/307/fd
     lrwx------ 1 fedor fedor 64 Mar  9 11:09 5 -> /dev/pts/0
     fedor@DESKTOP-FEKCCDN:~$ echo Netology > /proc/$$/fd/5
     Netology
     fedor@DESKTOP-FEKCCDN:~$
     ```

  8. **Получится ли в качестве входного потока для pipe использовать только stderr команды, не потеряв при этом отображение stdout на pty? Напоминаем: по умолчанию через pipe передается только stdout команды слева от | на stdin команды справа. Это можно сделать, поменяв стандартные потоки местами через промежуточный новый дескриптор, который вы научились создавать в предыдущем вопросе.**

     Получится:
     ```
     fedor@DESKTOP-FEKCCDN:~$ ls / 3>&1 1>&2 2>&3 | cat > /tmp/File
     bin   dev  home  lib    lib64   lost+found  mnt  proc  run   snap  sys  usr
     boot  etc  init  lib32  libx32  media       opt  root  sbin  srv   tmp  var
     fedor@DESKTOP-FEKCCDN:~$ ls /qwe 3>&1 1>&2 2>&3 | cat > /tmp/File
     fedor@DESKTOP-FEKCCDN:~$ cat /tmp/File
     ls: cannot access '/qwe': No such file or directory
     fedor@DESKTOP-FEKCCDN:~$
     ```
  9. **Что выведет команда cat /proc/$$/environ? Как еще можно получить аналогичный по содержанию вывод?**

  10. **Используя man, опишите что доступно по адресам /proc/<PID>/cmdline, /proc/<PID>/exe.**

  11. **Узнайте, какую наиболее старшую версию набора инструкций SSE поддерживает ваш процессор с помощью /proc/cpuinfo.**

  12. **При открытии нового окна терминала и vagrant ssh создается новая сессия и выделяется pty. Это можно подтвердить командой tty, которая упоминалась в лекции 3.2. Однако:**
 
  ```
    vagrant@netology1:~$ ssh localhost 'tty'
    not a tty
  ```
  
  **Почитайте, почему так происходит, и как изменить поведение.**

  13. **Бывает, что есть необходимость переместить запущенный процесс из одной сессии в другую. Попробуйте сделать это, воспользовавшись reptyr. Например, так можно перенести в screen процесс, который вы запустили по ошибке в обычной SSH-сессии.**
  14. **`sudo echo string > /root/new_file` не даст выполнить перенаправление под обычным пользователем, так как перенаправлением занимается процесс shell'а, который запущен без sudo под вашим пользователем. Для решения данной проблемы можно использовать конструкцию echo string | sudo tee /root/new_file. Узнайте что делает команда tee и почему в отличие от sudo echo команда с sudo tee будет работать.**
