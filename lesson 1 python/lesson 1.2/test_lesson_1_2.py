"""
Тесты к уроку 1.2: Типы данных.

Запусти после выполнения домашки:
    pytest test_main.py -v
"""

from data_types import task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9


class TestHomework:
    def test_task_1_int_variable(self):
        result = task_1()
        assert result == 25
        assert isinstance(result, int)

    def test_task_2_float_variable(self):
        result = task_2()
        assert result == 99.90
        assert isinstance(result, float)

    def test_task_3_str_variable(self):
        result = task_3()
        assert result == "Анна"
        assert isinstance(result, str)

    def test_task_4_bool_variable(self):
        result = task_4()
        assert result is True
        assert isinstance(result, bool)

    def test_task_5_str_to_int_conversion(self):
        result = task_5()
        assert result == 42
        assert isinstance(result, int)

    def test_task_6_addition(self):
        result = task_6()
        assert result == 15

    def test_task_7_string_concat(self):
        result = task_7()
        assert result == "Привет, Анна"

    def test_task_8_modulo(self):
        result = task_8()
        assert result == 1

    def test_task_9_string_repeat(self):
        result = task_9()
        assert result == "хахаха"
