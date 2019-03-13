Домашнее задание для третьего урока. Запускалось под Ubuntu 18.04
Python 3.6.7
# ISSUE1
1.
* Запускать:
* cd issue1/
* python3 issue1.py > log_issue1.txt - для использования с директивами
* или
* python3 -m doctest -o IGNORE_EXCEPTION_DETAIL -v issue1.py > log_issue1.txt - с флагом
2. Результат в log_issue1.txt
# ISSUE2
1.
* cd issue2/
* Установить:
* pip3 install pytest
* Запускать:
* python3 -m pytest issue2.py::test_encode > log_issue2.txt
2. Результат в log_issue2.txt
# ISSUE3
1.
* cd issue3/
* Запускать:
* python3 -m unittest -v issue3.py > log_issue3.txt
2. Результат в log_issue3.txt
# ISSUE4
1.
* cd issue4/
* Запускать:
* python3 -m pytest issue4_test_pytest.py -v > log_issue4.txt
2. Результат в log_issue4.txt
