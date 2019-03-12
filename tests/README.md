Домашнее задание для третьего урока. Запускалось под Windows 10
Python 3.7.2 Среда: VScode
# ISSUE1
1. Варианты запуска:
* Необходимо импортировать модуль morse
* python issue1.py или
* python -m doctest -o IGNORE_EXCEPTION_DETAIL -v issue1.py
2. Результат в log_issue1.txt
# ISSUE2
1. Варианты запуска:
* Необходим пакет pytest: pip install pytest
* python -m pytest issue2.py::test_decode -v
* python -m pytest issue2.py -v
2. Результат в log_issue2.txt
# ISSUE3
1. Варианты запуска:
* python -m  unittest issue3.py -v
* Тестируемая функция не проходит flake8, тесты проходят
2. Результат в log_issue3.txt
# ISSUE4
1. Варианты запуска:
* Необходим пакет pytest: pip install pytest
* python -m pytest issue4.py -v
* python -m pytest issue4.py::test_name -v
* Тестируемая функция не проходит flake8, тесты проходят
2. Результат в log_issue4.txt
