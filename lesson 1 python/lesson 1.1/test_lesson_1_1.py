"""
Тесты к уроку 1.1: Переменные.

Запусти после выполнения домашки:
    pytest test_main.py -v

Красные тесты = ещё не доделал. Зелёные = всё верно.
"""

from variables import task_1, task_2, task_3


class TestHomework:
    def test_task_1_name_is_sasha(self):
        assert task_1() == "Саша"

    def test_task_2_number_reassigned(self):
        assert task_2() == 10

    def test_task_3_city_changed(self):
        assert task_3() == "Питер"
