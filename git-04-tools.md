

## Ответы к домашнему заданию к занятию «Инструменты Git»

1. Найдите полный хеш и комментарий коммита, хеш которого начинается на **`aefea`**.

Ответ: **`aefead2207ef7e2aa5dc81a34aedf0cad4c32545`**

Команда: 
```
git show aefea
```
Вывод:
```
commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545
Author: Alisdair McDiarmid <alisdair@users.noreply.github.com>
Date:   Thu Jun 18 10:29:58 2020 -0400

    Update CHANGELOG.md

diff --git a/CHANGELOG.md b/CHANGELOG.md
index 86d70e3e0d..588d807b17 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
@@ -27,6 +27,7 @@ BUG FIXES:
...

```

2.1 Какому тегу соответствует коммит **`85024d3`**?

Ответ: **`v0.12.23`**

```
git show 85024d3
```
Вывод:
```
commit 85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23)
Author: tf-release-bot <terraform@hashicorp.com>
Date:   Thu Mar 5 20:56:10 2020 +0000

    v0.12.23

diff --git a/CHANGELOG.md b/CHANGELOG.md
index 1a9dcd0f9b..faedc8bf4e 100644
```

2.2. Сколько родителей у коммита **`b8d720`**? Напишите их хеши.

Ответ: **2** родителя, хеши:

**`56cd7859e05c36c06b56d013b55a252d0bb7e158`**

**`9ea88f22fc6269854151c571162c5bcf958bee2b`**

Команды:

```
git show b8d720
git rev-parse b8d720^1
git rev-parse b8d720^2
```
Вывод:
```
commit b8d720f8340221f2146e4e4870bf2ee0bc48f2d5
Merge: 56cd7859e0 9ea88f22fc
Author: Chris Griggs <cgriggs@hashicorp.com>
Date:   Tue Jan 21 17:45:48 2020 -0800

    Merge pull request #23916 from hashicorp/cgriggs01-stable

    [Cherrypick] community links
...
56cd7859e05c36c06b56d013b55a252d0bb7e158
...
9ea88f22fc6269854151c571162c5bcf958bee2b
```

2.3 Перечислите хеши и комментарии всех коммитов, которые были сделаны между тегами **`v0.12.23`** и **`v0.12.24`**

Команда:
```
git log v0.12.23...v0.12.24 --pretty=oneline
```
Вывод:
```
33ff1c03bb960b332be3af2e333462dde88b279e (tag: v0.12.24) v0.12.24
b14b74c4939dcab573326f4e3ee2a62e23e12f89 [Website] vmc provider links
3f235065b9347a758efadc92295b540ee0a5e26e Update CHANGELOG.md
6ae64e247b332925b872447e9ce869657281c2bf registry: Fix panic when server is unreachable
5c619ca1baf2e21a155fcdb4c264cc9e24a2a353 website: Remove links to the getting started guide's old location
06275647e2b53d97d4f0a19a0fec11f6d69820b5 Update CHANGELOG.md
d5f9411f5108260320064349b757f55c09bc4b80 command: Fix bug when using terraform login on Windows
4b6d06cc5dcb78af637bbb19c198faff37a066ed Update CHANGELOG.md
dd01a35078f040ca984cdd349f18d0b67e486c35 Update CHANGELOG.md
225466bc3e5f35baa5d07197bbc079345b77525e Cleanup after v0.12.23 release
```
2.4 Найдите коммит, в котором была создана функция func **`providerSource`**

Ответ: **`8c928e83589d90a031f811fae52a81be7153e82f`**

Команда:
```
git grep --break --heading -n -e 'providerSource' --and -e 'func'
```
Вывод:
```
internal/command/init_test.go
1635:func TestInit_providerSource(t *testing.T) {

provider_source.go
23:func providerSource(configs []*cliconfig.ProviderInstallation, services *disco.Disco) (getproviders.Source, tfdiags.Diagnostics) {
187:func providerSourceForCLIConfigLocation(loc cliconfig.ProviderInstallationLocation, services *disco.Disco) (getproviders.Source, tfdiags.Diagnostics) {
```
Команда:
```
git log -L :providerSource:provider_source.go --pretty=oneline --no-patch
```
Вывод:
```
5af1e6234ab6da412fb8637393c5a17a1b293663 main: Honor explicit provider_installation CLI config when present
92d6a30bb4e8fbad0968a9915c6d90435a4a08f6 main: skip direct provider installation for providers available locally
8c928e83589d90a031f811fae52a81be7153e82f main: Consult local directories as potential mirrors of providers
```

2.5 Найдите все коммиты, в которых была изменена функция **`globalPluginDirs`**

Ответ:
```
78b12205587fe839f10d946ea3fdc06719decb05
52dbf94834cb970b510f2fba853a5b49ad9b1a46
41ab0aef7a0fe030e84018973a64135b11abcd70
66ebff90cdfaa6938f26f908c7ebad8d547fea17
8364383c359a6b738a436d1b7745ccdce178df47
```
Команда:
```
git grep --break --heading -c -e 'globalPluginDirs' --and -e 'func'
```
Вывод:
```
plugins.go:1
```
Команда:
```
git log -L :globalPluginDirs:plugins.go --pretty=oneline --no-patch
```
Вывод:
```
78b12205587fe839f10d946ea3fdc06719decb05 Remove config.go and update things using its aliases
52dbf94834cb970b510f2fba853a5b49ad9b1a46 keep .terraform.d/plugins for discovery
41ab0aef7a0fe030e84018973a64135b11abcd70 Add missing OS_ARCH dir to global plugin paths
66ebff90cdfaa6938f26f908c7ebad8d547fea17 move some more plugin search path logic to command
8364383c359a6b738a436d1b7745ccdce178df47 Push plugin discovery down into command package
```

2.6 Кто автор функции **`synchronizedWriters`**?

Ответ: **`Такой функции нет в этом репозитории`**.

Команда:
```
git grep --break --heading -c -e 'synchronizedWriters'
```
Ничего не выводит.
