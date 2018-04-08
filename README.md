# Anti-Duplicator
Эта программа позволит Вам найти дубликаты файлов.

# Как запустить
Пример запуска скрипта под Linux с установленным интерпретатором python 3.
Необходимо передать аргументом путь, по которому программа будет искать дубликаты файлов.
Программа выводит имя и размер дубликатов.
```bash
$python3 duplicates.py /home/ubuntu/git

[['12', 0], ['HEAD', 23], ['HEAD', 32], ['HEAD', 205], ['HEAD', 206], ['HEAD', 214], ['HEAD', 217], ['HEAD', 220], ['ORIG_HEAD', 41], ['applypatch-msg.sample', 478], ['commit-msg.sample', 896], ['config', 259], ['description', 73], ['exclude', 240], ['index', 217], ['master', 41], ['packed-refs', 107], ['post-update.sample', 189], ['pre-applypatch.sample', 424], ['pre-commit.sample', 1642], ['pre-push.sample', 1348], ['pre-rebase.sample', 4898], ['prepare-commit-msg.sample', 1239], ['testtest', 2], ['update.sample', 3610]]
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
