Домашнее задание для третьего урока. Запускалось под Ubuntu 18.04
issue1:
Запускать:
	python3 issue1_doctest.py > log_issue1.txt - для использования с директивами
или
	python3 -m doctest -o IGNORE_EXCEPTION_DETAIL -v issue1_doctest.py > log_issue1.txt - с флагом

issue2:
Установить:
	pip3 install pytest
Запускать:
	python3 -m pytest issue2_pytest.py::test_encode > log_issue2.txt
